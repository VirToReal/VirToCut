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

from gi.repository import Gtk

class DIA_CONFIG: #Klasse für Konfigurations-Dialog

    def __init__(self, verbose, builder, tools):
        self.verbose = verbose
        self.builder = builder
        self.tools = tools
        self.settings = self.builder.get_object("DIA_CONFIG")
        self.settings.show()
        self.selectedgcode = False #Initalisiere Einstellungs-Dialog mit nicht ausgewählten G-Code Arbeitsschritt

        #Verknüpfe Objekte der GUI mit Python
        #Notebook-Tab: Vorlagen
        self.nb_vl_vfm_combo = self.builder.get_object("NB_VL_VFM_COMBO") #Combo-Box-Text - Notebook/Vorlagen/Vorlange für Materialstärken/Vorhandene Materialstärken
        self.nb_vl_vfm_comborevealer1 = self.builder.get_object("NB_VL_VFM_COMBORevealer1") # Revealer1 - Zeigt Eigenschaftstext der Combobox-Auswahl
        self.nb_vl_vfm_comborevealer2 = self.builder.get_object("NB_VL_VFM_COMBORevealer2") # Revealer2 - Zeigt Eigenschaften der Combobox-Auswahl
        self.nb_vl_vfm_descr = self.builder.get_object("NB_VL_VFM_DESCR") #Text-Entry - Notebook/Vorlagen/Vorlage für Materialstärken/Bezeichnung für Materialstärke
        self.nb_vl_vfm_thick = self.builder.get_object("NB_VL_VFM_THICK") #Spin-Button - Notebook/Vorlagen/Vorlage für Materialstärken/Wert für Materialstärke in mm
        self.nb_vl_vfm_label_thick = self.builder.get_object("NB_VL_VFM_LABEL_THICK") #Label - Notebook/Vorlagen/Vorlage für Materialstärken/Wert für Materialstärke in mm darstellen
        self.nb_vl_vfm_speed = self.builder.get_object("NB_VL_VFM_SPEED") #Spin-Button - Notebook/Vorlagen/Vorlage für Materialstärken/Schnittgeschwindigkeit für Materialstärke in mm/s
        self.nb_vl_vfm_label_speed = self.builder.get_object("NB_VL_VFM_LABEL_SPEED") #Label - Notebook/Vorlagen/Vorlage für Materialstärken/Schnittgeschwindigkeit für Materialstärke in mm/s darstellen

        self.nb_vl_spds_swc = self.builder.get_object("NB_VL_SPDS_SWC") #Spin-Button - Notebook/Vorlagen/Soft-Parametierung der Schneidwerkzeuge/Schrittweite Cursortasten
        self.nb_vl_spds_smb = self.builder.get_object("NB_VL_SPDS_SMB") #Spin-Button - Notebook/Vorlagen/Soft-Parametierung der Schneidwerkzeuge/Schrittweite Mausrad/Bild_Ab/Bild_Auf
        self.nb_vl_hpds_sdv = self.builder.get_object("NB_VL_HPDS_SDV") #Spin-Button - Notebook/Vorlagen/Hard-Parametierung der Schneidwerkzeuge/Schrittweite Drucktaste Vorschub
        self.nb_vl_hpds_bsdv = self.builder.get_object("NB_VL_HPDS_BSDV") #Spin-Button - Notebook/Vorlagen/Hard-Parametierung der Schneidwerkzeuge/Beschleunigung Schrittweite  Vorschub
        self.nb_vl_hpds_sds = self.builder.get_object("NB_VL_HPDS_SDS") #Spin-Button - Notebook/Vorlagen/Hard-Parametierung der Schneidwerkzeuge/Schrittweite Drucktaste Säge
        self.nb_vl_hpds_bsds = self.builder.get_object("NB_VL_HPDS_BSDS") #Spin-Button - Notebook/Vorlagen/Hard-Parametierung der Schneidwerkzeuge/Beschleunigung Schrittweite  Säge
        self.nb_vl_hpds_sbhs = self.builder.get_object("NB_VL_HPDS_SBHS") #Checkbox - Notebook/Vorlagen/Hard-Parametierung der Schneidwerkzeuge/Säge-Bestätigung über Hardware-Start anfordern

        self.nb_vl_svp_combo = self.builder.get_object("NB_VL_SVP_COMBO") #Combo-Box-Text - Notebook/Vorlagen/Neuen Port Anlagen/Angelegte Verbindungen
        self.nb_vl_svp_comborevealer1 = self.builder.get_object("NB_VL_SVP_COMBORevealer1") # Revealer1 - Zeigt Eigenschaftstext der Combobox-Auswahl
        self.nb_vl_svp_comborevealer2 = self.builder.get_object("NB_VL_SVP_COMBORevealer2") # Revealer2 - Zeigt Eigenschaften der Combobox-Auswahl
        self.nb_vl_svp_port = self.builder.get_object("NB_VL_SVP_PORT") #Text-Entry - Notebook/Vorlagen/Neuen Port Anlagen/Port
        self.nb_vl_svp_baud = self.builder.get_object("NB_VL_SVP_BAUD") #Text-Entry - Notebook/Vorlagen/Neuen Port Anlagen/Baudrate
        self.nb_vl_svp_label_baud = self.builder.get_object("NB_VL_SVP_LABEL_BAUD") #Label - Notebook/Vorlagen/Neuen Port Anlagen/Baudrate darstellen
        self.nb_vl_svp_timeout = self.builder.get_object("NB_VL_SVP_TIMEOUT") #Spin-Button - Notebook/Vorlagen/Neuen Port Anlagen/Zeitfenster zum verbinden in ms
        self.nb_vl_svp_label_timeout = self.builder.get_object("NB_VL_SVP_LABEL_TIMEOUT") #Label - Notebook/Vorlagen/Neuen Port Anlagen/Timeout darstellen
        self.nb_vl_svp_trys = self.builder.get_object("NB_VL_SVP_TRYS") #Spin-Button - Notebook/Vorlagen/Neuen Port Anlagen/Anzahl Sendeversuche nach Fehlschlag
        self.nb_vl_svp_label_trys = self.builder.get_object("NB_VL_SVP_LABEL_TRYS") #Label - Notebook/Vorlagen/Neuen Port Anlagen/Anzahl Sendeversuche darstellen

        self.nb_vl_st_bpav = self.builder.get_object("NB_VL_ST_BPAV") #Checkbox - Notebook/Vorlagen/Sonstiges/Bei Programmstart automatisch verbinden

        #Notebook-Tab: G-Codes
        self.nb_gc_gke_combo = self.builder.get_object("NB_GC_GKE_COMBO") #Combo-Box-Text - Notebook/G-Codes/G-Code Kommandos editieren/Zu editierendes Kommando
        self.gcodeeditbuffer = self.builder.get_object("GcodeEditBuffer") #TextViewBuffer - Notebook/G-Codes/G-Code Kommandos editieren/GcodeEditBuffer

        #Notebook-Tab: Parameter
        self.nb_pm_pds_sb = self.builder.get_object("NB_PM_PDS_SB") #Spin-Button - Notebook/Parameter/Parametrieren der Säge/Schnittbreite
        self.nb_pm_pds_nzsa = self.builder.get_object("NB_PM_PDS_NZSA") #Spin-Button - Notebook/Parameter/Parametrieren der Säge/Nachlaufzeit Säge
        self.nb_pm_pds_nzst = self.builder.get_object("NB_PM_PDS_NZST") #Spin-Button - Notebook/Parameter/Parametrieren der Säge/Nachlaufzeit Staubsauger
        self.nb_pm_pds_fs = self.builder.get_object("NB_PM_PDS_FS") #Spin-Button - Notebook/Parameter/Parametrieren der Säge/Fahrbare Strecke
        self.nb_pm_pds_asm = self.builder.get_object("NB_PM_PDS_ASM") #Spin-Button - Notebook/Parameter/Parametrieren der Säge/Abstand Sägeblatt zum Materialanschlag

        self.nb_pm_pdv_bv = self.builder.get_object("NB_PM_PDV_BV") #Spin-Button - Notebook/Parameter/Parametrieren des Vorschubs/Be,-Endschleunigung des Vorschub-Anschlags
        self.nb_pm_pdv_fs = self.builder.get_object("NB_PM_PDV_FS") #Spin-Button - Notebook/Parameter/Parametrieren des Vorschubs/Fahrbare Strecke
        self.nb_pm_pdv_us = self.builder.get_object("NB_PM_PDV_US") #Spin-Button - Notebook/Parameter/Parametrieren des Vorschubs/Umkehrspiel Vorschub

        self.nb_pm_pda_aba = self.builder.get_object("NB_PM_PDA_ABA") #Spin-Button - Notebook/Parameter/Parametrieren des Anpressbügels/Anpressentschleunigung des Anpressbügels
        self.nb_pm_pda_fs = self.builder.get_object("NB_PM_PDA_FS") #Spin-Button - Notebook/Parameter/Parametrieren des Anpressbügels/Fahrbare Strecke
        self.nb_pm_pda_us = self.builder.get_object("NB_PM_PDA_US") #Spin-Button - Notebook/Parameter/Parametrieren des Anpressbügels/Umkehrspiel Anpressbügel

        self.nb_pm_zds_smb = self.builder.get_object("NB_PM_ZDS_SMB") #Spin-Button - Notebook/Parameter/Zwischen den Schnitten/Zeit zwischen den Schnitten
        self.nb_pm_zds_saa = self.builder.get_object("NB_PM_ZDS_SAA") #Checkbox - Notebook/Parameter/Zwischen den Schnitten/Sägen zwischen den Schnitten abschalten
        self.nb_pm_zds_sta = self.builder.get_object("NB_PM_ZDS_STA") #Checkbox - Notebook/Parameter/Zwischen den Schnitten/Staubsauger zwischen den Schnitten abschalten

        #Lese Einstellungen aus Datei aus
        self.load()

    def hide(self): # Schließe Dialog
        self.settings.hide() # Verstecke Fenster
        self.nb_vl_vfm_combo.remove_all() # Lösche Materialstärken aus Combo-Box
        self.nb_vl_vfm_comborevealer1.set_reveal_child(False) # Lasse Combo-Box Auswahl "Eigenschaftstext" verschwinden
        self.nb_vl_vfm_comborevealer2.set_reveal_child(False) # Lasse Combo-Box Auswahl "Materialeigenschaftstext" verschwinden
        self.nb_vl_svp_combo.remove_all() # Lösche Serielle Verbindungs-Ports aus Combo-Box
        self.nb_vl_svp_comborevealer1.set_reveal_child(False) # Lasse Combo-Box Auswahl "Eigenschaftstext" verschwinden
        self.nb_vl_svp_comborevealer2.set_reveal_child(False) # Lasse Combo-Box Auswahl "Porteigenschaftstext" verschwinden

        self.gcodeeditbuffer.set_text("") # Lösche letzte Eingabe aus Gcode-TextBuffer
        if self.selectedgcode:
            self.nb_gc_gke_combo.prepend_text("... auswählen") # Füge Standardauswahl der GCode Auswahl wieder in ComboboxText an, wenn gelöscht
            self.nb_gc_gke_combo.set_active(0) # Diese dann auch auswählen

    def load(self): # Lade Einstellungen aus .yaml Datei
        try: # Einstellungen
            self.configdata = self.tools.yaml_load(self.verbose, ['Config'], 'Einstellungen')
            self.materiallist = self.configdata['VFM']['Vorhandene_Materialstaerken'] # Suche Liste für Materialstärken
            self.portlist = self.configdata['SVP']['Angelegte_Verbindungen'] # Suche Liste für serielle Verbindungen

            # Schreibe gespeicherte Einstellungen in die Eingabefelder zurück
            self.nb_vl_spds_swc.set_value(self.configdata['SPDS']['Schrittweite_Cursortasten'])
            self.nb_vl_spds_smb.set_value(self.configdata['SPDS']['Schrittweite_Maus_Bild'])
            self.nb_vl_hpds_sdv.set_value(self.configdata['HPDS']['Schrittweite_Vorschub'])
            self.nb_vl_hpds_bsdv.set_value(self.configdata['HPDS']['Beschl_Schrittweite_Vorschub'])
            self.nb_vl_hpds_sds.set_value(self.configdata['HPDS']['Schrittweite_Saege'])
            self.nb_vl_hpds_bsds.set_value(self.configdata['HPDS']['Beschl_Schrittweite_Saege'])
            self.nb_vl_hpds_sbhs.set_active(self.configdata['HPDS']['Start_anfordern'])
            self.nb_vl_st_bpav.set_active(self.configdata['ST']['Automatisch_Verbinden'])

            self.nb_pm_pds_sb.set_value(self.configdata['PDS']['Schnittbreite'])
            self.nb_pm_pds_nzsa.set_value(self.configdata['PDS']['Nachlaufzeit_Saege'])
            self.nb_pm_pds_nzst.set_value(self.configdata['PDS']['Nachlaufzeit_Staubsauger'])
            self.nb_pm_pds_fs.set_value(self.configdata['PDS']['Fahrbare_Strecke'])
            self.nb_pm_pds_asm.set_value(self.configdata['PDS']['Abstand_Saegeblatt_zum_Materialanschlag'])

            self.nb_pm_pdv_bv.set_value(self.configdata['PDV']['Be_End-Schleunigung_Vorschub'])
            self.nb_pm_pdv_fs.set_value(self.configdata['PDV']['Fahrbare_Strecke'])
            self.nb_pm_pdv_us.set_value(self.configdata['PDV']['Umkehrspiel_Vorschub'])

            self.nb_pm_pda_aba.set_value(self.configdata['PDA']['Anpressentschleunigung_Anpressbuegel'])
            self.nb_pm_pda_fs.set_value(self.configdata['PDA']['Fahrbare_Strecke'])
            self.nb_pm_pda_us.set_value(self.configdata['PDA']['Umkehrspiel_Anpressbuegel'])

            self.nb_pm_zds_smb.set_active(self.configdata['ZDS']['Schnitte_manuell_bestaetigen'])
            self.nb_pm_zds_saa.set_active(self.configdata['ZDS']['Saege_dazwischen_abschalten'])
            self.nb_pm_zds_sta.set_active(self.configdata['ZDS']['Staubsauger_dazwischen_abschalten'])

        except:
            self.tools.verbose(self.verbose, "Konnte Einstellungs-Datei nicht laden, evtl exisitiert diese noch nicht")

        try: # Materialstärken
            for entry in self.materiallist: # Populiere ComboBox
                self.nb_vl_vfm_combo.append_text(entry[0])
        except:
            self.tools.verbose(self.verbose, "Noch keine Materialstärken eingetragen")
            self.materiallist = [] # Wenn keine Einträge oder in der .yaml Datei oder sie existiert nicht - leere Liste erzeugen

        try: # Angelegte Verbindungen
            for entry in self.portlist: # Populiere ComboBox
                self.nb_vl_svp_combo.append_text(entry[0])
        except:
            self.tools.verbose(self.verbose, "Noch keine Verbindungs-Ports eingetragen")
            self.portlist = [] # Wenn keine Einträge oder in der .yaml Datei oder sie existiert nicht - leere Liste erzeugen

        try: # G-Codes
            self.gcodedata = self.tools.yaml_load(self.verbose, ['Config'], 'GCode')
        except:
            self.tools.verbose(self.verbose, "Konnte GCode-Datei nicht laden, evtl exisitiert diese noch nicht")
            self.gcodedata = { 'HOME' : '', 'VORHERIG' : '', 'NACHFOLGEND' : '', 'ANPRESSEN' : '', 'SCHNEIDEN' : '', 'VORSCHUB' : '', 'RUECKFAHRT' : '', 'FREIGEBEN' : ''} # Erzeuge leeres Dictionary wenn keine anderen Vorlagen vorhanden


    def write(self): #Speichere Einstellungen in .yaml Datei
        configdata = {
            'VFM': {
                        'Vorhandene_Materialstaerken' : self.materiallist},
            'SPDS' : {
                        'Schrittweite_Cursortasten': self.nb_vl_spds_swc.get_value(),
                        'Schrittweite_Maus_Bild': self.nb_vl_spds_smb.get_value()},
            'HPDS' : {
                        'Schrittweite_Vorschub' : self.nb_vl_hpds_sdv.get_value(),
                        'Beschl_Schrittweite_Vorschub' : self.nb_vl_hpds_bsdv.get_value(),
                        'Schrittweite_Saege' : self.nb_vl_hpds_sds.get_value(), 
                        'Beschl_Schrittweite_Saege' : self.nb_vl_hpds_bsds.get_value(),
                        'Start_anfordern' : self.nb_vl_hpds_sbhs.get_active()},
            'SVP' : {
                        'Angelegte_Verbindungen' : self.portlist},
            'ST' : {
                        'Automatisch_Verbinden' : self.nb_vl_st_bpav.get_active()},
            'PDS' : {
                        'Schnittbreite' : self.nb_pm_pds_sb.get_value(),
                        'Nachlaufzeit_Saege' : self.nb_pm_pds_nzsa.get_value(),
                        'Nachlaufzeit_Staubsauger' : self.nb_pm_pds_nzst.get_value(),
                        'Fahrbare_Strecke' : self.nb_pm_pds_fs.get_value(),
                        'Abstand_Saegeblatt_zum_Materialanschlag' : self.nb_pm_pds_asm.get_value()},
            'PDV' : {
                        'Be_End-Schleunigung_Vorschub' : self.nb_pm_pdv_bv.get_value(),
                        'Fahrbare_Strecke' : self.nb_pm_pdv_fs.get_value(),
                        'Umkehrspiel_Vorschub' : self.nb_pm_pdv_us.get_value()},
            'PDA' : {
                        'Anpressentschleunigung_Anpressbuegel' : self.nb_pm_pda_aba.get_value(),
                        'Fahrbare_Strecke' : self.nb_pm_pda_fs.get_value(),
                        'Umkehrspiel_Anpressbuegel' : self.nb_pm_pda_us.get_value()},
            'ZDS' : {
                        'Schnitte_manuell_bestaetigen' : self.nb_pm_zds_smb.get_active(),
                        'Saege_dazwischen_abschalten' : self.nb_pm_zds_saa.get_active(),
                        'Staubsauger_dazwischen_abschalten' : self.nb_pm_zds_sta.get_active()}}

        if self.selectedgcode: #Auch letzte G-Code Änderung beim Bestätigen berücksichtigen
            self.gcodedata[self.selectedgcode] = self.gcodeeditbuffer.get_text(Gtk.TextBuffer.get_start_iter(self.gcodeeditbuffer), Gtk.TextBuffer.get_end_iter(self.gcodeeditbuffer), False)

        if self.tools.crtdir(self.verbose, ['Config']): # Erzeuge Ordner für Einstellungen wenn noch nicht geschehen
            self.tools.crtdir(self.verbose, ['Config', 'Voreinstellung']) # Erzeuge Ordner für Standard Einstellungen
            self.tools.yaml_dump(self.verbose, ['Config', 'Voreinstellung'], 'Voreinstellungen', configdata) #Schreibe diese in erzeugten Ordner

        self.tools.yaml_dump(self.verbose, ['Config'], 'Einstellungen', configdata) # Schreibe Veränderungen von Einstellungen in eine Yaml-Datei
        self.tools.yaml_dump(self.verbose, ['Config'], 'GCode', self.gcodedata) # Schreibe Veränderungen von Gcode in eine Yaml-Datei

    def show_material(self): # Zeige die Eigenschaften der ausgewählten Materialstärke an
        self.nb_vl_vfm_comborevealer1.set_reveal_child(True) # Zeige Beschreibungstext
        self.nb_vl_vfm_comborevealer2.set_reveal_child(True) # Zeige Materialeigenschaftstext
        selected = self.nb_vl_vfm_combo.get_active_text() # Text der Auswahl
        for i in self.materiallist: # Suche in Materialliste die Eigenschaften der Combobox-Auswahl
            if i[0] == selected:
                self.nb_vl_vfm_label_thick.set_text(str(i[1])) # Materialdicke darstellen
                self.nb_vl_vfm_label_speed.set_text(str(i[2])) # Materialschneidgeschwindigkeit darstellen

    def add_material(self): # Füge Auswahl in Notebook/Vorlagen/Vorlage für Materialstärken/Combobox hinzu
        descr = self.nb_vl_vfm_descr.get_text()
        self.nb_vl_vfm_descr.set_text('') # Leere Eingabefeld
        thick = self.nb_vl_vfm_thick.get_value()
        self.nb_vl_vfm_thick.set_value(0) # Leere Spin-Button
        speed = self.nb_vl_vfm_speed.get_value()
        self.nb_vl_vfm_speed.set_value(0) # Leere Spin-Button

        self.nb_vl_vfm_combo.append_text(descr) # Füge Eingabe der Combobox hinzu
        self.materiallist.append([descr, thick, speed]) # Füge Eintrag der Liste hinzu

    def del_material(self): # Lösche Auswahl in Notebook/Vorlagen/Vorlage für Materialstärken/Combobox
        selected = self.nb_vl_vfm_combo.get_active_text() # Text der Auswahl
        oldmateriallist = self.materiallist
        self.materiallist = []
        count = 0
        for i in oldmateriallist: # Erzeuge neue Liste ohne dem gelöschten Eintrag
            if i[0] != selected:
                self.materiallist.append(i)
                count += 1
            else:
                self.nb_vl_vfm_combo.remove(count) # Lösche Eintrag aus Combo-Box
                self.nb_vl_vfm_comborevealer1.set_reveal_child(False) # Lasse Eigenschaftstext verschwinden
                self.nb_vl_vfm_comborevealer2.set_reveal_child(False) # Lasse Materialeigenschaftstext verschwinden

    def show_port(self): # Zeige die Eigenschaften des ausgewählten Ports an
        self.nb_vl_svp_comborevealer1.set_reveal_child(True) # Zeige Beschreibungstext
        self.nb_vl_svp_comborevealer2.set_reveal_child(True) # Zeige Porteigenschaftstext
        selected = self.nb_vl_svp_combo.get_active_text() # Text der Auswahl
        for i in self.portlist: # Suche in Portliste die Eigenschaften der Combobox-Auswahl
            if i[0] == selected:
                self.nb_vl_svp_label_baud.set_text(str(i[1])) # Baudrate darstellen
                self.nb_vl_svp_label_timeout.set_text(str(i[2])) # Timeout darstellen
                self.nb_vl_svp_label_trys.set_text(str(i[3])) # Sendeversuche darstellen

    def add_port(self): #Füge Auswahl in Notebook/Vorlagen/Verbindungs-Ports für die serielle Kommunikation/Combobox hinzu
        pfad = self.nb_vl_svp_port.get_text()
        self.nb_vl_svp_port.set_text('') # Leere Eingabefeld
        baud = int(self.nb_vl_svp_baud.get_active_text())
        self.nb_vl_svp_baud.set_active(2) # Leere Spin-Button
        timeout = int(self.nb_vl_svp_timeout.get_value())
        self.nb_vl_svp_timeout.set_value(0) # Leere Spin-Button
        trys = int(self.nb_vl_svp_trys.get_value())
        self.nb_vl_svp_trys.set_value(0) # Leere Spin-Button

        self.nb_vl_svp_combo.append_text(pfad) # Füge Eingabe der Combobox hinzu
        self.portlist.append([pfad, baud, timeout, trys, False]) # Füge Eintrag der Liste hinzu + Favouritbemerkung mit Standardauswahl: False

    def del_port(self): # Lösche Auswahl in Notebook/Vorlagen/Verbindungs-Ports für die serielle Kommunikation/Combobox
        selected = self.nb_vl_svp_combo.get_active_text() # Text der Auswahl
        oldportlist = self.portlist
        self.portlist = []
        count = 0
        for i in oldportlist: # Erzeuge neue Liste ohne dem gelöschten Eintrag
            if i[0] != selected:
                self.portlist.append(i)
                count += 1
            else:
                self.nb_vl_svp_combo.remove(count) # Lösche Eintrag aus Combo-Box
                self.nb_vl_svp_comborevealer1.set_reveal_child(False) # Lasse Eigenschaftstext verschwinden
                self.nb_vl_svp_comborevealer2.set_reveal_child(False) # Lasse Porteigenschaftstext verschwinden

    def edit_gcode(self): # Stelle je nach Combo-Box auswahl G-Code aus Yaml-Datei dar
        selected = self.nb_gc_gke_combo.get_active_text() # Text der Auswahl
        text = self.gcodeeditbuffer.get_text(Gtk.TextBuffer.get_start_iter(self.gcodeeditbuffer), Gtk.TextBuffer.get_end_iter(self.gcodeeditbuffer), False) # Text im Buffer
        if self.selectedgcode: #Eingegebenen Text in ausgewählte G-Code Auswahl einfügen
            self.gcodedata[self.selectedgcode] = text
        else:
            self.nb_gc_gke_combo.remove(0) #Lösche "... auswählen" Eintrag aus ComboBox nach einer Auswahl

        if selected == 'Home': # Lese je nach Auswahl den Text der Variable in den TextBuffer
            self.gcodeeditbuffer.set_text(self.gcodedata['HOME'], -1)
            self.selectedgcode = 'HOME'
        elif selected == 'Kommandos vor Programmablauf':
            self.gcodeeditbuffer.set_text(self.gcodedata['VORHERIG'], -1)
            self.selectedgcode = 'VORHERIG'
        elif selected == 'Kommandos nach Programmablauf':
            self.gcodeeditbuffer.set_text(self.gcodedata['NACHFOLGEND'], -1)
            self.selectedgcode = 'NACHFOLGEND'
        elif selected == 'Anpressen':
            self.gcodeeditbuffer.set_text(self.gcodedata['ANPRESSEN'], -1)
            self.selectedgcode = 'ANPRESSEN'
        elif selected == 'Schneiden':
            self.gcodeeditbuffer.set_text(self.gcodedata['SCHNEIDEN'], -1)
            self.selectedgcode = 'SCHNEIDEN'
        elif selected == 'Vorschub':
            self.gcodeeditbuffer.set_text(self.gcodedata['VORSCHUB'], -1)
            self.selectedgcode = 'VORSCHUB'
        elif selected == 'Rückfahrt':
            self.gcodeeditbuffer.set_text(self.gcodedata['RUECKFAHRT'], -1)
            self.selectedgcode = 'RUECKFAHRT'
        elif selected == 'Freigeben':
            self.gcodeeditbuffer.set_text(self.gcodedata['FREIGEBEN'], -1)
            self.selectedgcode = 'FREIGEBEN'


    def reset_gcode(self): # Stelle ursprünglich gespeicherten G-Code wieder her (falls G-Code importiert wurde)
        print ("Not done Yet") #TODO


