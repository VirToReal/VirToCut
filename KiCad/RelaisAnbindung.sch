EESchema Schematic File Version 2
LIBS:RelaisAnbindung-rescue
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:IC_raspberry
LIBS:Dispositivos_I2C
LIBS:Meine KiCad Library
LIBS:RelaisAnbindung-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Signal und Relaisanbindung Arduino/Raspberry Pi"
Date "2016-08-02"
Rev "Hirmer B."
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L RELAY_FIN94 K1
U 1 1 57986020
P 5950 1500
F 0 "K1" H 5900 1900 50  0000 C CNN
F 1 "RELAY_Stbsgr" H 6100 1000 50  0000 C CNN
F 2 "EigenbauFootprints:Relais_FIN94_Print-Socket" H 5950 1500 50  0001 C CNN
F 3 "" H 5950 1500 50  0000 C CNN
	1    5950 1500
	1    0    0    -1  
$EndComp
$Comp
L RELAY_FIN94 K2
U 1 1 579860B3
P 5950 2500
F 0 "K2" H 5900 2900 50  0000 C CNN
F 1 "RELAY_Hakrsae" H 6100 2000 50  0000 C CNN
F 2 "EigenbauFootprints:Relais_FIN94_Print-Socket" H 5950 2500 50  0001 C CNN
F 3 "" H 5950 2500 50  0000 C CNN
	1    5950 2500
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X08 P1
U 1 1 5799AA03
P 1100 1600
F 0 "P1" H 1100 2050 50  0000 C CNN
F 1 "CONN_SUPPLY2" V 1200 1600 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x08" H 1100 1600 50  0001 C CNN
F 3 "" H 1100 1600 50  0000 C CNN
	1    1100 1600
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X02 P3
U 1 1 5799D2B9
P 1100 3800
F 0 "P3" H 1100 3950 50  0000 C CNN
F 1 "CONN_Reset" V 1200 3800 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 1100 3800 50  0001 C CNN
F 3 "" H 1100 3800 50  0000 C CNN
	1    1100 3800
	-1   0    0    -1  
$EndComp
$Comp
L R R14
U 1 1 5799D7A6
P 3750 3500
F 0 "R14" V 3830 3500 50  0000 C CNN
F 1 "R470" V 3750 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 3680 3500 50  0001 C CNN
F 3 "" H 3750 3500 50  0000 C CNN
	1    3750 3500
	1    0    0    -1  
$EndComp
$Comp
L R R15
U 1 1 5799D809
P 3950 3500
F 0 "R15" V 4030 3500 50  0000 C CNN
F 1 "R470" V 3950 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 3880 3500 50  0001 C CNN
F 3 "" H 3950 3500 50  0000 C CNN
	1    3950 3500
	1    0    0    -1  
$EndComp
$Comp
L R R16
U 1 1 5799D883
P 4150 3500
F 0 "R16" V 4230 3500 50  0000 C CNN
F 1 "R10k" V 4150 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4080 3500 50  0001 C CNN
F 3 "" H 4150 3500 50  0000 C CNN
	1    4150 3500
	1    0    0    -1  
$EndComp
$Comp
L R R17
U 1 1 5799DDBD
P 4350 3500
F 0 "R17" V 4430 3500 50  0000 C CNN
F 1 "R10k" V 4350 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4280 3500 50  0001 C CNN
F 3 "" H 4350 3500 50  0000 C CNN
	1    4350 3500
	1    0    0    -1  
$EndComp
$Comp
L R R22
U 1 1 5799EDD2
P 5800 3500
F 0 "R22" V 5880 3500 50  0000 C CNN
F 1 "R10k" V 5800 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 5730 3500 50  0001 C CNN
F 3 "" H 5800 3500 50  0000 C CNN
	1    5800 3500
	1    0    0    -1  
$EndComp
$Comp
L R R23
U 1 1 5799EE43
P 6000 3500
F 0 "R23" V 6080 3500 50  0000 C CNN
F 1 "R10k" V 6000 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 5930 3500 50  0001 C CNN
F 3 "" H 6000 3500 50  0000 C CNN
	1    6000 3500
	1    0    0    -1  
$EndComp
$Comp
L R R24
U 1 1 5799EE93
P 6200 3500
F 0 "R24" V 6280 3500 50  0000 C CNN
F 1 "R10k" V 6200 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 6130 3500 50  0001 C CNN
F 3 "" H 6200 3500 50  0000 C CNN
	1    6200 3500
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P6
U 1 1 579A1DA0
P 5300 3750
F 0 "P6" H 5300 4000 50  0000 C CNN
F 1 "CONN_TV_Vr" V 5400 3750 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 5300 3750 50  0001 C CNN
F 3 "" H 5300 3750 50  0000 C CNN
	1    5300 3750
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P7
U 1 1 579A1E41
P 5300 4300
F 0 "P7" H 5300 4550 50  0000 C CNN
F 1 "CONN_TV_Zk" V 5400 4300 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 5300 4300 50  0001 C CNN
F 3 "" H 5300 4300 50  0000 C CNN
	1    5300 4300
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P8
U 1 1 579A1FB7
P 5300 4850
F 0 "P8" H 5300 5100 50  0000 C CNN
F 1 "CONN_TV_GZk" V 5400 4850 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 5300 4850 50  0001 C CNN
F 3 "" H 5300 4850 50  0000 C CNN
	1    5300 4850
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P9
U 1 1 579A2127
P 5300 5400
F 0 "P9" H 5300 5650 50  0000 C CNN
F 1 "CONN_TS_Vr" V 5400 5400 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 5300 5400 50  0001 C CNN
F 3 "" H 5300 5400 50  0000 C CNN
	1    5300 5400
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P11
U 1 1 579A2BDA
P 7400 3750
F 0 "P11" H 7400 4000 50  0000 C CNN
F 1 "CONN_TS_Zk" V 7500 3750 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7400 3750 50  0001 C CNN
F 3 "" H 7400 3750 50  0000 C CNN
	1    7400 3750
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P12
U 1 1 579A2C6A
P 7400 4300
F 0 "P12" H 7400 4550 50  0000 C CNN
F 1 "CONN_TS_Snt" V 7500 4300 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7400 4300 50  0001 C CNN
F 3 "" H 7400 4300 50  0000 C CNN
	1    7400 4300
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P13
U 1 1 579A2CCB
P 7400 4850
F 0 "P13" H 7400 5100 50  0000 C CNN
F 1 "CONN_T_Res" V 7500 4850 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7400 4850 50  0001 C CNN
F 3 "" H 7400 4850 50  0000 C CNN
	1    7400 4850
	1    0    0    -1  
