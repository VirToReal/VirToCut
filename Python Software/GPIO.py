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
        #GPIO.setup(8, GPIO.OUT) # RS232 - TX
        #GPIO.setup(10, GPIO.IN) # RS232 - RX
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

        self.ButtonPressed(0, 1, 'Booting', 1) # LED Spielerei
        self.CheckInput(300) # Überwache auf Tastendrücke, Enprellzeit: 300ms


    def reset_arduino (self): # Resettet den Arduino
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, False)
        time.sleep(0.1)
        GPIO.setup(7, GPIO.IN)


    #TODO Tastendruckdauer auswerten
    def HW_BW_VV(self, channel): # Hardware Button "Vorschub Vor" gedrückt
        self.tools.verbose(self._verbose, 'Hardware-Button: "Vorschub Vor" gedrückt')
        self.ButtonPressed(11, 1, "ONOFF")
        self._commandsstack.BUTTON("HW", "VV")


    def HW_BW_VZ(self, channel): # Hardware Button "Vorschub Zurück" gedrückt
        self.tools.verbose(self._verbose, 'Hardware-Button: "Vorschub Zurück" gedrückt')
        self.ButtonPressed(13, 1, "ONOFF")
        self._commandsstack.BUTTON("HW", "VZ")


    def HW_BW_VGZ(self, channel): # Hardware Button "Vorschub Ganz Zurück" gedrückt
        self.tools.verbose(self._verbose, 'Hardware-Button: "Vorschub Ganz Zurück" gedrückt')
        self.ButtonPressed(15, 1, "ONOFF")
        self._commandsstack.BUTTON("HW", "VGZ")


    def HW_BW_SV(self, channel): # Hardware Button "Säge Vor" gedrückt
        self.tools.verbose(self._verbose, 'Hardware-Button: "Säge Vor" gedrückt')
        self.ButtonPressed(19, 1, "ONOFF")
        self._commandsstack.BUTTON("HW", "SV")


    def HW_BW_SZ(self, channel): # Hardware Button "Säge Zurück" gedrückt
        self.tools.verbose(self._verbose, 'Hardware-Button: "Säge Zurück" gedrückt')
        self.ButtonPressed(21, 1, "ONOFF")
        self._commandsstack.BUTTON("HW", "SZ")


    def HW_BW_S(self, channel): # Hardware Button "Sägen" gedrückt
        self.tools.verbose(self._verbose, 'Hardware-Button: "Sägen" gedrückt')
        self.ButtonPressed(23, 1, "ONOFF")
        self._commandsstack.BUTTON("HW", "S")


    def CheckInput(self, debounce): # Prüft auf Tastendrücke mit Enprellzeit
        GPIO.add_event_detect(3, GPIO.RISING, self.HW_BW_VV, bouncetime=debounce) # Taster Vorschub - Vor
        GPIO.add_event_detect(5, GPIO.RISING, self.HW_BW_VZ, bouncetime=debounce) # Taster Vorschub - Zurück
        GPIO.add_event_detect(12, GPIO.RISING, self.HW_BW_VGZ, bouncetime=debounce) # Taster Vorschub - Ganz Zurück
        GPIO.add_event_detect(16, GPIO.RISING, self.HW_BW_SV, bouncetime=debounce) # Taster Säge - Vor
        GPIO.add_event_detect(18, GPIO.RISING, self.HW_BW_SZ, bouncetime=debounce) # Taster Säge - Zurück
        GPIO.add_event_detect(22, GPIO.RISING, self.HW_BW_S, bouncetime=debounce) # Taster Säge - Schneiden


    def CheckProximitySensor(self, debounce): # Prüft auf Annäherung an die Näherungssensoren
        GPIO.add_event_detect(30, GPIO.RISING, callback=my_callback, bouncetime=debounce) # Näherungssensor - Säge Vor
        GPIO.add_event_detect(31, GPIO.RISING, callback=my_callback, bouncetime=debounce) # Näherungssensor - Säge Zurück


    def ButtonPressed(self, pinout, duration, effect, loops=1): #Erzeuge Effekt nach Tastendruck in neuen Thread
        threading._start_new_thread(self.LED, (pinout, duration, effect, loops))


    def ButtonBlink(self, pinout, effect, status): # Erzeuge eine Funktion die Buttons Eventgesteuert blinken lässt
        self.blinkthread_stop = threading.Event()
        if status:
            threading._start_new_thread(self.LED, (pinout, duration, effect, 0))
        else:
            self.blinkthread_stop.set() # Übergebe der Enlosschleife ein Stop-Signal


    def LED(self, pinout, duration, effect, loops=1): #Lasse LEDs verschiedene Effekte durchlaufen
        if loops == 0:
            while (not self.blinkthread_stop.is_set()):
                self.EFFECTS(pinout, duration, effect) #Kontinuierlich bis abgebrochen wird
        elif effect == 'booting':
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