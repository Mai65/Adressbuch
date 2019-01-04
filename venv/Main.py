from __future__ import print_function
from tkinter import *
import tkinter as ttk
from tkinter import Tk
from typing import List
import os.path

import datetime
import mysql.connector


class Main:
    def __init__(self):
        # Fenster wird erzeugt
        main_win = Tk()
        main_win.title('Adressbuch')

        main_win.columnconfigure(0, weight=1)
        main_win.rowconfigure(0, weight=1)

        Menue(main_win)

        main_win.mainloop()


class Menue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Erstellen des MenueFrames
        menue_frame = ttk.Frame(borderwidth=2, width=200, height=150)

        # MenuFrame wird ausgerichtet und vergrößert sich automatisch
        menue_frame.grid_propagate(0)
        menue_frame.grid(sticky=(W + N + S + E))

        # Frame wird dynamisch
        menue_frame.columnconfigure(0, weight=1)
        menue_frame.rowconfigure(0, weight=1)
        menue_frame.rowconfigure(1, weight=1)
        menue_frame.rowconfigure(2, weight=1)
        menue_frame.rowconfigure(3, weight=1)

        # Erstellen der Buttons
        hinzufuegen_button = ttk.Button(menue_frame, text="Hinzufügen", command=lambda: Mask(parent), width=10)
        abrufen_button = ttk.Button(menue_frame, text="Abrufen", command=lambda: Mask(parent, False), width=10)

        # Erstellen des Labels
        adressbuch = Label(menue_frame, text="Adressbuch", font=("Helvetica", 16))

        # Buttons werden angeordnet
        adressbuch.grid(column=0, row=0)
        hinzufuegen_button.grid(column=0, row=1)
        abrufen_button.grid(column=0, row=2)