$EndComp
$Comp
L ULN2803 U1
U 1 1 5799E3E2
P 3200 6550
F 0 "U1" H 3450 7050 60  0000 C CNN
F 1 "ULN2803" H 3450 6050 60  0000 C CNN
F 2 "Housings_DIP:DIP-18_W7.62mm" H 3200 6550 60  0001 C CNN
F 3 "" H 3200 6550 60  0000 C CNN
	1    3200 6550
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 579A1D33
P 2100 5400
F 0 "R5" V 2180 5400 50  0000 C CNN
F 1 "R10k" V 2100 5400 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2030 5400 50  0001 C CNN
F 3 "" H 2100 5400 50  0000 C CNN
	1    2100 5400
	1    0    0    -1  
$EndComp
$Comp
L R R7
U 1 1 579A1DE4
P 2300 5400
F 0 "R7" V 2380 5400 50  0000 C CNN
F 1 "R10k" V 2300 5400 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2230 5400 50  0001 C CNN
F 3 "" H 2300 5400 50  0000 C CNN
	1    2300 5400
	1    0    0    -1  
$EndComp
$Comp
L R R9
U 1 1 579A1F10
P 2500 5400
F 0 "R9" V 2580 5400 50  0000 C CNN
F 1 "R10k" V 2500 5400 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2430 5400 50  0001 C CNN
F 3 "" H 2500 5400 50  0000 C CNN
	1    2500 5400
	1    0    0    -1  
$EndComp
$Comp
L R R11
U 1 1 579A1F75
P 2700 5400
F 0 "R11" V 2780 5400 50  0000 C CNN
F 1 "R10k" V 2700 5400 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2630 5400 50  0001 C CNN
F 3 "" H 2700 5400 50  0000 C CNN
	1    2700 5400
	1    0    0    -1  
$EndComp
$Comp
L R R12
U 1 1 579A1FDD
P 2900 5400
F 0 "R12" V 2980 5400 50  0000 C CNN
F 1 "R10k" V 2900 5400 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2830 5400 50  0001 C CNN
F 3 "" H 2900 5400 50  0000 C CNN
	1    2900 5400
	1    0    0    -1  
$EndComp
$Comp
L R R13
U 1 1 579A2CD0
P 3100 5400
F 0 "R13" V 3180 5400 50  0000 C CNN
F 1 "R10k" V 3100 5400 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 3030 5400 50  0001 C CNN
F 3 "" H 3100 5400 50  0000 C CNN
	1    3100 5400
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X04 P14
U 1 1 579A8BF7
P 7400 5400
F 0 "P14" H 7400 5650 50  0000 C CNN
F 1 "CONN_T_Res" V 7500 5400 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x04" H 7400 5400 50  0001 C CNN
F 3 "" H 7400 5400 50  0000 C CNN
	1    7400 5400
	1    0    0    -1  
$EndComp
$Comp
L R R25
U 1 1 579AA2F3
P 6400 3500
F 0 "R25" V 6480 3500 50  0000 C CNN
F 1 "R10k" V 6400 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 6330 3500 50  0001 C CNN
F 3 "" H 6400 3500 50  0000 C CNN
	1    6400 3500
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X02 P4
U 1 1 579AB1A3
P 1100 4400
F 0 "P4" H 1100 4550 50  0000 C CNN
F 1 "CONN_SUPPLY" V 1200 4400 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 1100 4400 50  0001 C CNN
F 3 "" H 1100 4400 50  0000 C CNN
	1    1100 4400
	-1   0    0    -1  
$EndComp
$Comp
L R R18
U 1 1 579B165C
P 4950 3800
F 0 "R18" V 5030 3800 50  0000 C CNN
F 1 "R240" V 4950 3800 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4880 3800 50  0001 C CNN
F 3 "" H 4950 3800 50  0000 C CNN
	1    4950 3800
	0    1    1    0   
$EndComp
$Comp
L R R19
U 1 1 579B181E
P 4950 4350
F 0 "R19" V 5030 4350 50  0000 C CNN
F 1 "R240" V 4950 4350 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4880 4350 50  0001 C CNN
F 3 "" H 4950 4350 50  0000 C CNN
	1    4950 4350
	0    1    1    0   
