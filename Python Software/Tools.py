#!/usr/bin/env python
# -*- coding: utf-8 -*-  

#VirToCut - Controlsoftware for dynamical Plate-Saw-Machine
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

from time import ctime
import os, re
from gi.repository import Gtk, Pango

try:
        import yaml # Importiert die Yaml Bibliothek
except:
        print('kein "python3-yaml" gefunden, bitte nachinstallieren! ')


class Tools: # Diese Klasse stellt Werkzeuge die von verschiedenen Oberklassen verwendet werden kann

    def __init__ (self, DebugBuffer, TerminalBuffer, label_position, infobar_items): # Übergibt Verbindungs-Parameter beim aufrufen der Klasse
        self.__DebugBuffer = DebugBuffer # Notebook/Debug - Textfeld
        self.__TerminalBuffer = TerminalBuffer # Terminal
        self.TerminalBufferTags = (self.__TerminalBuffer.create_tag("machine", foreground="#666666"), # Erzeuge Formatierungs-Tag "machine" für über das Programm gesendeten G-Code in den Terminal TextBuffer
                                   self.__TerminalBuffer.create_tag("user", weight=Pango.Weight.BOLD), # Erzeuge Formatierungs-Tag "user" für eigene Nachrichten in den Terminal TextBuffer
                                   self.__TerminalBuffer.create_tag("button", foreground="#0066ff"), # Erzeuge Formatierungs-Tag "button" für über Buttons ausgelöste Nachrichten für den Terminal TextBuffer
                                   self.__TerminalBuffer.create_tag("idle", foreground="#0066ff")) # Erzeuge Formatierungs-Tag "idle" für abgefangene Nachrichten für den Terminal TextBuffer
        self.__DebugBufferToggle = False # Notebook/Debug - Standardmäßig ausschalten
        self.__homedir = os.environ['HOME'] # Lese Absoluten Home-Pfad aus Umgebungsvariable
        self.__progdir = os.path.join(self.__homedir, ".hysac")
        self.__label_position = label_position
        self.__infobar_items = infobar_items

        self.wait_for_save = None # Variable die für das zwischenspeichern verwendet wird, wenn eine Datei bereits existiert und vom Benutzer ein Überschreiben abgefragt werden muss

        #Folgende RegEx Kombinationen wurden mit den Editor von https://regex101.com/ erzeugt:
        self.M114Check = re.compile('[xX+:]{2}([0-9.]{1,15})+\s[yY:]{2}([0-9.]{1,15})+\s[zZ:]{2}([0-9.]{1,15})+\s') #RegEx - String auf M114 Antwort prüfen und Achsen-Positionen in Gruppen aufteilen
        self.PosCheck = re.compile('[gG0-3]{1,3}|\s{1,2}[xX]-?([0-9.]{1,15})|\s[yY]-?([0-9.]{1,15})|\s[zZ]-?([0-9.]{1,15})') #RegEx - String auf G0-3 Prüfen und Achsen-Positionen in Gruppen aufteilen (RegEx String ist für "findall" vorbereitet)
        self.cutting_mask_distances = re.compile('[Aa]-?([0-9.]{1,15})|[Bb]-?([0-9.]{1,15})') #RegEx - String auf Vorschubdistanz und Schnittlänge prüfen (RegEx String ist für "findall" vorbereitet)
        self.__checknext = False # Boolische Variable die ihren Zustand wechselt wenn das gesendete Kommando 'M114' war


    def verbose (self, verbose, text, infobar=False): #Werkzeug zum senden von Meldetexten ins Terminal und den Debugger(Infobar)
        if verbose == 'Toggle': # Schalte logging je nach Checkbox Ein/Aus
            if self.__DebugBufferToggle == False:
                self.__DebugBufferToggle = True
            elif self.__DebugBufferToggle == True:
                self.__DebugBufferToggle = False

        elif verbose == 'Clear': # Wenn "Leeren" gedrückt - Textfeld leeren
            self.__DebugBuffer.set_text('')

        elif verbose == True and self.__DebugBufferToggle: # Nur wenn auch eingeschaltet
            print (str(ctime().split()[3] + " - " + str(text))) # Text in Terminal ausgeben
            self.__DebugBuffer.insert(Gtk.TextBuffer.get_end_iter(self.__DebugBuffer), ctime().split()[3] + " - " + str(text) + '\n') # Text in Notebook/Debug DebugBuffer ausgeben (An letzte Stelle)
        if infobar: #Falls ausgewählt, Meldetext auch als Einblendung verwenden
            self.infobar('ERROR', text)


    def infobar (self, message_type, message, buttons=None): #Blendet eine Info-Leiste mit Informationen ein
        if buttons == 'YES/NO': # Blende die Infobar für Dialoge ein
            self.__infobar_items[0].show()
            self.__infobar_items[2].set_text(message)
        else: # Blende die Infobar für Informationen ein, und stelle diese je nach Informationstyp dar
            if message_type == 'INFO':
                self.__infobar_items[3].set_message_type(Gtk.MessageType.INFO)
                self.__infobar_items[4].set_from_icon_name(Gtk.STOCK_DIALOG_INFO, Gtk.IconSize.LARGE_TOOLBAR)
            elif message_type == 'WARNING':
                self.__infobar_items[3].set_message_type(Gtk.MessageType.WARNING)
                self.__infobar_items[4].set_from_icon_name(Gtk.STOCK_DIALOG_WARNING, Gtk.IconSize.LARGE_TOOLBAR)
            elif message_type == 'QUESTION':
                self.__infobar_items[3].set_message_type(Gtk.MessageType.QUESTION)
                self.__infobar_items[4].set_from_icon_name(Gtk.STOCK_DIALOG_QUESTION, Gtk.IconSize.LARGE_TOOLBAR)
            elif message_type == 'ERROR':
                self.__infobar_items[3].set_message_type(Gtk.MessageType.ERROR)
                self.__infobar_items[4].set_from_icon_name(Gtk.STOCK_DIALOG_ERROR, Gtk.IconSize.LARGE_TOOLBAR)
            else:
                self.__infobar_items[3].set_message_type(Gtk.MessageType.OTHER)

            self.__infobar_items[5].set_text(message)
            self.__infobar_items[3].show()


    def terminal (self, verbose, text=None, user=0): #Werkzeug zum darstellen des Textes im Terminal, die auch an die serielle Schnittstelle gesendet werden
        if verbose == 'Clear': # Leere Terminal wenn Signal dafür erhalten
            self.__TerminalBuffer.set_text("")
        else:

            #User-Code Beschreibung: 0 = Text von Arduino; 1 = Text von Benutzer über Eingabezeile; 2 = Text von CommandStack über Buttons ausgelöst; 3 = Text von Arduino in Dauerschleife abgefangen
            if user == 0: # Darstellung maschinell dargestellten Textes
                self.__TerminalBuffer.insert_with_tags(Gtk.TextBuffer.get_end_iter(self.__TerminalBuffer), ctime().split()[3] + " - " + str(text) + '\n', self.TerminalBufferTags[0]) # Text in Terminal ausgeben (An letzte Stelle)

            elif user == 1: # Darstellung manuell übertragenen Textes über Eingabezeile
                self.__TerminalBuffer.insert_with_tags(Gtk.TextBuffer.get_end_iter(self.__TerminalBuffer), ctime().split()[3] + " - " + str(text) + '\n', self.TerminalBufferTags[1]) # Text in Terminal ausgeben (An letzte Stelle) mit Eigenvermerk
                self.check_coords('G0-3', text) #Nach Koordinaten darin suchen

            elif user == 2: # Darstellung manuell übertragenen Textes über Button
                self.__TerminalBuffer.insert_with_tags(Gtk.TextBuffer.get_end_iter(self.__TerminalBuffer), ctime().split()[3] + " - " + str(text) + '\n', self.TerminalBufferTags[2]) # Text in Terminal ausgeben (An letzte Stelle) mit Eigenvermerk

            elif user == 3: # Darstellung abgefragten maschinell erzeugten Textes
                self.__TerminalBuffer.insert_with_tags(Gtk.TextBuffer.get_end_iter(self.__TerminalBuffer), ctime().split()[3] + " - " + str(text) + '\n', self.TerminalBufferTags[3]) # Text in Terminal ausgeben (An letzte Stelle)

            if user == 0 or user == 1: # Koordinaten abfragen bei antworten von Arduino, und bei manuellen Eingaben über Eingabezeile
                if self.__checknext: # Script mitteilen das der "text" Koordinaten enthält
                    self.check_coords('M114', text)
                    self.__checknext = False
                elif text == 'M114': # Wenn nicht, prüfen ob die Anfrage nach Koordinaten darin steht
                    self.__checknext = True
                else: #Prüfe ob der Text Bewegungs-Koordinaten enthält
                    self.check_coords('G0-3', text)

            if verbose is True: # Falls angefordert, diesen auch in die Shell ausgeben
                print(str(ctime().split()[3] + " - " + str(text)))


    def check_coords (self, matchtype, position_response): #Koordinaten interpretieren und Darstellen
        if matchtype == 'M114':
            if self.M114Check.match(position_response): # Prüfe ob erhaltene Nachricht auf das Muster einer M114 Antwort passt
                regline = self.M114Check.match(position_response) # Muster assoziieren
                self.__label_position[0].set_text(regline.group(1)) # Setze Label X
                self.__label_position[1].set_text(regline.group(2)) # Setze Label Y
                self.__label_position[2].set_text(regline.group(3)) # Setze Label Z
        elif matchtype == 'G0-3':
            if self.PosCheck.findall(position_response): # Prüfe ob erhaltene Nachricht auf das Muster von zu bewegenden Achsen passt
                regline = self.PosCheck.findall(position_response) # Muster assoziieren und mehrmals anwenden bis nichts mehr übrig bleibt (Falls alle drei Achsen angegeben wurden)
                for i in regline: # Durchlaufe Matches, und greife jeweils die gefundene Achse heraus
                    if i[0]:
                        self.__label_position[0].set_text(i[0]) # Setze Label X
                    if i[1]:
                        self.__label_position[1].set_text(i[1]) # Setze Label Y
                    if i[2]:
                        self.__label_position[2].set_text(i[2]) # Setze Label Z


    def check_template (self, checkrow): # Prüft erhaltene Zeile auf Elemente der Schneidvorlage und gibt die Infos zurück
        if self.cutting_mask_distances.findall(checkrow): # Prüfe ob Zeile Schneitvolagenrelevante Informationen enthält
            feed = None #Variable vorinitialisieren
            cut = None #Variable vorinitialisieren
            regline = self.cutting_mask_distances.findall(checkrow) # Muster assoziieren und mehrmals anwenden bis nichts mehr übrig bleibt (Falls Vorschub und Schneidlänge in einer Zeile)
            for i in regline: # Durchlaufe Matches, und greife jeweils die gefundene Parameter heraus
                if i[0]:
                    feed = float(i[0])
                if i[1]:
                    cut = float(i[1])
            if feed and cut:
                return (0, feed, cut)
            else:
                return False

        elif any(x in checkrow for x in ['ROTATE','rotate']):
            return (1,None,None)
        elif any(x in checkrow for x in ['WAIT','wait']):
            return (2,None,None)
        else:
            return False


    def check_file (self, verbose, filepath): # Prüft ob eine spezifische Datei existiert
        if os.path.isfile(filepath):
            self.verbose(verbose, "Datei '" + str(filepath) + "' existiert")
            return True
        else:
            self.verbose(verbose, "Datei '" + str(filepath) + "' existiert nicht")
            return False


    def check_format (self, verbose, filepath, returning, ending): # Prüft String auf Dateikonsistenz, und gibt je nach 'returning/ending' den korrekten String zurück
        #returning = 1; Gibt Dateipfad mit Formatendung 'ending' zurück
        filepathHT = os.path.split(filepath)
        ext = os.path.splitext(filepathHT[1])
        if returning == 1: #Gebe String immer mit Dateiendung zurück
            if ext[1] == ending:
                return filepath
            elif ext[1] == '':
                return filepath + ending


    def save_file (self, verbose, filedata, filepath, override=False): # Speichert Daten in Dateipfad ab
        write = False
        if not override: #Wenn nicht eindeutig überschrieben werden soll, vorher abfragen:
            if self.check_file (verbose, filepath):
                self.infobar('QUESTION', 'Datei existiert bereits, überschreiben?', 'YES/NO')
                self.wait_for_save = (filedata, filepath)
            else:
                write = True
        else:
            write = True

        if write:
            with open(filepath, 'w') as f:
                f.write(filedata)


    def fetch_textbuffer (self, verbose, textbuffer): # Holt Text aus einem TextBuffer
        text = textbuffer.get_text(Gtk.TextBuffer.get_start_iter(textbuffer), Gtk.TextBuffer.get_end_iter(textbuffer), True)
        self.verbose(verbose, "Habe folgenden Text aus Textbuffer: '" + str(textbuffer) + "' geholt:\n" + text)
        return text


    def crtdir (self, verbose, name): # Erzeugt einen Ordner
        newdir = os.path.join(self.__progdir, *name)
        if not os.path.exists(newdir):
            os.mkdir(newdir)
            self.verbose(verbose, "Verzeichnis '" + str(name) + "' erstellt")
            return True
        else:
            self.verbose(verbose, "Verzeichnis '" + str(name) + "' existiert bereits")
            return False


    def yaml_load (self, verbose, folder, filename): # Führt YAML-Load durch (auslesen von Daten aus .yaml Datei)
        folderPath = os.path.join(*folder)
        with open(os.path.join(self.__progdir, folderPath, filename + '.yaml'), 'r') as yaml_file:
            yaml_data = yaml.load(yaml_file)
            self.verbose(verbose, "Lese .yaml Datei '" + str(filename) + "' mit folgenden Inhalt: \n" + str(yaml_data))
            return yaml_data


    def yaml_dump (self, verbose, folder, filename, data): # Führt YAML-Dump durch (ablegen von Daten in .yaml Datei)
        folderPath = os.path.join(*folder)
        with open(os.path.join(self.__progdir, folderPath, filename + '.yaml'), 'w') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
            self.verbose(verbose, "Erzeuge .yaml Datei '" + str(filename) + "' mit folgenden Inhalt: \n" + str(yaml.dump(data, default_flow_style=False)))