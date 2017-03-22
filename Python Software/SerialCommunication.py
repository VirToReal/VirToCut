#!/usr/bin/env python
# -*- coding: utf-8 -*-

#VirToCut - Controlsoftware for a dynamical Plate-Saw-Machine
#Copyright (C) 2016  Benjamin Hirmer - hardy at virtoreal.net

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import time
import queue
import threading

# TODO - Checksumme zu jeder G-Code Zeile hinzufügen und abgleichen

try:
        import serial # Importiert die Serielle-Kommunikations-Library für Python
except:
        print('kein pySerial gefunden, bitte mit "sudo apt-get install python3-serial" nachinstallieren! ')

ps_on_sig = "M80" # G-Code zum Einschalten der Spannungsversorgung
ps_on_delay = "G4 P1500" # G-Code nach Einschalten der Spannungsversorgung um folgende Aktionen zu verzögern
infotext_after_arduino_reset = "start" # Textmeldung die ausgegeben wird wenn Arduino resettet

class SerialCommunication(): # Klasse zum senden/empfangen von G-Code über die Serielle Schnittstelle

        # Vorinitialisierte Werte von Privaten Variablen:
        _verbose = False
        _timeout = 2
        _oksig = "OK"
        _queuesize = 20
        gcoderow = ""


        def __init__ (self, verbose, tools, port, baudrate, timeout, trys, oksig, statuslabel, connectbutton, disconnectbutton, resetbutton): # Übergibt Verbindungs-Parameter beim aufrufen der Klasse
            self._verbose = verbose # Verbose-Modus überladen
            self._timeout = timeout # Timeout überladen
            self._oksig = oksig # Okay-Signal überladen
            self.trys = trys # Versuche für eines erneuten sendens bei Fehlschlag

            # Generiere Bufferspeicher für Meldungen von seriellen Schnittstelle
            self.idlebuffer = queue.Queue(self._queuesize) # Buffer für den alle Meldungen die der Arduino von sich aus sendet
            self.responsebuffer = queue.Queue(self._queuesize) # Buffer für alle Meldungen die vom Arduino erwartet werden
            self.sendingbuffer = queue.Queue(self._queuesize) # Buffer für das nacheinander abarbeiten von Befehlen die an die serielle Schnittstelle senden wollen

            self.sendingthread = None # Initialisiere 'sendingthread' als 'nicht Vorhanden' am Anfang

            # übergebe verschiedene Objekte
            self.tools = tools
            self.statuslabel = statuslabel
            self.connectbutton = connectbutton
            self.disconnectbutton = disconnectbutton
            self.resetbutton = resetbutton

            # Steuerung Spannungsversorgung
            self.supply = None # Zustand der Spannungsversorgung
            self.timeoutcount = 0 # Zähler für Abschaltung Spannungsversorgung

            # Sonstiges
            self.tools.verbose(self._verbose, "Öffne Serielle Verbindung auf Port: " + port) # Debug Info
            self.statuslabel.set_text("Verbinde...") # Ändere Label im Verbindungsfenster
            self.readreset = False # Nicht auf Arduino Reset lauschen beim Systemstart

            try:
                self.sc = serial.Serial(port=port, baudrate=baudrate, timeout=self._timeout) # Baue Serielle Verbindung auf
                self.tools.verbose(self._verbose, "Serielle Verbindung aufgebaut")
                status = "verbunden"
                self.connectbutton.set_sensitive(False) # Deaktiviere "Verbinden"-Button
                self.disconnectbutton.set_sensitive(True) # Aktiviere "Trennen"-Button
                self.resetbutton.set_sensitive(True) # Aktiviere "Reset" -Button
                self.startstopidle(True)
                self.sending('M114', False) # Momentane Position abfragen

            except Exception as errortext:
                self.tools.verbose(self._verbose, "Konnte Port mit folgender Fehlermeldung nicht öffnen:\n" + str(errortext))
                status = "nicht verbunden"
            self.statuslabel.set_text(status)


        def startstopidle(self, status): # Erzeuge Start/Stop Funktion eines Threads für das Lauschen auf dem Port
            self.idlethread_stop = threading.Event()
            if status:
                self.idlethread = threading.Thread(target=self.idle) # Lausche auf Leitung so lange diese nicht verwendet wird in einem seperaten Thread
                self.idlethread.start() # Lasse Idle-Thread anlaufen
            else:
                self.idlethread_stop.set() # Übergebe der Enlosschleife ein Stop-Signal
                self.idlethread.join() # Lasse geschlossenen Thread mit Main-Thread aufschließen


        def idle(self): # Lauschfunktion selbst
            while (not self.idlethread_stop.is_set()): # Lasse Thread so lange laufen bis Kill-Signal kommt
                if self.idlebuffer.qsize() < self._queuesize:
                    try:
                        response = self.sc.readline().strip().decode() # Decodiere empfangene Datensegmente nach Text
                        if response == "": # Leere Meldungen ignorieren
                            self.idlethread_stop.wait(1) # Warte jeweils 1 Sekunde um erneut auf Leitung zu lauschen, jedoch über das Event um den Thread bei Bedarf richtig schließen zu können
                        elif self.readreset and infotext_after_arduino_reset in response: # Reset des Arudino durchgeführt
                            self.idlebuffer.put((False, 5)) # Infomeldung: Arduino erfolgreich resettet
                            self.readreset = False # nicht mehr darauf lauschen
                        else: # Ansonsten Input-Buffer leeren
                            self.idlebuffer.put((True, response, 3)) # Stelle erhaltene Text-Lines im Main-Loop Terminal dar
                    except:
                        self.idlebuffer.put((False, 1)) # Füge Queue Fehlermeldung hinzu: "Kann Textzeile nicht lesen"
                else:
                    self.idlebuffer.put((False, 2)) # Teile der Queue-Auswertung mit, das die Schleife jetzt voll ist
                    return
            return


        def stopsending (self): # Stoppt das ausführen und senden von G-Code und resettet den Arduino (da Arduino-Buffer ebenfalls noch G-Code enthält)
            self.writethread_stop.set() # Übergebe Sendeschleife ein Stop-Signal
            self.sendingthread.join() # Lasse geschlossenen Thread mit Main-Thread aufschließen
            self.reset() # Resette Arduino
            return True

        #TODO G-Code Befehle definieren bei der die Spannungsversorgung eingeschaltet werden soll
        def sending(self, gcode, user=0): # Sendet GCode Zeilen in einem neuen Thread
            rows = 0 #zu sendende G-Code Zeilen auf 0 setzen
            self.writethread_stop = threading.Event()
            gcodelist = []
            if self.supply: #Timer zurücksetzen falls Spannungsversorgung schon Eingeschaltet 
                self.timeoutcount = 0
            else: #Ansonsten Spannungsversorgung Einschalten
                gcode = ps_on_sig + '\n' + ps_on_delay + '\n' + gcode #Kommando dafür den zu sendenen Befehl vorne anfügen, nachfolgende Aktionen verzögern bis Spannungsversorgung vollständig Eingeschaltet
                self.supply = True #Spannungsversorgung auf "Eingeschaltet" setzen
            for gcoderow in gcode.split('\n'): #Säubere G-Code Zeilen und zähle zu sendene Zeilen hoch für eine Fortschrittsanzeige
                gcoderow = gcoderow.strip() # Entferne Whitespace
                gcoderow = gcoderow.replace("\t",'') # Lösche Tabulatoren
                if len(gcoderow) == 0: # Wenn dann nichts mehr übrig bleibt, G-Code-Zeile überspringen
                    continue
                else:
                    rows += 1 #Zeilen hochzählen
                    gcodelist.append(gcoderow) #Zeile einer Liste hinzufügen

            self.startstopidle(False) # Stoppe Idle-Thread, um Überschneidungen zu vermeiden
            if self.sendingthread is not None and self.sendingthread.isAlive(): # Wenn Thread läuft -> in die Warteschlange stellen
                self.sendingbuffer.put((gcodelist, user, rows))
            else: # Ansonsten direkt ausführen
                self.sendingthread = threading.Thread(target=self.write, args=(gcodelist, user, rows)) # Sarte neuen Thread um Text zu senden
                self.sendingthread.start()
            return True


        def write(self, gcode, user, rows=None): # Schreibt "gcode" an den seriellen Port, Zeile für Zeile

            # Es ist Wichtig bei der Marlin-Firmware auf ein "ok" zu warten, da es sonst sein kann das der Buffer des Arduino überläuft.

            recv = 0 #zu erhaltende Antworten auf 0 setzen
            for gcoderow in gcode: #Verarbeite eine G-Code Zeile nach dem anderen in der Liste
                whiles = 0
                while (not self.writethread_stop.is_set()): # Sendungswiederholung bei Fehlschlag
                    if whiles >= self.trys:
                        self.responsebuffer.put((False, 1, 0)) # Füge Queue Fehlermeldung hinzu: "Sendeversuche gescheitert"
                        break

                    self.sc.write((gcoderow + "\n").encode()) # Sende G-Code mit Zeilenumbruch, zusätzlich String in Bytes umwandeln
                    self.responsebuffer.put((True, gcoderow, user))  # Stelle G-Code Text im Main-Loop Terminal dar
                    status = self.read(self._oksig) # Lausche auf eine Bestätigung von der Firmware

                    if status:
                        recv += 1 #Antworten hochzählen
                        self.responsebuffer.put((False, 10, rows, recv)) #Gebe erhaltene/gesendete Zeilen zurück
                        break
                    else:
                        self.responsebuffer.put((False, 2)) # Füge Queue Fehlermeldung hinzu: "Erneuter Sendeversuch"
                        whiles += 1 #Sende-Wiederhol-Schleifen hochzählen
                        time.sleep(0.01) # Warte bevor erneut gesendet wird

            if not self.sendingbuffer.empty(): # Falls noch Befehle zum senden anstehen, den nächsten Befehl abarbeiten
                entry = self.sendingbuffer.get_nowait() # Befehl aus Buffer holen
                self.write(entry[0], entry[1]) # Funktion noch einmal mit neuen Input ausführen
            self.startstopidle(True) # Lausche wieder auf Port nach Meldungen
            return


        def read(self, expect=None): # Liest vom seriellen Port
            while (not self.writethread_stop.is_set()):
                try:
                    response = self.sc.readline().strip().decode() # Lese Firmware-Antwort und wandle Bytestring wieder in einen String um
                except:
                    self.responsebuffer.put((False, 3)) # Füge Queue Fehlermeldung hinzu: "Kann Textzeile nicht lesen"
                    return False
                if expect is None: # Zurück wenn keine gezielte Antwort erwartet
                    return
                if expect.lower() in response.lower(): # lauschen auf gezielte Antwort
                    self.responsebuffer.put((True, response, 0))  # Stelle erhaltene Bestätigung im Main-Loop Terminal dar
                    return True
                else:
                    self.responsebuffer.put((True, response, 0)) # Stelle erhaltenen Antwort-Text im Main-Loop Terminal dar


        def reset(self): # Setzt den Arduino zurück
            self.tools.verbose(self._verbose, "Setzte Arduino zurück...")
            self.responsebuffer.put((False, 4)) # Fordere Arduino-Reset über den Reset-Pin an
            self.readreset = True # Lasse auf Antwort lauschen

        def terminate(self): # Schließt serielle Kommunikation mit dem Arduino
            self.tools.verbose(self._verbose, "Schließe serielle Verbindung mit Arduino")
            self.statuslabel.set_text("schließe Verbindung")  # Ändere Label im Verbindungsfenster
            self.sc.close()
            time.sleep(1)
            if self.sc.isOpen():
                status = "noch Verbunden"
            else:
                status = "getrennt"
            self.tools.verbose(self._verbose, "Status: " + status)
            self.statuslabel.set_text(status)  # Ändere Label im Verbindungsfenster
            self.connectbutton.set_sensitive(True) # Aktiviere "Verbinden"-Button
            self.disconnectbutton.set_sensitive(False) # Deaktiviere "Trennen"-Button
            self.resetbutton.set_sensitive(False) # Deaktiviere "Reset" -Button