$EndComp
$Comp
L R R20
U 1 1 579B18AD
P 4950 4900
F 0 "R20" V 5030 4900 50  0000 C CNN
F 1 "R240" V 4950 4900 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4880 4900 50  0001 C CNN
F 3 "" H 4950 4900 50  0000 C CNN
	1    4950 4900
	0    1    1    0   
$EndComp
$Comp
L R R21
U 1 1 579B193F
P 4950 5450
F 0 "R21" V 5030 5450 50  0000 C CNN
F 1 "R240" V 4950 5450 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4880 5450 50  0001 C CNN
F 3 "" H 4950 5450 50  0000 C CNN
	1    4950 5450
	0    1    1    0   
$EndComp
$Comp
L R R26
U 1 1 579B847B
P 7050 3800
F 0 "R26" V 7130 3800 50  0000 C CNN
F 1 "R240" V 7050 3800 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 6980 3800 50  0001 C CNN
F 3 "" H 7050 3800 50  0000 C CNN
	1    7050 3800
	0    1    1    0   
$EndComp
$Comp
L R R27
U 1 1 579B8553
P 7050 4350
F 0 "R27" V 7130 4350 50  0000 C CNN
F 1 "R240" V 7050 4350 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 6980 4350 50  0001 C CNN
F 3 "" H 7050 4350 50  0000 C CNN
	1    7050 4350
	0    1    1    0   
$EndComp
$Comp
L R R28
U 1 1 579B85F2
P 7050 4900
F 0 "R28" V 7130 4900 50  0000 C CNN
F 1 "R240" V 7050 4900 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 6980 4900 50  0001 C CNN
F 3 "" H 7050 4900 50  0000 C CNN
	1    7050 4900
	0    1    1    0   
$EndComp
$Comp
L R R29
U 1 1 579B8690
P 7050 5450
F 0 "R29" V 7130 5450 50  0000 C CNN
F 1 "R240" V 7050 5450 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 6980 5450 50  0001 C CNN
F 3 "" H 7050 5450 50  0000 C CNN
	1    7050 5450
	0    1    1    0   
$EndComp
$Comp
L F_Small F1
U 1 1 579B6161
P 3150 3550
F 0 "F1" H 3110 3610 50  0000 L CNN
F 1 "1A" H 3030 3490 50  0000 L CNN
F 2 "Fuse_Holders_and_Fuses:Fuseholder5x20_horiz_SemiClosed_Casing10x25mm" H 3150 3550 50  0001 C CNN
F 3 "" H 3150 3550 50  0000 C CNN
	1    3150 3550
	-1   0    0    1   
$EndComp
$Comp
L F_Small F3
U 1 1 579BB903
P 3650 3100
F 0 "F3" H 3610 3160 50  0000 L CNN
F 1 "1A" H 3530 3040 50  0000 L CNN
F 2 "Fuse_Holders_and_Fuses:Fuseholder5x20_horiz_SemiClosed_Casing10x25mm" H 3650 3100 50  0001 C CNN
F 3 "" H 3650 3100 50  0000 C CNN
	1    3650 3100
	-1   0    0    1   
$EndComp
Text Notes 550  3850 0    39   ~ 0
Reset\nArduino
Text Notes 550  4450 0    39   ~ 0
5V Vers.\nSpannung
Text Notes 5500 3800 0    39   ~ 0
Taster Vorschub\n- Vor
Text Notes 5500 4350 0    39   ~ 0
Taster Vorschub\n- Zurück
Text Notes 5500 4900 0    39   ~ 0
Taster Vorschub\n- Ganz Zurück
Text Notes 5500 5450 0    39   ~ 0
Taster Säge\n- Vor
Text Notes 7600 3800 0    39   ~ 0
Taster Säge\n- Zurück
Text Notes 7600 4350 0    39   ~ 0
Taster Säge\n- Schneiden
Text Notes 7600 4900 0    39   ~ 0
Reserve
Text Notes 7600 5450 0    39   ~ 0
Reserve
$Comp
L CONN_01X07 P5
U 1 1 579C7106
P 4250 2800
F 0 "P5" H 4250 3200 50  0000 C CNN
F 1 "CONN_Aux_Res" V 4350 2800 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x07" H 4250 2800 50  0001 C CNN
F 3 "" H 4250 2800 50  0000 C CNN
	1    4250 2800
	0    -1   1    0   
$EndComp
$Comp
L F_Small F2
U 1 1 579C7ACF
P 3650 2500
F 0 "F2" H 3610 2560 50  0000 L CNN
F 1 "1A" H 3530 2440 50  0000 L CNN
F 2 "Fuse_Holders_and_Fuses:Fuseholder5x20_horiz_SemiClosed_Casing10x25mm" H 3650 2500 50  0001 C CNN
F 3 "" H 3650 2500 50  0000 C CNN
	1    3650 2500
	-1   0    0    1   
