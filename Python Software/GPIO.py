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

try:
    import RPi.GPIO as GPIO
except:
    print ("Kann Raspberry-PI GPIO Bibliothek nicht finden, bitte mit 'sudo apt-get install python3-rpi.gpio' installieren")

import time
import threading


class GPIOner(): # Klasse für die Konfiguration der Schnittstelle mit Bedienpanel und Arduino (mit den geerbten Funktionen der Windows-Klasse

    def __init__(self, verbose, tools, commandsstack):
        self.tools = tools
        self._verbose = verbose
        self._commandsstack = commandsstack
        GPIO.setwarnings(False) # Bereits belegte Pins überschreiben
        GPIO.setmode(GPIO.BOARD) # GPIO-Nummern als Platinen-Pins definieren
        GPIO.setup(3, GPIO.IN) # Taster Vorschub - Vor
        GPIO.setup(5, GPIO.IN) # Taster Vorschub - Zurück
        GPIO.setup(7, GPIO.IN) # Arduino Reset
        #GPIO.setup(8, GPIO.OUT) # RS232 - TX (Systemintern vergeben)
        #GPIO.setup(10, GPIO.IN) # RS232 - RX (Systemintern vergeben)
        GPIO.setup(11, GPIO.OUT) # LED Taster Vorschub - Vor
        GPIO.setup(12, GPIO.IN) # Taster Vorschub - Ganz Zurück
        GPIO.setup(13, GPIO.OUT) # LED Taster Vorschub - Zurück
        GPIO.setup(15, GPIO.OUT) # LED Taster Vorschub - Ganz Zurück
        GPIO.setup(16, GPIO.IN) # Taster Säge - Vor
        GPIO.setup(18, GPIO.IN) # Taster Säge - Zurück
        GPIO.setup(19, GPIO.OUT) # LED Taster Säge - Vor
        GPIO.setup(21, GPIO.OUT) # LED Taster Säge - Zurück
        GPIO.setup(22, GPIO.IN) # Taster Säge - Sägen
        GPIO.setup(23, GPIO.OUT) # LED Taster Säge - Sägen
        #GPIO.setup(24, GPIO.IN) # Taster Reserve
        #GPIO.setup(26, GPIO.IN) # Taster Reserve

        #GPIO.setup(28, GPIO.OUT) # LED? Taster - Reserve
        #GPIO.setup(29, GPIO.OUT) # LED? Taster - Reserve
        #GPIO.setup(30, GPIO.IN) # Näherungssensor - Säge Vor  #TODO Raspberry mekert beid dem Pin
        #GPIO.setup(31, GPIO.IN) # Näherungssensor - Säge Zurück  #TODO Raspberry mekert beid dem Pin

        self.CheckInput(300) # Überwache auf Tastendrücke, Enprellzeit: 300ms
        self.ButtonPressed(0, 1, 'Booting') # LED Spielerei


    def reset_arduino (self): # Resettet den Arduino indem Pin 7 auf Masse gezogen wird (out/low), um nach 100ms wieder hochohmig zu werden (in)
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, False)
        time.sleep(0.1)
        GPIO.setup(7, GPIO.IN)


    def HW_BW_VV(self, channel): # Hardware Button "Vorschub Vor" gedrückt
        global HW_BW_VV_TS
        global HW_BW_VV_TE
        if GPIO.input(3):
            HW_BW_VV_TS = time.time()
        if not GPIO.input(3):
            HW_BW_VV_TE = time.time()
            if HW_BW_VV_TE - HW_BW_VV_TS >= 0.2: # Tastendruckdauer min. 200 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Vorschub Vor" kurz gedrückt')
                self.ButtonPressed(11, 1, "ONOFF")
                self._commandsstack.BUTTON("HW", "VV")


    def HW_BW_VZ(self, channel): # Hardware Button "Vorschub Zurück" gedrückt
        global HW_BW_VZ_TS
        global HW_BW_VZ_TE
        if GPIO.input(5):
            HW_BW_VZ_TS = time.time()
        if not GPIO.input(5):
            HW_BW_VZ_TE = time.time()
            if HW_BW_VZ_TE - HW_BW_VZ_TS >= 0.2: # Tastendruckdauer min. 200 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Vorschub Zurück" kurz gedrückt')
                self.ButtonPressed(13, 1, "ONOFF")
                self._commandsstack.BUTTON("HW", "VZ")


    def HW_BW_VGZ(self, channel): # Hardware Button "Vorschub Ganz Zurück" gedrückt
        global HW_BW_VGZ_TS
        global HW_BW_VGZ_TE
        if GPIO.input(12):
            HW_BW_VGZ_TS = time.time()
        if not GPIO.input(12):
            HW_BW_VGZ_TE = time.time()
            if HW_BW_VGZ_TE - HW_BW_VGZ_TS >= 0.2: # Tastendruckdauer min. 200 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Vorschub Ganz Zurück" kurz gedrückt')
                self.ButtonPressed(15, 1, "ONOFF")
                self._commandsstack.BUTTON("HW", "VZ", True)


    def HW_BW_SV(self, channel): # Hardware Button "Säge Vor" gedrückt
        global HW_BW_SV_TS
        global HW_BW_SV_TE
        if GPIO.input(16):
            HW_BW_SV_TS = time.time()
        if not GPIO.input(16):
            HW_BW_SV_TE = time.time()
            if HW_BW_SV_TE - HW_BW_SV_TS >= 1: # Tastendruckdauer min. 1000 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Säge Vor" lang gedrückt')
                self.ButtonPressed(19, 1, "ONOFF". 10)
                self._commandsstack.BUTTON("HW", "SV", True)
            elif HW_BW_SV_TE - HW_BW_SV_TS >= 0.2: # Tastendruckdauer min. 200 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Säge Vor" kurz gedrückt')
                self.ButtonPressed(19, 1, "ONOFF")
                self._commandsstack.BUTTON("HW", "SV")


    def HW_BW_SZ(self, channel): # Hardware Button "Säge Zurück" gedrückt
        global HW_BW_SZ_TS
        global HW_BW_SZ_TE
        if GPIO.input(18):
            HW_BW_SZ_TS = time.time()
        if not GPIO.input(18):
            HW_BW_SZ_TE = time.time()
            if HW_BW_SZ_TE - HW_BW_SZ_TS >= 1: # Tastendruckdauer min. 1000 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Säge Zurück" lang gedrückt')
                self.ButtonPressed(21, 1, "ONOFF", 10)
                self._commandsstack.BUTTON("HW", "SZ", True)
            elif HW_BW_SZ_TE - HW_BW_SZ_TS >= 0.2: # Tastendruckdauer min. 200 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Säge Zurück" kurz gedrückt')
                self.ButtonPressed(21, 1, "ONOFF")
                self._commandsstack.BUTTON("HW", "SZ")


    def HW_BW_S(self, channel): # Hardware Button "Sägen" gedrückt
        global HW_BW_S_TS
        global HW_BW_S_TE
        if GPIO.input(22):
            HW_BW_S_TS = time.time()
        if not GPIO.input(22):
            HW_BW_S_TE = time.time()
            if HW_BW_S_TE - HW_BW_S_TS >= 0.5: # Tastendruckdauer min. 500 ms
                self.tools.verbose(self._verbose, 'Hardware-Button: "Sägen" gedrückt')
                self.ButtonPressed(23, 1, "ONOFF")
                self._commandsstack.BUTTON("HW", "S")


    def CheckInput(self, debounce): # Prüft auf Tastendrücke mit Enprellzeit
        GPIO.add_event_detect(3, GPIO.BOTH, self.HW_BW_VV, bouncetime=debounce) # Taster Vorschub - Vor
        GPIO.add_event_detect(5, GPIO.BOTH, self.HW_BW_VZ, bouncetime=debounce) # Taster Vorschub - Zurück
        GPIO.add_event_detect(12, GPIO.BOTH, self.HW_BW_VGZ, bouncetime=debounce) # Taster Vorschub - Ganz Zurück
        GPIO.add_event_detect(16, GPIO.BOTH, self.HW_BW_SV, bouncetime=debounce) # Taster Säge - Vor
        GPIO.add_event_detect(18, GPIO.BOTH, self.HW_BW_SZ, bouncetime=debounce) # Taster Säge - Zurück
        GPIO.add_event_detect(22, GPIO.BOTH, self.HW_BW_S, bouncetime=debounce) # Taster Säge - Schneiden


    def CheckProximitySensor(self, debounce): # Prüft auf Annäherung an die Näherungssensoren
        GPIO.add_event_detect(30, GPIO.BOTH, callback=my_callback, bouncetime=debounce) # Näherungssensor - Säge Vor
        GPIO.add_event_detect(31, GPIO.BOTH, callback=my_callback, bouncetime=debounce) # Näherungssensor - Säge Zurück


    def ButtonPressed(self, pinout, duration, effect, loops=1): #Erzeuge Effekt nach Tastendruck in neuen Thread
        threading._start_new_thread(self.LED, (pinout, duration, effect, loops))


    def ButtonBlink(self, pinout, duration, effect, status): # Erzeuge eine Funktion die Buttons Eventgesteuert blinken lässt
        self.blinkthread_stop = threading.Event()
        if status:
            threading._start_new_thread(self.LED, (pinout, duration, effect, 0))
        else:
            self.blinkthread_stop.set() # Übergebe der Enlosschleife ein Stop-Signal


    def LED(self, pinout, duration, effect, loops=1): #Lasse LEDs verschiedene Effekte durchlaufen
        if loops == 0:
            while (not self.blinkthread_stop.is_set()):
                self.EFFECTS(pinout, duration, effect) #Kontinuierlich bis abgebrochen wird
        elif effect == 'Booting':
            self.EFFECTS(pinout, duration, "LampTest")
            for i in range(8):
                self.EFFECTS(pinout, duration, "CircleCW")
        else:
            for i in range(loops):
                self.EFFECTS(pinout, duration, effect) #Nur 'loops' mal so oft


    def EFFECTS(self, pinout, duration, effect): # Schalte LED mit verschiedenen Effekten
        if effect == "CircleCW":
            GPIO.output(11, True)
            time.sleep(duration/4)
            GPIO.output(11, False)
            GPIO.output(19, True)
            time.sleep(duration/4)
            GPIO.output(19, False)
            GPIO.output(13, True)
            time.sleep(duration/4)
            GPIO.output(13, False)
            GPIO.output(21, True)
            time.sleep(duration/4)
            GPIO.output(21, False)
        elif effect == "CircleCCW":
            GPIO.output(11, True)
            time.sleep(duration/4)
            GPIO.output(11, False)
            GPIO.output(21, True)
            time.sleep(duration/4)
            GPIO.output(21, False)
            GPIO.output(13, True)
            time.sleep(duration/4)
            GPIO.output(13, False)
            GPIO.output(19, True)
            time.sleep(duration/4)
            GPIO.output(19, False)
        elif effect == "ONOFF":
            GPIO.output(pinout, True)
            time.sleep(duration)
            GPIO.output(pinout, False)
        elif effect == "OFFON":
            time.sleep(duration)
            GPIO.output(pinout, True)
            time.sleep(duration)
            GPIO.output(pinout, False)
        elif effect == "ON":
            GPIO.output(pinout, True)
        elif effect == "OFF":
            GPIO.output(pinout, False)
        elif effect == "MovementError":
            GPIO.output(11, True)
            GPIO.output(19, True)
            GPIO.output(13, True)
            GPIO.output(21, True)
            time.sleep(duration)
            GPIO.output(11, False)
            GPIO.output(19, False)
            GPIO.output(13, False)
            GPIO.output(21, False)
        elif effect == "LampTest":
            GPIO.output(11, True)
            GPIO.output(13, True)
            GPIO.output(15, True)
            GPIO.output(19, True)
            GPIO.output(21, True)
            GPIO.output(23, True)
            time.sleep(duration)
            GPIO.output(11, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
            GPIO.output(19, False)
            GPIO.output(21, False)
            GPIO.output(23, False)

    def terminate(self): # Trennt den GPIO zuverlässig
        GPIO.remove_event_detect(3)
        GPIO.remove_event_detect(5)
        GPIO.remove_event_detect(12)
        GPIO.remove_event_detect(16)
        GPIO.remove_event_detect(18)
        GPIO.remove_event_detect(22)
        GPIO.cleanup()