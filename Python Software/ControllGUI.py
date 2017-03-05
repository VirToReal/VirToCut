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
        import gi # Importiert die gobject-introspection«-Bibliotheken
except:
        print('kein "python-gobject" gefunden, bitte nachinstallieren! ')

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
from gi.repository.GdkPixbuf import Pixbuf
from Tools import *
from Dialogs import *
from GPIO import *
from SerialCommunication import *
from CommandsStack import *

gladefile = "ControllGUI_9.glade"
oksig = "ok" # Marlin gibt dies als Bestätigung von Kommandos aus
ps_off_sig = "M81" # G-Code zum Ausschalten der Spannungsversorgung
ps_timeout = 120000 # Zeit in ms bis das Netzteil sich Ausschalten soll
checksequencetime = 1000 # Zeit in ms auf die nach Änderungen am Programm geprüft werden soll

class Windows:
    def __init__(self):
        #Grundlegendes
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladefile)
        self.window = self.builder.get_object("window1") #Bedienoberfläche
        self.statusbar = self.builder.get_object("statusbar1") #Statusbar am Fuße der Bedienoberfläche
        self.infobardia = self.builder.get_object("infobarDia") #Infobar - InfobarDia selbst
        self.infobardia_image = self.builder.get_object("infobarDia_Image") #InfobarDia - Grafik
        self.infobardia_label = self.builder.get_object("infobarDia_Label") #InfobarDia - Label zur Darstellung von Meldetexten
        self.infobarinfo = self.builder.get_object("infobarInfo") #Infobar - InfobarInfo selbst
        self.infobarinfo_image = self.builder.get_object("infobarInfo_Image") #InfobarInfo - Grafik
        self.infobarinfo_label = self.builder.get_object("infobarInfo_Label") #InfobarInfo - Label zur Darstellung von Meldetexten
        self.infobar_tupel = (self.infobardia, self.infobardia_image , self.infobardia_label, self.infobarinfo, self.infobarinfo_image, self.infobarinfo_label)
        self.window.show()

        #Variablen
        self.connected = False # Variable dessen Zustand der der seriellen Verbindung ist
        self.timeoutcount = 0 # Variable die sich mit der timeout-Hauptschleife hochzählt

        #Verknüpfe Objekte der GUI mit Python
        #Bewegung
        self.bw_s = self.builder.get_object("BW_S") #Button - Bewegung/Schnitt
        self.bw_sk = self.builder.get_object("BW_SK") #Skale - Bewegung/Schrittweite
        self.bw_sk_v = self.builder.get_object("BW_SK_V") #Wert - Bewegung/Schrittweite
        self.bw_h = self.builder.get_object("BW_H") #Button - Bewegung/Home
        self.bw_gv = self.builder.get_object("BW_GV") #Button - Bewegung/Ganz Vor
        self.bw_v = self.builder.get_object("BW_V") #Button - Bewegung/Vor
        self.bw_z = self.builder.get_object("BW_Z") #Button - Bewegung/Zurück
        self.bw_gz = self.builder.get_object("BW_GZ") #Button - Bewegung/Ganz Zurück

        #Material
        self.ab_md = self.builder.get_object("AB_MD") #Spin-Button - Material/Benutzerdefinierte Anpresstiefe zur ComboboxText
        self.ab_mdl = self.builder.get_object("AB_MDL") #ComboboxText - Material/Anpresstiefe
        self.ab_ap = self.builder.get_object("AB_AP") #Button - Material/Anpressen
        self.ab_ah = self.builder.get_object("AB_AH") #Button - Material/Loslassen

        #Terminal
        self.serialscrolledwindow = self.builder.get_object("SerialScrolledWindow")
        self.serialsenden = self.builder.get_object("SerialSenden") #Button - Terminal/Text über serielle Schnittstelle senden
        self.serialtext = self.builder.get_object("SerialText") #Textfeld - Terminal/Text
        GObject.timeout_add(checksequencetime, self.timeout) # Hauptschleife ruft diese Funktion in den mit "checksequencetime" definierten Interval auf

        #Notebook - Schneidvorlage
        self.menu_sv_neu = self.builder.get_object("MENU_SV_Neu") # Menüitem Schneidvorlage/Neu
        self.menu_sv_on = self.builder.get_object("MENU_SV_On") # Menüitem Schneidvorlage/Öffnen
        self.menu_sv_sp = self.builder.get_object("MENU_SV_Sp") # Menüitem Schneidvorlage/Speichern
        self.menu_sv_spu = self.builder.get_object("MENU_SV_Spu") # Menüitem Schneidvorlage/Speichern unter
        self.schneidvorlage_label = self.builder.get_object("Schneidvorlage_Label") # Label - Schneidvorlage/Infotext für Schneidvorlage
        self.schneidvorlage = self.builder.get_object("Schneidvorlage") # TextView - Schneidvorlage/Textview für geladene Schneidvorlage
        self.schneidvorlagebuffer = self.builder.get_object("SchneidvorlageBuffer") # Textbuffer - Schneidvorlage/Textbuffer für Textview
        self.schneidvorlage_edit = self.builder.get_object("Schneidvorlage_Edit") # Button - Schneidvorlage/Schneidvorlage bearbeiten
        self.schneidvorlage_send = self.builder.get_object("Schneidvorlage_Send") # Button - Schneidvorlage/Schneidvorlage an Säge senden
        self.schneidvorlage_tuple = (self.schneidvorlage_label, self.schneidvorlage, self.schneidvorlagebuffer, self.menu_sv_neu, self.menu_sv_sp, self.menu_sv_spu, self.schneidvorlage_edit, self.schneidvorlage_send, Gtk.Image.new_from_icon_name("gtk-media-stop", Gtk.IconSize.BUTTON), Gtk.Image.new_from_icon_name("gtk-media-play", Gtk.IconSize.BUTTON))

        #Notebook - Debug
        self.debugscrolledwindow = self.builder.get_object("DebugScrolledWindow")

        #Notebook - Status
        self.if_st_pos_label_x = self.builder.get_object("IF_ST_POS_LABEL_X") #Label - Information/Status Position - Position der Säge
        self.if_st_pos_label_y = self.builder.get_object("IF_ST_POS_LABEL_Y") #Label - Information/Status Position - Position des Vorschubs
        self.if_st_pos_label_z = self.builder.get_object("IF_ST_POS_LABEL_Z") #Label - Information/Status Position - Position der Anpresshilfe
        self.if_st_pos_label_ya = self.builder.get_object("IF_ST_POS_LABEL_YA") #Label - Information/Status Position - Absolute Position des Vorschubs
        self.if_st_pos_tuple = (self.if_st_pos_label_x, self.if_st_pos_label_y, self.if_st_pos_label_z, self.if_st_pos_label_ya)

        self.if_st_fsrevealer1 = self.builder.get_object("IF_ST_FSRevealer1") #Revealer - Information/Status Fortschritt - Blendet Fortschrittsanzeige ein/aus
        self.if_st_fs_rowbar = self.builder.get_object("IF_ST_FS_RowBar") #LevelBar - Information/Status Fortschritt - Fortschrittsanzeige für abgearbeitete Zeilen G-Code
        self.if_st_fs_blockbar = self.builder.get_object("IF_ST_FS_BlockBar") #LevelBar - Information/Status Fortschritt - Fortschrittsanzeige für abgearbeitete G-Code Blöcke
        self.if_st_fsrevealer2 = self.builder.get_object("IF_ST_FSRevealer2") #Revealer - Information/Status Sägenposition überschreiben - Blendet Togglebutton samt Beschriftung ein/aus
        self.if_st_ms_overwrite = self.builder.get_object("IF_ST_MS_Overwrite") # Togglebutton - Information/Status Sägenposition überschreiben - Überschreibe max. Sägenposition auf momentane Sägenposition
        self.if_st_tuple = (self.if_st_fsrevealer1, self.if_st_fs_blockbar, self.if_st_fsrevealer2, self.if_st_ms_overwrite)

        #Notebook - Verbindung
        self.if_vb_status = self.builder.get_object("IF_VB_LABEL_STATUS")
        self.if_vb_info = self.builder.get_object("IF_VB_LABEL_INFO")
        self.if_vb_verb = self.builder.get_object("IF_VB_LABEL_VERB")
        self.if_vb_combo = self.builder.get_object("IF_VB_COMBO")
        self.if_vb_vb = self.builder.get_object("IF_VB_VB")
        self.if_vb_tr = self.builder.get_object("IF_VB_TR")
        self.if_vb_rs = self.builder.get_object("IF_VB_RS")

        #Verbinde Handler mit diesem Script
        self.builder.connect_signals(self)

        #Zu Testwecken auf True
        self._verbose = True

        #Generiere Programmverzeichnis für Daten
        self.tools = Tools(self.builder.get_object("DebugBuffer"),self.builder.get_object("TerminalBuffer"), self.if_st_pos_tuple, self.infobar_tupel)
        self.tools.crtdir(self._verbose, "")


        #Lade Einstellungen für Materialstärken und Port-Verbindungen
        self.load()

    def load(self): #Lade Konfigurationen aus Yaml-Datei
        try: # Lade Material,- und Portliste
            self.configdata = self.tools.yaml_load(self._verbose, ['Config'], 'Einstellungen')
            self.materiallist = self.configdata['VFM']['Vorhandene_Materialstaerken'] # Suche Liste für Materialstärken
            self.portlist = self.configdata['SVP']['Angelegte_Verbindungen'] # Suche Liste für serielle Verbindungen
            self.ab_mdl.remove_all() # Lösche alle Einträge aus Materialliste
            portselected = self.if_vb_combo.get_active_text() # Letzte Auswahl speichern
            self.if_vb_combo.remove_all() # Lösche alle Einträge aus Portliste
            portitems = 0
            for entry in self.materiallist: # Populiere Materialstärken ComboBox neu
                self.ab_mdl.append_text(entry[0])
            for entry in self.portlist: # Populiere Ports ComboBox neu
                self.if_vb_combo.append_text(entry[0])
                if portselected == entry[0]: # Wähle vorherige Auswahl wieder aus
                    self.if_vb_combo.set_active(portitems)
                if self.configdata['ST']['Automatisch_Verbinden'] and entry[4] and not self.connected: #Verbinde automatisch auf letzten aktiven Port wenn nötig und eingestellt
                    self.connect_port(True, entry[0])
                    #TODO Auswahl der Verbindung aus ComboboxText
                portitems += 1

        except Exception as errortext:
            self.tools.verbose(self._verbose, "Fehler beim laden der Konfigurationsdateien:\n" + str(errortext))
            self.materiallist = None
            self.portlist = None

        if self.connected: #Wenn serielle Verbindung besteht, auch GCodes aus Einstellungen laden
            self._commandsstack.load()

    def operability(self, state, excl_cut = False): # Bedienbarkeit aktivieren/deaktivieren
        self.menu_sv_neu.set_sensitive(state)
        self.menu_sv_on.set_sensitive(state)
        if not excl_cut: #Statusänderung des "Schnitt"-Buttons deaktivieren falls nötig
            self.bw_s.set_sensitive(state)
        self.bw_h.set_sensitive(state)
        self.bw_gv.set_sensitive(state)
        self.bw_v.set_sensitive(state)
        self.bw_z.set_sensitive(state)
        self.bw_gz.set_sensitive(state)
        self.ab_ap.set_sensitive(state)
        self.ab_ah.set_sensitive(state)
        self.serialsenden.set_sensitive(state)

    def connect_port(self, status, port=None): # Funktion zum Verbinden auf seriellen Port
        if self.portlist:
            if status:
                if port: # Wenn Port vorgegeben auf diesen Verbinden, ansonsten auf den von ComboboxText
                    self.selectedport = port
                else:
                    self.selectedport = self.if_vb_combo.get_active_text() # Text der Auswahl
                for i in self.portlist: # Suche Combobox-Auswahl in Einstellungen
                    if i[0] == self.selectedport:
                        self.if_vb_info.set_text("Baudrate: " + str(i[1]))
                        self._serialsession = SerialCommunication(self._verbose, self.tools, i[0], i[1], i[2], i[3], oksig, self.if_vb_status, self.if_vb_vb, self.if_vb_tr, self.if_vb_rs) #Baue Verbindung zu Arduino auf
                        try:
                            if self._serialsession.sc.isOpen(): # Wenn Verbindung besteht
                                self.gpioner = GPIOner(self._verbose, self.tools) #Initalisiere den GPIO auf dem Raspberry
                                self._commandsstack = CommandsStack(self._verbose, self.tools, self._serialsession, self.bw_sk_v, self.ab_mdl, self.if_st_pos_tuple, self.schneidvorlage_tuple, self.if_st_tuple, self.gpioner) #Bereite vordefinierte G-Code Arbeitsschritte
                                self.if_vb_verb.set_text("Verbunden auf Port") # Passe Überschrift von ComboboxText (Ports) an
                                self.operability(True) #Setzte alle Buttons die mit der seriellen Verbindung in "Verbindung" stehen auf Aktiv
                                self.dia_file = DIA_FILE(self.builder) #Erzeuge Datei-Dialog
                                self.connected = True # Setze Verbindungs-Variable auf True
                        except Exception as errortext:
                            self.if_vb_verb.set_text("Verbinden auf Port") # Passe Überschrift von ComboboxText (Ports) an
                            self.tools.verbose(self._verbose, 'Verbindungsversuch mit folgender Fehlermeldung abgebrochen:\n' + str(errortext))
                if not self.connected: #Fehlermeldung in Debugger/Infobar falls Verbindung misslang
                    self.tools.verbose(self._verbose, 'Konnte nicht auf die serielle Schnittstelle zugreifen', True)
            else:
                self._serialsession.terminate() # Schließe serielle Verbindung
                self.connected = False # Setze Verbindungs-Variable auf False
                self.operability(False)

    # Signale für das Hauptfenster
    def onDeleteWindow(self, object, data=None): # Signal "Fenster durch x geschlossen"
        self.tools.verbose(self._verbose, 'geschlossen mit x')
        self.close_application() # Ruft die Funktion zum Beenden des Programms auf

    def on_MENU_Quit_activate(self, object, data=None): # Signal Menüleiste/Beenden "Programm beenden" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Beenden "Programm beenden" gedrückt')
        self.close_application() # Ruft die Funktion zum Beenden des Programms auf

    def on_infobarDia_response(self, object, response_id): # Signal von der "InfobarDia" erhalten
        if response_id == -7: #'X' wurde gedrückt
            object.hide() #Blende InfobarDia aus
        elif response_id == 1: #'Apply' wurde gedrückt
            object.hide() #Blende InfobarDia aus
            if self.tools.wait_for_save: # Prüfe ob Dialog für das Überschreiben einer Datei erzeugt wurde
                self.tools.save_file(self._verbose, self.tools.wait_for_save[1], self.tools.wait_for_save[2], True) #Lasse Daten in Datei schreiben
            else: # Ansonsten muss Dialog zum überschreiben der maximalen Sägenposition sein
                self._commandsstack.toggle_ms(True, False)
        elif response_id == 2: #'Cancel' wurde gedrückt
            object.hide() #Blende InfobarDia aus

    def on_infobarInfo_response(self, object, response_id): # Signal von der "InfobarInfo" erhalten
        if response_id == -7: #X wurde gedrückt
            object.hide() #Blende InfobarInfo aus

    def on_BW_GV_clicked(self, object, data=None): # Signal Button/Begegung "Ganz Vor" gedrückt
        self.tools.verbose(self._verbose, 'Button/Bewegung: "Ganz Vor" gedrückt')
        self._commandsstack.BUTTON("SW", "GV")

    def on_BW_V_clicked(self, object, data=None): # Signal Button/Bewegung "Vor" gedrückt
        self.tools.verbose(self._verbose, 'Button/Bewegung: "Vor" gedrückt') 
        self._commandsstack.BUTTON("SW", "V")

    def on_BW_Z_clicked(self, object, data=None): # Signal Button/Bewegung "Zurück" gedrückt
        self.tools.verbose(self._verbose, 'Button/Bewegung: "Zurück" gedrückt')
        self._commandsstack.BUTTON("SW", "Z")

    def on_BW_GZ_clicked(self, object, data=None): # Signal Button/Bewegung "Ganz Zurück" gedrückt
        self.tools.verbose(self._verbose, 'Button/Bewegung: "Ganz Zurück" gedrückt')
        self._commandsstack.BUTTON("SW", "GZ")

    def on_BW_S_clicked(self, object, data=None): # Signal Button/Bewegung "Schnitt" gedrückt
        self.tools.verbose(self._verbose, 'Button/Bewegung: "Schnitt" gedrückt')
        self._commandsstack.BUTTON("SW", "S")

    def on_BW_H_clicked(self, object, data=None): # Signal Button/Bewegung "Home" gedrückt
        self.tools.verbose(self._verbose, 'Button/Bewegung: "Home" gedrückt')
        self._commandsstack.BUTTON("SW", "H")

    def on_BW_SK_clicked(self, object, data=None): # Signal Button/Scale "Schrittweite" gedrückt
        self.tools.verbose(self._verbose, 'Button/Scale "Schrittweite" gedrückt')

    def on_BW_SK_value_changed(self, object, data=None): # Signal Schieber/Scale "Schrittweite" verändert
        self.tools.verbose(self._verbose, 'Schieber/Scale "Schrittweite" auf Wert ' + str(self.bw_sk.get_value()) + ' verändert')
        self.bw_sk_v.set_text(str(self.bw_sk.get_value())) # Schreibe Schrittweite von Schieberegler in das Textfeld

    def on_BW_SK_V_changed(self, object, data=None): # Signal Eingabefeld/Scale "Schrittweite" verändert
        try:
            bw_sk_v_value = float(self.bw_sk_v.get_text())
            self.tools.verbose(self._verbose, 'Eingabefeld/Scale "Schrittweite" auf Wert ' + str(bw_sk_v_value) + ' verändert')
            self.bw_sk_v.set_progress_fraction(float(bw_sk_v_value)/100) # Zeige Schrittweite auch in Textfeld grafisch an
        except:
            self.tools.verbose(self._verbose, 'Eingabefeld/Scale "Schrittweite" enthielt kein Fließkomma-Zahl')
            self.bw_sk_v.set_text('')

    def on_AB_AP_clicked(self, object, data=None): # Signal Button/Anpressbügel "Anpressen" gedrückt
        self.tools.verbose(self._verbose, 'Button/Anpressbügel: "Anpressen" gedrückt')
        self._commandsstack.BUTTON("SW", "AP")

    def on_AB_AH_clicked(self, object, data=None): # Signal Button/Anpressbügel "Anheben" gedrückt
        self.tools.verbose(self._verbose, 'Button/Anpressbügel: "Anheben" gedrückt')
        self._commandsstack.BUTTON("SW", "AH")

    def on_AP_MD_value_changed(self, object, data=None): # Signal SpinButton/Anpressbügel "Materialstärke" geändert
        self.tools.verbose(self._verbose, 'SpinButton/Anpressbügel "Materialstärke" auf Wert ' + str(self.ab_md.get_value()) + ' geändert')

    def on_AP_MD_OK_clicked(self, object, data=None): # Signal SpinButton/Anpressbügel "Materialstärke" bestätigt
        self.tools.verbose(self._verbose, 'SpinButton/Anpressbügel "Materialstärke" bestätigt')
        self.ab_mdl.append(str(self.ab_md.get_value()), 'Benutzerdefiniert: ' + (str(self.ab_md.get_value())))
        self.ab_mdl.set_active(self.__materialitems) # Setze Benutzerdefinierte breite Aktiv
        self.__materialitems += 1

    def on_AP_MDL_changed(self, object, data=None): # Signal Combobox/Anpressbügel "Materialstärke" ausgewählt
        self.tools.verbose(self._verbose, 'Signal Combobox/Anpressbügel "Materialstärke" ausgewählt')
        #value = self.ab_mdl.get_value()
        #print (value)

    def on_IF_ST_MS_Overwrite_toggled(self, object, data=None): # Signal Togglebutton/max. Sägenposition "Überschreiben" gedrückt
        self.tools.verbose(self._verbose, 'Signal Togglebutton/max. Sägenposition "Überschreiben" gedrückt')
        self._commandsstack.toggle_ms() # Löse im CommandsStack die Funktion "toggle_ms" aus

    def on_IF_VB_VB_clicked(self, object, data=None): # Signal Button/Information/Verbindung/ "Verbinden" gedrückt
        self.tools.verbose(self._verbose, 'Signal Button/Information/Verbindung "Verbinden" gedrückt')
        self.connect_port(True)

    def on_IF_VB_TR_clicked(self, object, data=None): # Signal Button/Information/Verbindung/ "Trennen" gedrückt
        self.tools.verbose(self._verbose, 'Signal Button/Information/Verbindung "Trennen" gedrückt')
        self.connect_port(False)

    def on_IF_VB_RS_clicked(self, object, data=None): # Signal Button/Information/Verbindung/ "Reset" gedrückt
        self.tools.verbose(self._verbose, 'Signal Button/Information/Verbindung "Reset" gedrückt')
        self._serialsession.reset()

    def on_SerialText_activate(self, object, data=None): # Signal Enter gedrückt zum "Senden" des Textes
        self.tools.verbose(self._verbose, 'Enter gedrückt zum "Senden" des Textes')
        if self.serialsenden.get_sensitive():
            self._serialsession.sending(self.serialtext.get_text(), True)
            self.serialtext.set_text("")

    def on_SerialSenden_clicked(self, object, data=None): # Signal Button/Terminal "Senden" gedrückt
        self.tools.verbose(self._verbose, 'Signal Button/Terminal "Senden" gedrückt')
        self._serialsession.sending(self.serialtext.get_text(), True)
        self.serialtext.set_text("")

    def on_SerialLeeren_clicked(self, object, data=None): # Signal Button/Terminal "Leeren" gedrückt
        self.tools.terminal('Clear')
        self.tools.verbose(self._verbose, 'Signal Button/Terminal "Leeren" gedrückt')

    def on_Terminal_size_allocate(self, object, data=None): # Signal Terminal Textview-Göße hat sich geändert, scrolle nach unten
        adjust = self.serialscrolledwindow.get_vadjustment()
        adjust.set_value(adjust.get_upper() - adjust.get_page_size())

    def on_DebugLeeren_clicked(self, object, data=None): # Signal Button/Notebook/Debug "Leeren" gedrückt
        self.tools.verbose('Clear','')
        self.tools.verbose(self._verbose, 'Button/Notebook/Debug: "Leeren" gedrückt')

    def on_DebugON_toggled(self, object, data=None): # Signal CheckButton/Notebook/Debug "Eingeschaltet" gewechselt
        self.tools.verbose('Toggle','')
        self.tools.verbose(self._verbose, 'CheckButton/Notebook/Debug: "Eingeschaltet" gewechselt')

    def on_Debug_size_allocate(self, object, data=None): # Signal Debug Textview-Göße hat sich geändert, scrolle nach unten
        adjust = self.debugscrolledwindow.get_vadjustment()
        adjust.set_value(adjust.get_upper() - adjust.get_page_size())


    # Signale für die Schneidvorlage
    def on_MENU_SV_Neu_activate(self, object, data=None): # Signal Menüleiste/Neu "Schneidvorlage anlegen" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Neu "Schneidvorlage anlegen" gedrückt')
        self._commandsstack.cutting_template_new()

    def on_MENU_SV_On_activate(self, object, data=None): # Signal Menüleiste/Öffnen "Schneidvorlage öffnen" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Öffnen "Schneidvorlage öffnen" gedrückt')
        self.dia_file.action('OPEN', 'Datei mit Dateiendung .vtc')

    def on_MENU_SV_Sp_activate(self, object, data=None): # Signal Menüleiste/Speichern "Schneidvorlage speichern" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Speichern "Schneidvorlage speichern" gedrückt')
        self._commandsstack.cutting_template_save() # überschreibe Geöffnete Schneidvorlage

    def on_MENU_SV_Spu_activate(self, object, data=None): # Signal Menüleiste/Speichern unter "Schneidvorlage speichern unter" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Speichern unter " Schneidvorlage speichern unter" gedrückt')
        self.dia_file.action('SAVE', 'Wählen sie einen Ort/Dateinamen für die zu speichernde Schneidvorlage')

    def on_Schneidvorlage_Edit_clicked(self, object, data=None): # Signal Button/Schneidvorlage "Bearbeiten" gedrückt
        self.tools.verbose(self._verbose, 'Button/Schneidvorlage "Bearbeiten" gedrückt')
        self._commandsstack.cutting_template_edit() # Ermögliche es den Benutzer die Schneidvorlage zu bearbeiten

    def on_Schneidvorlage_Send_clicked(self, object, data=None): # Signal Button/Schneidvorlage "Schneidvorlage an Säge senden" gedrückt
        self.tools.verbose(self._verbose, 'Button/Schneidvorlage "Schneidvorlage an Säge senden" gedrückt')
        self.operability(False, True) #Alle "Maschinen"-Buttons deaktivieren bis auf den "Schneiden"-Button
        self._commandsstack.sequenced_sending(1) # Sende Schneidvorlage an die Maschine


    # Signal für den File_Open Dialog
    def on_DIA_FILE_delete_event(self, object, data=None): # Signal "FILE_OPEN-Dialog durch "X" geschlossen"
        self.tools.verbose(self._verbose, 'FILE_OPEN-Dialog durch "X" geschlossen')
        self.dia_file.hide()
        return True

    def on_DIA_FILE_response(self, object, response_id): # Signal "FILE-Dialog" Antwort erhalten
        if response_id == 1:
            self.tools.verbose(self._verbose, '"FILE-Dialog durch "Close" geschlossen')
            self.dia_file.hide()
        elif response_id == 2:
            self.tools.verbose(self._verbose, 'Datei mit "File-Dialog" ausgewählt')
            dia_type = self.dia_file.get_action() #Prüft in welchen Modus sich der "FILE-Dialog" befindet
            filename = self.dia_file.open_file() # Hole Dateinamen
            if dia_type == 'OPEN':
                self._commandsstack.cutting_template_load(filename) # Übergebe ausgewählte Datei der Schneidvorlagen-Auswertung
            elif dia_type == 'SAVE':
                self._commandsstack.cutting_template_save_as(filename) # Übergebe ausgewählte Datei der Schneidvorlagen-Auswertung
        return True


    # Signale für den Einstellungs-Dialog
    def on_MENU_Einstellungen_activate(self, object, data=None): # Signal Menüleiste/Edit "Einstellungen" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Edit "Einstellungen" gedrückt - Einstellungen geöffnet')
        self.dia_config = DIA_CONFIG(self._verbose, self.builder, self.tools) #TODO

    def on_DIA_CONFIG_delete_event(self, object, data=None): # Signal "Config-Dialog durch x geschlossen"
        self.tools.verbose(self._verbose, 'Config-Dialog durch x geschlossen')
        self.dia_config.hide()
        return True # Das ist wichtig, Blockiert den Handler vor einem nachträglichem "Destroy"

    def on_NB_VL_VFM_COMBO_changed(self, object, data=None): # Signal "Combobox/Config-Dialog/Notebook/Vorlagen/Vorlage für Materialstärken/Combobox - Material ausgewählt"
        self.tools.verbose(self._verbose, 'Combobox/Config-Dialog/Notebook/Vorlagen/Vorlage für Materialstärken/Combobox - Material ausgewählt')
        self.dia_config.show_material()

    def on_NB_VL_VFM_DEL_clicked(self, object, data=None): # Signal "Delete-Button/Config-Dialog/Notebook/Vorlagen/Vorlage für Materialstärken/Combobox "auswahl löschen" gedrückt"
        self.tools.verbose(self._verbose, 'Delete-Button/Config-Dialog/Notebook/Vorlagen/Vorlage für Materialstärken/Combobox "auswahl löschen" gedrückt')
        self.dia_config.del_material()

    def on_NB_VL_VFM_APPLY_clicked(self, object, data=None): # Signal "Apply-Button/Config-Dialog/Notebook/Vorlagen/Vorlage für Materialstärken/Button "Material hinzufügen" gedrückt"
        self.tools.verbose(self._verbose, 'Apply-Button/Config-Dialog/Notebook/Vorlagen/Vorlage für Materialstärken/Button "Material hinzufügen" gedrückt')
        self.dia_config.add_material()

    def on_NB_VL_SVP_COMBO_changed(self, object, data=None): # Signal "Combobox/Config-Dialog/Notebook/Vorlagen/Serielle Verbindungs-Ports/Combobox - Verbindung ausgewählt"
        self.tools.verbose(self._verbose, 'Combobox/Config-Dialog/Notebook/Vorlagen/Serielle Verbindungs-Ports/Combobox - Verbindung ausgewählt')
        self.dia_config.show_port()

    def on_NB_VL_SVP_DEL_clicked(self, object, data=None): # Signal "Combobox/Config-Dialog/Notebook/Vorlagen/Serielle Verbindungs-Ports/Combobox "auswahl löschen" gedrückt"
        self.tools.verbose(self._verbose, 'Combobox/Config-Dialog/Notebook/Vorlagen/Serielle Verbindungs-Ports/Combobox "auswahl löschen" gedrückt')
        self.dia_config.del_port()

    def on_NB_VL_SVP_APPLY_clicked(self, object, data=None): # Signal "Apply-Button/Config-Dialog/Notebook/Vorlagen/Serielle Verbindungs-Ports/Button "Port hinzufügen" gedrückt"
        self.tools.verbose(self._verbose, 'Apply-Button/Config-Dialog/Notebook/Vorlagen/Serielle Verbindungs-Ports/Button "Material hinzufügen" gedrückt')
        self.dia_config.add_port()

    def on_NB_GC_GKE_COMBO_changed(self, object, data=None): # Signal "Combobox/Config-Dialog/Notebook/G-Codes/G-Code Kommandos editieren/Combobox G-Code ausgewählt"
        self.tools.verbose(self._verbose, 'Combobox/Config-Dialog/Notebook/G-Codes/G-Code Kommandos editieren/Combobox G-Code ausgewählt')
        self.dia_config.edit_gcode()

    def on_NB_GC_GKE_RS_clicked(self, object, data=None): # Signal "Combobox/Config-Dialog/Notebook/G-Codes/G-Code Kommandos editieren/Importieren G-Code wiederherstellen"
        self.tools.verbose(self._verbose, 'Combobox/Config-Dialog/Notebook/G-Codes/G-Code Kommandos editieren/Importieren G-Code wiederherstellen')
        self.dia_config.reset_gcode()

    def on_BT_DIA_CONFIG_Ok_clicked(self, object, data=None): # Signal "Config-Dialog durch "OK" bestätigt"
        self.tools.verbose(self._verbose, 'Config-Dialog durch "OK" bestätigt')
        self.dia_config.write() # Lasse Config von Yaml in eine Datei schreiben
        self.dia_config.hide() # Schließe Dialog
        self.load() # Lade neue Einstellungen auch gleich in das Hauptfenster
        return True

    def on_BT_DIA_CONFIG_Refresh_clicked(self, object, data=None): # Signal "Config-Dialog - Anforderung "Einstellungen" durch "Refresh" neu abzurufen"
        self.tools.verbose(self._verbose, 'Config-Dialog - Anforderung "Einstellungen" durch "Refresh" neu abzurufen')
        #self.dia_config.refresh() #TODO

    def on_BT_DIA_CONFIG_Close_clicked(self, object, data=None): # Signal "Config-Dialog durch x geschlossen"
        self.tools.verbose(self._verbose, 'Config-Dialog durch "Abbrechen" geschlossen')
        self.dia_config.hide()
        return True


    # Signale für den About-Dialog
    def on_MENU_Ueber_activate(self, object, data=None): # Signal Menüleiste/Hilfe "About" gedrückt
        self.tools.verbose(self._verbose, 'Menüleiste/Hilfe "About" gedrückt - About geöffnet')
        self.dia_about = DIA_ABOUT(self.builder)

    def on_DIA_ABOUT_delete_event(self, object, data=None): # Signal "About-Dialog durch "X" geschlossen"
        self.tools.verbose(self._verbose, 'About-Dialog durch "X" geschlossen')
        self.dia_about.hide()
        return True

    def on_DIA_ABOUT_response(self, object, data=None): # Signal "About-Dialog durch "Close" geschlossen"
        self.tools.verbose(self._verbose, 'About-Dialog durch "Close" geschlossen')
        self.dia_about.hide()
        return True


    def timeout (self): # Operationen die in einem definierten Zeitintervall von der Hauptschleife (am Schluss) aufgerufen werden (Es kann je nach Auslastung dabei zu Verzögerungen kommen)
        try: # Versuche _serialsession (Serielle Sitzung) aufzufinden,

            if not self._serialsession.idlebuffer.empty(): # Wenn diese existiert und dessen Buffer Informationen enthält
                while True: # alle bisher enthaltenen Objekte abholen
                    if self._serialsession.idlebuffer.empty(): # damit aufhören wenn Buffer leergeräumt wurde
                        break
                    entry = self._serialsession.idlebuffer.get_nowait()
                    if entry[0]: # Wenn es sich um ein Antwort des Arduinos handelt, TextView Widget übergeben
                        self.tools.terminal(self._verbose, entry[1], entry[2]) # Stelle erhaltene Text-Lines im Terminal dar
                    else:
                        if entry[1] == 1: # Fehlercode "1" auswerten
                            self.tools.verbose(self._verbose, "Kann empfangene Textzeile nicht lesen, scheinbar ist der Bytestring verrutscht, Arduino Resetten!")
                        elif entry[1] == 2: # Fehlercode "2" auswerten
                            self.tools.verbose(self._verbose, "Der IdleBuffer ist jetzt vollgelaufen, Arduino spamt Nachrichten!")

            if not self._serialsession.responsebuffer.empty(): # Prüfe auch ob der Responsebuffer Information enthält
                while True: # alle bisher enthaltenen Objekte abholen
                    if self._serialsession.responsebuffer.empty(): # damit aufhören wenn Buffer leergeräumt wurde
                        break
                    entry = self._serialsession.responsebuffer.get_nowait()
                    if entry[0]: # Wenn es sich um Terminal-Kommunikation handelt, Text an Terminal übergeben
                            self.tools.terminal(self._verbose, entry[1], entry[2])
                    else:
                        if entry[1] == 1: # Fehlercode "1" auswerten
                            self.tools.verbose(self._verbose, "Senden einer G-Code Zeile fehlgeschlagen nach '" + str(self._serialsession.trys) + "' versuchen")
                        elif entry[1] == 2: # Fehlercode "2" auswerten
                            self.tools.verbose(self._verbose, "Keine Bestätigung erhalten, sende Zeile noch einmal...")
                        elif entry[1] == 3: # Fehlercode "3" auswerten
                            self.tools.verbose(self._verbose, "Kann erhaltene Textzeile vom seriellen Port nicht lesen")
                        elif entry[1] == 10: #Auswertung gesendete/erhaltene Zeilen
                            if self._commandsstack.svprogress: #Wenn Schneidvorlage abgearbeitet wird, Fortschritt aktualisieren
                                percentage = entry[3] / entry[2] #Wert für Fortschrittsanzeige 0-1
                                self.if_st_fs_rowbar.set_value(percentage) #Wert GtkLevelBar
                                if percentage == 1.0: #Wenn Schneidvorlage komplett übertragen und bestätigt wurde,
                                    self.operability(True) #"Maschinen"-Buttons reaktivieren
                                    transmission_status = self._commandsstack.get_transmission_status() #Hole momentane verfügbare und abgearbeitete G-Code Blöcke
                                    if transmission_status[0] == transmission_status[1]: #Prüfe ob alle G-Code Blöcke abgearbeitet wurden
                                        self._commandsstack.sequenced_sending(3) #Bestätigen das alle G-Code Blöcke abgearbeitet wurden
                                        self.if_st_fs_rowbar.set_value(0) #GtkLevelBar für G-Code Fortschritt wieder auf 0 setzen
                                    else: #Ansonsten nächsten G-Code Block abarbeiten
                                        self._commandsstack.sequenced_sending(2) #Bestätigen das ein G-Code Block abgearbeitet wurde

            if not self.gpioner.buttonbuffer.empty(): # Prüfe auch ob der ButtonBuffer der GPIO-Schnittstelle gedrückte Hardwaretasten beeinhaltet
                while True: # alle bisher enthaltenen Objekte abholen
                    if self.gpioner.buttonbuffer.empty(): # damit aufhören wenn Buffer leergeräumt wurde
                        break
                    entry = self.gpioner.buttonbuffer.get_nowait() # hole Tastendruck ohne abzuwarten
                    self._commandsstack.BUTTON("HW", entry[0], entry[1]) #Führe Hardware-Tastendruck in der CommandsStack-Klasse aus

            if self._serialsession.supply == True: # Spannungsversorgung nur versuchen Auszuschalten wenn auch Eingeschaltet
                if not self._commandsstack.svprogress: # Spannungsversorgung bei automatischen Abläufen nicht beeinflussen
                    self.timeoutcount += 1 # timeout-Hauptschleife hochzählen so lange Netzteil noch Eingeschalten sein soll
                if self.timeoutcount >= ps_timeout / checksequencetime: # Beim Erreichen des Intervals die Spannungsversorgung Ausschalten
                    self._serialsession.sending(ps_off_sig, False) # sende Kommando zum Ausschalten der Spannungsversorgung
                    self._serialsession.supply = False # Spannungsversorgung ist Ausgeschaltet
                    self.timeoutcount = 0 # timeout-Hauptschleife zurücksetzen

            print (str(self._serialsession.supply) + str(self.timeoutcount))

        except AttributeError: # Sollte noch keine serielle Verbindung bestehen, existieren die Objekte auch noch nicht
            pass

        #except Exception as errortext: # Läuft irgendetwas schief, Errortext in Debug-Log schreiben #TODO
            #self.tools.verbose(self._verbose, "Die Main-Loop Erweiterung in der Timout-Funktion berichtet folgenden Fehler:\n" + str(errortext))
            #pass
        return True # !!Sehr Wichtig!! Sonst wird diese Funktion nur 1x aufgerufen

    def close_application (self): # Beende das Programm ordnungsgemäß
        Gtk.main_quit()
        if self.connected: # Wenn serielle Verbindung besteht
            self._serialsession.startstopidle(False) # den Thread schließen, der auf dem Port lauscht
            if self.portlist:
                oldportlist = self.portlist
                self.portlist = []
                for i in oldportlist: # Vermerke letzten verbundenen Port als Favourit
                    if i[0] == self.selectedport:
                        self.portlist.append([i[0],i[1],i[2],i[3], True])
                    else:
                        self.portlist.append([i[0],i[1],i[2],i[3], False])
                self.configdata['SVP']['Angelegte_Verbindungen'] = self.portlist # Ports im Dictionary mit Favouritenbezeichnung überschreiben
                self.tools.yaml_dump(self._verbose, ['Config'], 'Einstellungen', self.configdata) # Schreibe Veränderungen von Einstellungen in die Yaml-Datei
            self.gpioner.terminate() # Trennt GPIO des Raspberrys zuverlässig

main = Windows()
Gtk.main()