$EndComp
Text Notes 600  1700 0    39   ~ 0
12V Vers.\nArduino/\nRamps Aux
$Comp
L R R1
U 1 1 579CC0A5
P 1550 2200
F 0 "R1" V 1630 2200 50  0000 C CNN
F 1 "R10k" V 1550 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 1480 2200 50  0001 C CNN
F 3 "" H 1550 2200 50  0000 C CNN
	1    1550 2200
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 579CC50D
P 1750 2200
F 0 "R3" V 1830 2200 50  0000 C CNN
F 1 "R10k" V 1750 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 1680 2200 50  0001 C CNN
F 3 "" H 1750 2200 50  0000 C CNN
	1    1750 2200
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 579CC5AF
P 1950 2200
F 0 "R4" V 2030 2200 50  0000 C CNN
F 1 "R10k" V 1950 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 1880 2200 50  0001 C CNN
F 3 "" H 1950 2200 50  0000 C CNN
	1    1950 2200
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 579CC6DD
P 2150 2200
F 0 "R6" V 2230 2200 50  0000 C CNN
F 1 "R10k" V 2150 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2080 2200 50  0001 C CNN
F 3 "" H 2150 2200 50  0000 C CNN
	1    2150 2200
	1    0    0    -1  
$EndComp
$Comp
L R R8
U 1 1 579CC785
P 2350 2200
F 0 "R8" V 2430 2200 50  0000 C CNN
F 1 "R10k" V 2350 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2280 2200 50  0001 C CNN
F 3 "" H 2350 2200 50  0000 C CNN
	1    2350 2200
	1    0    0    -1  
$EndComp
$Comp
L ULN2803 U2
U 1 1 5799A440
P 3400 1600
F 0 "U2" H 3650 2100 60  0000 C CNN
F 1 "ULN2803" H 3650 1100 60  0000 C CNN
F 2 "Housings_DIP:DIP-18_W7.62mm" H 3400 1600 60  0001 C CNN
F 3 "" H 3400 1600 60  0000 C CNN
	1    3400 1600
	1    0    0    -1  
$EndComp
$Comp
L R R10
U 1 1 579CE806
P 2550 2200
F 0 "R10" V 2630 2200 50  0000 C CNN
F 1 "R10k" V 2550 2200 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2480 2200 50  0001 C CNN
F 3 "" H 2550 2200 50  0000 C CNN
	1    2550 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1400 2400 4150 2400
Connection ~ 3200 700 
Wire Wire Line
	4900 700  4900 2750
Wire Wire Line
	5100 1850 5550 1850
Wire Wire Line
	5100 1250 5100 1850
Wire Wire Line
	5000 1450 5000 2850
Wire Wire Line
	4900 2750 5550 2750
Wire Wire Line
	5000 2850 5550 2850
Connection ~ 5000 1550
Wire Wire Line
	4200 1550 5000 1550
Wire Wire Line
	5000 1450 4200 1450
Connection ~ 5100 1350
Wire Wire Line
	4200 1350 5100 1350
Wire Wire Line
	4200 1250 5100 1250
Wire Wire Line
	1400 1850 1400 2400
Wire Wire Line
	1300 1850 1400 1850
Wire Wire Line
	3200 700  3200 850 
Wire Wire Line
	1300 700  4900 700 
Wire Wire Line
	1300 700  1300 2600
Wire Wire Line
	1300 2600 3950 2600
Wire Wire Line
	1300 1950 1300 1950
Wire Wire Line
	1650 1950 2600 1950
Wire Wire Line
	1650 1750 1650 1950
Wire Wire Line
	1300 1750 1650 1750
Wire Wire Line
	1750 1850 2600 1850
Wire Wire Line
	1750 1650 1750 2050
Wire Wire Line
	1300 1650 1750 1650
Wire Wire Line
	1850 1750 2600 1750
Wire Wire Line
	1850 1550 1850 1750
Wire Wire Line
	1300 1550 1850 1550
Wire Wire Line
	1950 1650 2600 1650
Wire Wire Line
	1950 1450 1950 1650
Wire Wire Line
	1300 1450 1950 1450
Connection ~ 2150 1450
Wire Wire Line
	2150 1550 2150 1450
Wire Wire Line
	2600 1550 2150 1550
Wire Wire Line
	2050 1450 2600 1450
Wire Wire Line
	2050 1350 2050 1450
Wire Wire Line
	1300 1350 2050 1350
Connection ~ 2150 1250
Wire Wire Line
	2150 1350 2600 1350
Wire Wire Line
	2150 1250 2150 1350
Wire Wire Line
	1300 1250 2600 1250
Wire Wire Line
	4900 1750 5550 1750
Wire Wire Line
	5200 2250 5550 2250
Wire Wire Line
	5200 1250 5550 1250
Connection ~ 4900 1750
Wire Wire Line
	2250 3550 2000 3550
Wire Wire Line
	2000 3550 2000 3300
Wire Wire Line
	4600 3300 4600 5250
Wire Wire Line
	4600 3600 5100 3600
Wire Wire Line
	3650 3700 5100 3700
Wire Wire Line
	4600 4150 5100 4150
Connection ~ 4600 3600
Wire Wire Line
	3950 4250 5100 4250
Wire Wire Line
	4600 4700 5100 4700
Connection ~ 4600 4150
Wire Wire Line
	3850 4800 5100 4800
Wire Wire Line
	4600 5250 5100 5250
Connection ~ 4600 4700
Wire Wire Line
	3650 5350 5100 5350
Wire Wire Line
	7200 3700 6300 3700
Wire Wire Line
	6300 4000 6300 3700
Wire Wire Line
	4250 4000 6300 4000
Wire Wire Line
	4250 4000 4250 4350
Wire Wire Line
	6700 4150 7200 4150
Connection ~ 6700 3600
Wire Wire Line
	7200 4250 6300 4250
Wire Wire Line
	6300 4550 6300 4250