class Mask(ttk.Frame):

    def collect(self, number=False):
        """

        :type number: boolean
        """
        # Einsammeln der Einträge in ein dict wenn kein Wert vorhanden Wert = None
        if self.VornameEntry.get():
            self.dict['Vorname'] = self.VornameEntry.get()
        else:
            self.dict['Vorname'] = None
        if self.NachnameEntry.get():
            self.dict['Nachname'] = self.NachnameEntry.get()
        else:
            self.dict['Nachname'] = None
        if self.StraßeEntry.get():
            self.dict['Straße'] = self.StraßeEntry.get()
        else:
            self.dict['Straße'] = None
        if self.HausNrEntry.get():
            self.dict['HausNr'] = self.HausNrEntry.get()
        else:
            self.dict['HausNr'] = None
        if self.OrtEntry.get():
            self.dict['Ort'] = self.OrtEntry.get()
        else:
            self.dict['Ort'] = None
        if self.PLZEntry.get():
            self.dict['PLZ'] = self.PLZEntry.get()
        else:
            self.dict['PLZ'] = None
        if self.LandEntry.get():
            self.dict['Land'] = self.LandEntry.get()
        else:
            self.dict['Land'] = None
        if self.birthdateYearEntry.get():
            self.dict['birthdateYear'] = self.birthdateYearEntry.get()
        else:
            self.dict['birthdateYear'] = None
        if self.birthdateMonthEntry.get():
            self.dict['birthdateMonth'] = self.birthdateMonthEntry.get()
        else:
            self.dict['birthdateMonth'] = None
        if self.birthdateDayEntry.get():
            self.dict['birthdateDay'] = self.birthdateDayEntry.get()
        else:
            self.dict['birthdateDay'] = None

        # einsammmeln der Nummer nur wenn Nummer mit angegeben
        if number:
            if self.NummerEntry.get():
                self.dict['Nummer'] = self.NummerEntry.get()
        return self.dict

    def __init__(self, parent, number=False):
        self.dict = {}

        # erstellen des Frames
        super().__init__(parent)
        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0, sticky=(W + N + S + E))

        # erstellen und einfügen der Labels
        VornameLabel = ttk.Label(self, text="Vorname")
        NachnameLabel = ttk.Label(self, text="Nachname")
        StraßeLabel = ttk.Label(self, text="Straße")
        HausNrLabel = ttk.Label(self, text="Hausnummer")
        OrtLabel = ttk.Label(self, text="Ort")
        PLZLabel = ttk.Label(self, text="Postleitzahl")
        LandLabel = ttk.Label(self, text="Land")
        birthdateDayLabel = ttk.Label(self, text="Geburtstag")
        birthdateMonthLabel = ttk.Label(self, text="Geburtsmonat")
        birthdateYearLabel = ttk.Label(self, text="Geburtsjahr")
        abbrechenButton = ttk.Button(self, text="Abbrechen", command=self.destroy, width=10)

        VornameLabel.grid(column=0, row=1)
        NachnameLabel.grid(column=0, row=2)
        StraßeLabel.grid(column=0, row=3)
        HausNrLabel.grid(column=0, row=4)
        OrtLabel.grid(column=0, row=5)
        PLZLabel.grid(column=0, row=6)
        LandLabel.grid(column=0, row=7)
        birthdateDayLabel.grid(column=0, row=8)
        birthdateMonthLabel.grid(column=0, row=9)
        birthdateYearLabel.grid(column=0, row=10)

        # erstellen und einfügen der Entrys zu den jeweiligen Labels
        self.VornameEntry = ttk.Entry(self)
        self.NachnameEntry = ttk.Entry(self)
        self.StraßeEntry = ttk.Entry(self)
        self.HausNrEntry = ttk.Entry(self)
        self.OrtEntry = ttk.Entry(self)
        self.PLZEntry = ttk.Entry(self)
        self.LandEntry = ttk.Entry(self)
        self.birthdateYearEntry = ttk.Entry(self)
        self.birthdateMonthEntry = ttk.Entry(self)
        self.birthdateDayEntry = ttk.Entry(self)

        self.VornameEntry.grid(column=1, row=1)
        self.NachnameEntry.grid(column=1, row=2)
        self.StraßeEntry.grid(column=1, row=3)
        self.HausNrEntry.grid(column=1, row=4)
        self.OrtEntry.grid(column=1, row=5)
        self.PLZEntry.grid(column=1, row=6)
        self.LandEntry.grid(column=1, row=7)
        self.birthdateDayEntry.grid(column=1, row=8)
        self.birthdateMonthEntry.grid(column=1, row=9)
        self.birthdateYearEntry.grid(column=1, row=10)

        # Nummer wird nur auf anfrage beim Aufruf erstellt
        if number == True:
            NummerLabel = ttk.Label(self, text="Nummer")
            self.NummerEntry = ttk.Entry(self)
            self.NummerEntry.grid(column=1, row=11)
            ttk.Button(self, text='Ausführen', command=lambda: abfragen((self.collect(number))), width=10).grid(
                column=1, row=12)
            NummerLabel.grid(column=0, row=11)
            abbrechenButton.grid(column=0, row=12)
        else:
            ttk.Button(self, text='Ausführen', command=lambda: abfragen((self.collect(number))), width=10).grid(
                column=1, row=11)
            abbrechenButton.grid(column=0, row=11)


class abfragen():
    def __init__(self, dict):
        cnx = mysql.connector.connect(user='python', password='',
                                      host='127.0.0.1',
                                      database='adressbuch')

        cursor = cnx.cursor()
        add = (
            "INSERT INTO  `adressbuch` (`Vorname`, `Nachname`, `Straße`, `HausNr`, `Ort`, `PLZ`, `Land`, `birthdate`)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        if dict['birthdateMonth'] is not None:
            month = dict['birthdateMonth']
        else:
            month = None
        if dict['birthdateDay'] is not None:
            day = dict['birthdateDay']
        else:
            day = None
        if dict['birthdateYear'] is not None:
            year = dict['birthdateYear']
        else:
            year = None

        if month is not None and day is not None and year is not None:
            date = year + "-" + month + "-" + day
        elif month is not None and day is not None and year is None:
            date = '0000' + "-" + month + "-" + day
        elif month is not None and year is not None and day is None:
            date = year + "-" + month + "-" + '00'
        elif month is None and day is not None and year is not None:
            date = year + "-" + '00' + "-" + day
        elif month is not None:
            date = '0000' + "-" + month + "-" + '00'
        elif day is not None:
            date = '0000' + "-" + '00' + "-" + day
        elif year is not None:
            date = year + "-" + '00' + "-" + '00'
        else:
            date = None

        data = [(dict['Vorname'], dict['Nachname'], dict['Straße'], dict['HausNr'], dict['Ort'], dict['PLZ'],
                 dict['Land'], date)]
        cursor.executemany(add, data)

        cnx.commit()


        cnx.close()


Main()