class DIA_ABOUT: #Klasse für Über-Dialog

    def __init__(self, builder):
        self.builder = builder
        self.about = self.builder.get_object("DIA_ABOUT")
        self.about.show()

    def hide(self):
        self.about.hide() # Verstecke Dialog (durch schließen)


class DIA_FILE: #Klasse für das Auswählen/Abspeichern einer Datei

    def __init__(self, builder):
        self.builder = builder
        self.dia_file = self.builder.get_object("DIA_FILE")
        self.dia_file_label = self.builder.get_object("DIA_FILE_Label")

        self.dia_action = None #Initalisiere Grundzustand

    def action(self, dia_type, message): #Stellt Dialog als 'Datei öffnen/Datei speichern' dar
        if dia_type == 'OPEN':
            self.dia_file.set_action(Gtk.FileChooserAction.OPEN) #Dialog in "Datei öffnen" umwandeln
            self.dia_action = dia_type
        elif dia_type == 'SAVE':
            self.dia_file.set_action(Gtk.FileChooserAction.SAVE) #Dialog in "Datei speichern" umwandeln
            self.dia_file.set_create_folders(True) #Ermöglicht es den Anwender Ordner zu erstellen
            self.dia_action = dia_type
        self.dia_file.show()

        self.dia_file_label = self.builder.get_object("DIA_FILE_Label")
        self.dia_file_label.set_text(message)

    def get_action(self):
        return self.dia_action

    def hide(self):
        self.dia_file.hide() # Verstecke Dialog (durch schließen)

    def open_file(self):
        self.hide()
        return self.dia_file.get_filename()