Wire Wire Line
	3050 4550 6300 4550
Wire Wire Line
	1300 3850 2250 3850
Wire Wire Line
	3350 3200 3350 4150
Wire Wire Line
	1450 3200 9250 3200
Wire Wire Line
	3750 3200 3750 3350
Wire Wire Line
	3950 3200 3950 3350
Connection ~ 3750 3200
Wire Wire Line
	4150 3200 4150 3350
Connection ~ 3950 3200
Wire Wire Line
	3750 3650 3750 3700
Connection ~ 3750 3700
Wire Wire Line
	3950 3650 3950 4900
Connection ~ 3950 4250
Wire Wire Line
	4150 3650 4150 4800
Connection ~ 4150 4800
Wire Wire Line
	4350 3200 4350 3350
Connection ~ 4150 3200
Wire Wire Line
	4350 3650 4350 5350
Connection ~ 4350 5350
Wire Wire Line
	6700 4700 7200 4700
Connection ~ 6700 4150
Wire Wire Line
	6000 4800 7200 4800
Wire Wire Line
	6000 5150 6000 4800
Wire Wire Line
	3750 5150 6000 5150
Wire Wire Line
	6700 3300 6700 5250
Wire Wire Line
	5800 3200 5800 3350
Connection ~ 4350 3200
Wire Wire Line
	6000 3200 6000 3350
Connection ~ 5800 3200
Wire Wire Line
	6200 3200 6200 3350
Connection ~ 6000 3200
Wire Wire Line
	5800 3650 5800 4000
Connection ~ 5800 4000
Wire Wire Line
	6000 3650 6000 4550
Connection ~ 6000 4550
Wire Wire Line
	6200 3650 6200 4800
Connection ~ 6200 4800
Connection ~ 3350 3200
Wire Wire Line
	3050 4050 3850 4050
Wire Wire Line
	3850 4050 3850 4800
Wire Wire Line
	3050 4250 3650 4250
Wire Wire Line
	3650 4250 3650 5350
Wire Wire Line
	4250 4350 3050 4350
Wire Wire Line
	4700 3100 4700 5450
Connection ~ 4700 3800
Connection ~ 4700 4350
Connection ~ 4700 4900
Wire Wire Line
	6800 3100 6800 5450
Connection ~ 6200 3200
Connection ~ 6800 3800
Connection ~ 6800 4350
Wire Wire Line
	1450 3200 1450 7400
Wire Wire Line
	1450 7400 3000 7400
Wire Wire Line
	3000 7400 3000 7300
Wire Wire Line
	2250 4050 2000 4050
Wire Wire Line
	2000 4050 2000 6200
Wire Wire Line
	2000 6200 2400 6200
Wire Wire Line
	2250 4150 1900 4150
Wire Wire Line
	1900 4150 1900 6300
Wire Wire Line
	1900 6300 2400 6300
Wire Wire Line
	2250 4250 1800 4250
Wire Wire Line
	1800 4250 1800 6400
Wire Wire Line
	1800 6400 2400 6400
Wire Wire Line
	2250 4450 1700 4450
Wire Wire Line
	1700 4450 1700 6500
Wire Wire Line
	1700 6500 2400 6500
Wire Wire Line
	2250 4550 1600 4550
Wire Wire Line
	1600 4550 1600 6600
Wire Wire Line
	1600 6600 2400 6600
Wire Wire Line
	2250 4650 1500 4650
Wire Wire Line
	1500 4650 1500 6700
Wire Wire Line
	1500 6700 2400 6700
Wire Wire Line
	1450 5150 3100 5150
Wire Wire Line
	2100 4750 2100 5250
Wire Wire Line
	2300 5150 2300 5250
Connection ~ 2100 5150
Wire Wire Line
	2500 5150 2500 5250
Connection ~ 2300 5150
Wire Wire Line
	2700 5150 2700 5250
Connection ~ 2500 5150
Wire Wire Line
	2900 5150 2900 5250
Connection ~ 2700 5150
Wire Wire Line
	3100 5150 3100 5250
Connection ~ 2900 5150
Wire Wire Line
	2100 5550 2100 5700
Wire Wire Line
	2100 5700 1500 5700
Connection ~ 1500 5700
Wire Wire Line
	2300 5550 2300 5750
Wire Wire Line
	2300 5750 1600 5750
Connection ~ 1600 5750
Wire Wire Line
	2500 5550 2500 5800
Wire Wire Line
	2500 5800 1700 5800
Connection ~ 1700 5800
Wire Wire Line
	2700 5550 2700 5850
Wire Wire Line
	2700 5850 1800 5850
Connection ~ 1800 5850
Wire Wire Line
	2900 5550 2900 5900
Wire Wire Line
	2900 5900 1900 5900
Connection ~ 1900 5900
Wire Wire Line
	3100 5550 3100 5950
Wire Wire Line
	3100 5950 2000 5950
Connection ~ 2000 5950
Wire Wire Line
	2400 6800 2400 7400
Connection ~ 2400 7400
Connection ~ 2400 6900
Wire Wire Line
	4000 6200 4050 6200
Wire Wire Line
	4050 6200 4050 3900
Wire Wire Line
	4050 3900 5100 3900
Wire Wire Line
	4000 6300 4250 6300
Wire Wire Line
	4250 6300 4250 4450
Wire Wire Line
	4250 4450 5100 4450
Wire Wire Line
	4000 6400 4450 6400
