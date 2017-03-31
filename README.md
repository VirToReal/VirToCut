# VirToCut
## About the project
This is a project about building and controlling a Plate Saw Machine. You can generate your own components by using the "ConstructionTemplate.scad"-File with OpenSCAD (http://www.openscad.org). Every component are adjustable in their dimensions as described in the “OpenScadDokumentation”-Folder. In OpenSCAD you also able to switch between the complete overview as the picture below and each single printable part as listened in the “OpenScadDokumentation”-Folder by using the “printmode”-Variable within the “ConstructionTemplate.scad”-File. All details are described in the file itself. 

![OpenSCAD_Preview](https://github.com/VirToReal/VirToCut/blob/master/Images/PlateSawMachine_Transp.png)
![Constructed](https://github.com/VirToReal/VirToCut/blob/master/Images/PlateSawMachine_Contructed.png)

## Necessary experience and software
To get this project to work, you need some experience in printing parts with a 3D-Printer. Also some knowledge in electrical engineering are required, because you have to make a PCB and wire up a power-supply, raspberry-pi and an arduino-mega-2560 + ramps-shield. My files for milling/etching the PCB are to be found in the "KiCad"-Folder. The Files can be edited with the KiCad-Software (http://kicad-pcb.org). I used FlatCam (http://flatcam.org) to mill the "Gerber"-Files from KiCad.

## Software used in this project
I use Python to send G-Code-Commands from the Raspberry-Pi to the Arduino over a serial interface. Marlin (http://marlinfw.org) is running on the Arduino and interprets the received G-Code-Commands and drives the engines with the RAMPS1.4 Shield (http://reprap.org/wiki/RAMPS_1.4). My Marlin-Configuration can be found in the "Marlin Firmware"-Folder. 

The Python-Software can be found in the "Python Software"-Folder. At the moment its only available in German. If its necessary, I will rewrite it in english, too. The Software is already able to generate saw-pattern-templates, to cut a plate in different sized plates automatically. 

- Homescreen

![Homescreen](https://github.com/VirToReal/VirToCut/blob/master/Images/PythonSoftware_Homescreen.png)

- Configuration-Windows

![Config1](https://github.com/VirToReal/VirToCut/blob/master/Images/PythonSoftware_Config_1.png)
![Config2](https://github.com/VirToReal/VirToCut/blob/master/Images/PythonSoftware_Config_2.png)
![Config3](https://github.com/VirToReal/VirToCut/blob/master/Images/PythonSoftware_Config_3.png)

Contact me if you want futher informations!