Wire Wire Line
	4450 6400 4450 5000
Wire Wire Line
	4450 5000 5100 5000
Wire Wire Line
	4000 6500 4650 6500
Wire Wire Line
	4650 6500 4650 5550
Wire Wire Line
	4650 5550 5100 5550
Wire Wire Line
	4000 6600 6500 6600
Wire Wire Line
	6500 6600 6500 3900
Wire Wire Line
	6500 3900 7200 3900
Wire Wire Line
	3750 5150 3750 4650
Wire Wire Line
	3750 4650 3050 4650
Wire Wire Line
	4000 6700 6600 6700
Wire Wire Line
	6600 6700 6600 4450
Wire Wire Line
	6600 4450 7200 4450
Wire Wire Line
	6700 5250 7200 5250
Connection ~ 6700 4700
Connection ~ 6800 4900
Wire Wire Line
	6000 5350 7200 5350
Wire Wire Line
	6000 5350 6000 5700
Wire Wire Line
	6000 5700 3550 5700
Wire Wire Line
	3550 5700 3550 4750
Wire Wire Line
	3550 4750 3050 4750
Wire Wire Line
	6400 3200 6400 3350
Wire Wire Line
	6400 3650 6400 5350
Connection ~ 6400 5350
Connection ~ 4600 3300
Wire Wire Line
	1350 4350 1300 4350
Wire Wire Line
	1450 4450 1300 4450
Connection ~ 4700 3100
Wire Wire Line
	4800 3800 4700 3800
Wire Wire Line
	5100 3800 5100 3800
Wire Wire Line
	5100 4350 5100 4350
Wire Wire Line
	4800 4350 4700 4350
Wire Wire Line
	4800 4900 4700 4900
Wire Wire Line
	5100 4900 5100 4900
Wire Wire Line
	4700 5450 4800 5450
Wire Wire Line
	5100 5450 5100 5450
Wire Wire Line
	6700 3600 7200 3600
Wire Wire Line
	6800 3800 6900 3800
Wire Wire Line
	6800 4350 6900 4350
Wire Wire Line
	6800 4900 6900 4900
Wire Wire Line
	6800 5450 6900 5450
Wire Wire Line
	7200 5450 7200 5450
Wire Wire Line
	7200 4900 7200 4900
Wire Wire Line
	7200 4350 7200 4350
Wire Wire Line
	7200 3800 7200 3800
Connection ~ 1450 5150
Connection ~ 1450 4450
Wire Wire Line
	3050 3550 3050 3550
Wire Wire Line
	3250 2500 3250 3550
Connection ~ 3250 3100
Wire Wire Line
	1350 3100 3550 3100
Wire Wire Line
	3750 3100 6800 3100
Connection ~ 1300 1950
Wire Wire Line
	3250 2500 3550 2500
Wire Wire Line
	3750 2500 4050 2500
Wire Wire Line
	4050 2500 4050 2600
Wire Wire Line
	4150 2400 4150 2600
Wire Wire Line
	3200 2400 3200 2350
Connection ~ 3200 2400
Wire Wire Line
	4200 1650 4250 1650
Wire Wire Line
	4250 1650 4250 2600
Wire Wire Line
	4350 2600 4350 1750
Wire Wire Line
	4350 1750 4200 1750
Wire Wire Line
	4450 2600 4450 1850
Wire Wire Line
	4450 1850 4200 1850
Wire Wire Line
	4550 2600 4550 1950
Wire Wire Line
	4550 1950 4200 1950
Wire Wire Line
	1550 2350 1550 2400
Connection ~ 1550 2400
Wire Wire Line
	1750 2400 1750 2350
Connection ~ 1750 2400
Wire Wire Line
	1950 2400 1950 2350
Connection ~ 1950 2400
Wire Wire Line
	2150 2400 2150 2350
Connection ~ 2150 2400
Wire Wire Line
	2350 2400 2350 2350
Connection ~ 2350 2400
Wire Wire Line
	2550 2400 2550 2350
Connection ~ 2550 2400
Wire Wire Line
	1550 2050 1550 1750
Connection ~ 1550 1750
Connection ~ 1750 1850
Wire Wire Line
	1950 2050 1950 1750
Connection ~ 1950 1750
Wire Wire Line
	2150 2050 2150 1650
Connection ~ 2150 1650
Wire Wire Line
	2350 2050 2350 1450
Connection ~ 2350 1450
Wire Wire Line
	2550 2050 2550 1250
Connection ~ 2550 1250
Text Notes 3800 3000 0    39   ~ 0
Getriebene AUX-Outs Reserven
Text Notes 7600 1150 0    39   ~ 0
230VAC\n- Staubsauger\n- Handkreissäge
Text Notes 3250 1000 0    39   ~ 0
Angeschlossen um\nInduktivitäten abzuleiten
Wire Wire Line
	1350 3100 1350 4350
NoConn ~ 3000 5800
NoConn ~ 4000 6800
NoConn ~ 4000 6900
$Comp
L CONN_01X02 P2
U 1 1 579DAA02
P 1100 2900
F 0 "P2" H 1100 3050 50  0000 C CNN
F 1 "CONN_RS232" V 1200 2900 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 1100 2900 50  0001 C CNN
F 3 "" H 1100 2900 50  0000 C CNN
	1    1100 2900
	-1   0    0    -1  
$EndComp
Text Notes 550  2950 0    39   ~ 0
RS232\nArduino
Wire Wire Line
	6350 1350 6450 1350
Wire Wire Line
	6350 2150 6550 2150
Wire Wire Line
	6650 2350 6350 2350
Wire Wire Line
	6750 1400 5550 1400
Wire Wire Line
	5550 1400 5550 1550
Wire Wire Line
	6750 2400 5550 2400
Wire Wire Line
	5550 2400 5550 2550
Wire Wire Line
	6350 2450 6850 2450
Wire Wire Line
	6350 2650 6950 2650
$Comp
L CONN_01X05 P10
U 1 1 579EF762
P 7400 1050
F 0 "P10" H 7400 1350 50  0000 C CNN
F 1 "CONN_01X05" V 7500 1050 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_PT-3.5mm_6pol" H 7400 1050 50  0001 C CNN
F 3 "" H 7400 1050 50  0000 C CNN
	1    7400 1050
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X06 P10.1
U 1 1 579EF7E9
P 7400 1700
F 0 "P10.1" H 7400 2050 50  0000 C CNN
F 1 "CONN_01X06" V 7500 1700 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_PT-3.5mm_6pol" H 7400 1700 50  0001 C CNN
F 3 "" H 7400 1700 50  0000 C CNN
	1    7400 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6750 1400 6750 1450
Wire Wire Line
	6750 1450 7200 1450
Wire Wire Line
	6350 1450 6450 1450
Wire Wire Line
	6450 1450 6450 1550
Wire Wire Line
	6450 1550 7200 1550
Wire Wire Line
	6350 1650 7200 1650
Wire Wire Line
	6750 2400 6750 1750
Wire Wire Line
	6750 1750 7200 1750
Wire Wire Line
	6850 2450 6850 1850
Wire Wire Line
	6850 1850 7200 1850
Wire Wire Line
	6950 2650 6950 1950
Wire Wire Line
	6950 1950 7200 1950
Text Notes 7600 1800 0    39   ~ 0
max. 24VDC\nPotentialfreie Kontakte\n- Staubsauger\n- Handkreissäge
Wire Wire Line
	5200 1050 5200 2250
Wire Wire Line
	5200 1050 7200 1050
Connection ~ 5200 1250
Wire Wire Line
	6650 850  6650 2350
Wire Wire Line
	6350 1250 7200 1250
Wire Wire Line
	6450 1350 6450 1150
Wire Wire Line
	6450 1150 7200 1150
Wire Wire Line
	6350 1150 6350 1250
Wire Wire Line
	6650 850  7200 850 
Wire Wire Line
	6550 2150 6550 950 
Wire Wire Line
	6550 950  7200 950 
Wire Wire Line
	2250 3650 2250 3400
Wire Wire Line
	2250 3400 3650 3400
Wire Wire Line
	3650 3400 3650 3700
Wire Wire Line
	2250 3750 2200 3750
Wire Wire Line
	2200 3750 2200 4900
Wire Wire Line
	2200 4900 3950 4900
Wire Wire Line
	3050 3850 3450 3850
Wire Wire Line
	3450 3850 3450 2950
Wire Wire Line
	3450 2950 1300 2950
Wire Wire Line
	3050 3950 3550 3950
Wire Wire Line
	3550 3950 3550 2850
Text Notes 550  3100 0    31   ~ 0
1 = TX (Arduino)\n2 = RX (Arduino)
$Comp
L R R30
U 1 1 57B84426
P 1700 2700
F 0 "R30" V 1780 2700 50  0000 C CNN
F 1 "R6k2" V 1700 2700 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 1630 2700 50  0001 C CNN
F 3 "" H 1700 2700 50  0000 C CNN
	1    1700 2700
	0    1    1    0   
$EndComp
$Comp
L R R31
U 1 1 57B84532
P 2150 2700
F 0 "R31" V 2230 2700 50  0000 C CNN
F 1 "R12k" V 2150 2700 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 2080 2700 50  0001 C CNN
F 3 "" H 2150 2700 50  0000 C CNN
	1    2150 2700
	0    1    1    0   
$EndComp
Wire Wire Line
	2400 3200 2400 2700
Wire Wire Line
	2400 2700 2300 2700
Connection ~ 2400 3200
Wire Wire Line
	1400 2700 1550 2700
Wire Wire Line
	1850 2700 2000 2700
Wire Wire Line
	1900 2700 1900 2850
Connection ~ 1900 2700
Wire Wire Line
	1900 2850 3550 2850
Wire Wire Line
	1300 2850 1400 2850
Wire Wire Line
	1400 2850 1400 2700
Wire Wire Line
	3350 4150 3050 4150
$Comp
L RASPBERRY_IO-RESCUE-RelaisAnbindung RPi1_P1
U 1 1 5799A363
P 2650 4150
F 0 "RPi1_P1" H 2650 4850 60  0000 C CNN
F 1 "RASPBERRY_IO" V 2650 4150 50  0000 C CNN
F 2 "Socket_Strips:Socket_Strip_Straight_2x13" H 2650 4150 60  0001 C CNN
F 3 "" H 2650 4150 60  0000 C CNN
	1    2650 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 4750 2100 4750
NoConn ~ 3050 3750
$Comp
L CONN_02X04 CONN_02X4
U 1 1 57BED64C
P 9400 3500
F 0 "CONN_02X4" H 9400 3750 50  0000 C CNN
F 1 "RPi2_P5" H 9400 3250 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x04" H 9400 2300 50  0001 C CNN
F 3 "" H 9400 2300 50  0000 C CNN
	1    9400 3500
	0    1    -1   0   
$EndComp
Wire Wire Line
	8050 5100 7150 5100
Wire Wire Line
	7150 5100 7150 5000
Wire Wire Line
	7150 5000 7200 5000
Wire Wire Line
	9450 3950 9450 3750
Wire Wire Line
	7200 5550 7150 5550
Wire Wire Line
	7150 5550 7150 5650
Wire Wire Line
	7150 5650 8150 5650
Wire Wire Line
	9450 3100 9450 3250
Connection ~ 6400 3200
$Comp
L R R35
U 1 1 57BF414A
P 8950 3500
F 0 "R35" V 9030 3500 50  0000 C CNN
F 1 "R10k" V 8950 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 8880 3500 50  0001 C CNN
F 3 "" H 8950 3500 50  0000 C CNN
	1    8950 3500
	1    0    0    -1  
$EndComp
$Comp
L R R34
U 1 1 57BF4264
P 8750 3500
F 0 "R34" V 8830 3500 50  0000 C CNN
F 1 "R10k" V 8750 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 8680 3500 50  0001 C CNN
F 3 "" H 8750 3500 50  0000 C CNN
	1    8750 3500
	1    0    0    -1  
$EndComp
$Comp
L R R33
U 1 1 57BF4397
P 8550 3500
F 0 "R33" V 8630 3500 50  0000 C CNN
F 1 "R10k" V 8550 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 8480 3500 50  0001 C CNN
F 3 "" H 8550 3500 50  0000 C CNN
	1    8550 3500
	1    0    0    -1  
$EndComp
$Comp
L R R32
U 1 1 57BF4461
P 8350 3500
F 0 "R32" V 8430 3500 50  0000 C CNN
F 1 "R10k" V 8350 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 8280 3500 50  0001 C CNN
F 3 "" H 8350 3500 50  0000 C CNN
	1    8350 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	8050 3950 9450 3950
Wire Wire Line
	8050 3950 8050 5100
Wire Wire Line
	8050 3750 9250 3750
Wire Wire Line
	8050 3750 8050 3200
Connection ~ 8050 3200
Wire Wire Line
	9250 1550 9250 3250
Wire Wire Line
	8150 3100 9450 3100
Wire Wire Line
	8150 5650 8150 3100
$Comp
L CONN_01X02 P17
U 1 1 57BFBD73
P 9550 2650
F 0 "P17" H 9550 2800 50  0000 C CNN
F 1 "CONN_01X02" V 9650 2650 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 9550 2650 50  0001 C CNN
F 3 "" H 9550 2650 50  0000 C CNN
	1    9550 2650
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X02 P16
U 1 1 57BFC25C
P 9550 2100
F 0 "P16" H 9550 2250 50  0000 C CNN
F 1 "CONN_01X02" V 9650 2100 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x02" H 9550 2100 50  0001 C CNN
F 3 "" H 9550 2100 50  0000 C CNN
	1    9550 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	9350 3850 9350 3750
Wire Wire Line
	8250 3850 9350 3850
Wire Wire Line
	8250 3850 8250 2150
Wire Wire Line
	8250 2150 9350 2150
Wire Wire Line
	9350 3250 9350 3000
Wire Wire Line
	9350 3000 8350 3000
Wire Wire Line
	8350 2700 8350 3350
Wire Wire Line
	8350 2700 9350 2700
Wire Wire Line
	8950 3950 8950 3650
Connection ~ 8950 3950
Wire Wire Line
	8550 3850 8550 3650
Connection ~ 8550 3850
Wire Wire Line
	8950 3350 8950 3200
Connection ~ 8950 3200
Wire Wire Line
	8750 3100 8750 3350
Connection ~ 8750 3100
Wire Wire Line
	8750 3650 8750 3750
Connection ~ 8750 3750
Wire Wire Line
	8550 3350 8550 3200
Connection ~ 8550 3200
Connection ~ 8350 3000
Wire Wire Line
	8350 3650 8350 3750
Connection ~ 8350 3750
NoConn ~ 3050 3650
NoConn ~ 2250 3950
NoConn ~ 2250 4350
NoConn ~ 3050 4450
Text Notes 9800 2150 0    39   ~ 0
Näherungssensor\n- Vorwärts
Text Notes 9800 2700 0    39   ~ 0
Näherungssensor\n- Rückwärts
$Comp
L CONN_01X02 P15
U 1 1 57C19E01
P 9550 1500
F 0 "P15" H 9550 1650 50  0000 C CNN
F 1 "CONN_01X02" V 9650 1500 50  0000 C CNN
F 2 "Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_2pol" H 9550 1500 50  0001 C CNN
F 3 "" H 9550 1500 50  0000 C CNN
	1    9550 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 3300 6700 3300
Wire Wire Line
	9350 1450 8900 1450
Wire Wire Line
	8900 1450 8900 2600
Wire Wire Line
	8900 2050 9350 2050
Wire Wire Line
	8900 2600 9350 2600
Connection ~ 8900 2050
Wire Wire Line
	9350 1550 9250 1550
Connection ~ 9250 3200
Text Notes 9800 1550 0    39   ~ 0
Netzteil Spannung\n- 3,3V\n- GND
Wire Wire Line
	1300 3750 1450 3750
Connection ~ 1450 3750
$EndSCHEMATC
