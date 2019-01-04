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
        hinzufuegen_button = ttk.Button(menue_frame, text="Hinzufügen", command=lambda: hinzufügen(parent), width=10)
        abrufen_button = ttk.Button(menue_frame, text="Abrufen", command=lambda: abfragen(parent), width=10)

        # Erstellen des Labels
        adressbuch = Label(menue_frame, text="Adressbuch", font=("Helvetica", 16))

        # Buttons werden angeordnet
        adressbuch.grid(column=0, row=0)
        hinzufuegen_button.grid(column=0, row=1)
        abrufen_button.grid(column=0, row=2)


class Mask(ttk.Frame):
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
        self.birthdateDayEntry = ttk.Entry(self)
        self.birthdateMonthEntry = ttk.Entry(self)
        self.birthdateYearEntry = ttk.Entry(self)

        self.VornameEntry.grid(column=1, row=1)
        self.VornameEntry.focus()
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
            NummerLabel.grid(column=0, row=11)
            abbrechenButton.grid(column=0, row=12)
        else:
            abbrechenButton.grid(column=0, row=11)

    def collect(self, number=False):
        """

        :type number: boolean
        """
        self.dict.clear()

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
            else:
                self.dict['Nummer'] = None
        return self.dict


class hinzufügen():
    def __init__(self, parent):
        mask = Mask(parent, False)
        ttk.Button(mask, text='Ausführen', command=(lambda: self.insert(mask.collect(False))), width=10).grid(
            column=1, row=11)

    def insert(self, dict):
        cnx = mysql.connector.connect(user='python', password='',
                                      host='127.0.0.1',
                                      database='adressbuch')

        cursor = cnx.cursor()
        add = (
            "INSERT INTO  `adressbuch` (`Vorname`, `Nachname`, `Straße`, `HausNr`, `Ort`, `PLZ`, `Land`, `birthdate`)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        data = [(dict['Vorname'], dict['Nachname'], dict['Straße'], dict['HausNr'], dict['Ort'], dict['PLZ'],
                 dict['Land'], make_date.init(dict))]

        cursor.executemany(add, data)
        cnx.commit()
        cnx.close()


class abfragen():
    def __init__(self, parent):
        self.mask = Mask(parent, True)
        ttk.Button(self.mask, text='Ausführen', command= display_entry(parent, self.search(self.mask.collect(True))),
                   width=10).grid(
            column=1, row=12)

    def search(self, dict):
        is_empty = False
        for x in dict:
            if x is not None:
                is_empty = True
                break
        if is_empty is True:
            self.mask.destroy()

        else:
            cnx = mysql.connector.connect(user='python', password='',
                                          host='127.0.0.1',
                                          database='adressbuch')

            cursor = cnx.cursor()
            vorgänger = False
            get = ("SELECT * FROM `adressbuch` WHERE ")

            if dict['Vorname'] is not None and vorgänger is False:
                get += " Vorname = %s"
                data = (dict['Vorname'],)
                vorgänger = True
            elif dict['Vorname'] is not None and vorgänger is not False:
                get += " and Vorname = %s"
                li = list(data)
                li.append(dict['Vorname'])
                data = tuple(li)
            if dict['Nachname'] is not None and vorgänger is False:
                get += " Nachname = %s"
                data = (dict['Nachname'],)
                vorgänger = True
            elif dict['Nachname'] is not None and vorgänger is not False:
                get += " and Nachname = %s"
                li = list(data)
                li.append(dict['Nachname'])
                data = tuple(li)
            if dict['Straße'] is not None and vorgänger is False:
                get += " Straße = %s"
                data = (dict['Straße'],)
                vorgänger = True
            elif dict['Straße'] is not None and vorgänger is not False:
                get += " and Straße = %s"
                li = list(data)
                li.append(dict['Straße'])
                data = tuple(li)
            if dict['HausNr'] is not None and vorgänger is False:
                get += " HausNr = %s"
                data = (dict['HausNr'],)
                vorgänger = True
            elif dict['HausNr'] is not None and vorgänger is not False:
                get += " and HausNr = %s"
                li = list(data)
                li.append(dict['HausNr'])
                data = tuple(li)
            if dict['Ort'] is not None and vorgänger is False:
                get += " Ort = %s"
                data = (dict['Ort'],)
                vorgänger = True
            elif dict['Ort'] is not None and vorgänger is not False:
                get += " and Ort = %s"
                li = list(data)
                li.append(dict['Ort'])
                data = tuple(li)
            if dict['PLZ'] is not None and vorgänger is False:
                get += " PLZ = %s"
                data = (dict['PLZ'],)
                vorgänger = True
            elif dict['PLZ'] is not None and vorgänger is not False:
                get += " and PLZ = %s"
                li = list(data)
                li.append(dict['PLZ'])
                data = tuple(li)
            if dict['Land'] is not None and vorgänger is False:
                get += " Land = %s"
                data = (dict['Land'],)
                vorgänger = True
            elif dict['Land'] is not None and vorgänger is not False:
                get += " and Land = %s"
                li = list(data)
                li.append(dict['Land'])
                data = tuple(li)
            if make_date.init(dict) is not None and vorgänger is False:
                get += " DATE(birthdate)= %s"
                data = (make_date.init(dict),)
                vorgänger = True
            elif make_date.init(dict) is not None and vorgänger is not False:
                get += " and Nummer = %s"
                li = list(data)
                li.append(dict[make_date.init(dict)])
                data = tuple(li)
            if dict['Nummer'] is not None and vorgänger is False:
                get += " Nummer = %s"
                data = (dict['Nummer'],)
                vorgänger = True
            elif dict['Nummer'] is not None and vorgänger is not False:
                get += " and Nummer = %s"
                li = list(data)
                li.append(dict['Nummer'])
                data = tuple(li)

            cursor.execute(get, data)
            # cursor.execute(get)
            result = cursor.fetchall()
            resultList = []
            for x in result:
                resultList.extend(list(x))
            cnx.commit()
            cnx.close()
        return resultList


class make_date():
    @staticmethod
    def init(dict):
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

        return date


class display_entry(ttk.Frame):
    def __init__(self, parent, list):
        super().__init__(parent)
        self.columnconfigure(1, weight=1)
        self.grid(column=0, row=0, sticky=(W + N + S + E))
        old_list = list.copy()
        v = int(len(old_list) / 8)
        if v is not 1:
            v = v - 1
        list.clear()
        for x in range(v):
            temp = []
            for y in range(9):
                temp.append(old_list[x * 8 + y + x])
            list.append(temp)
        del old_list
        display_entry_frames = []
        for x in range(len(list)):
            display_entry_frames.append(display_entry_frame(self, list[x]))

        self.current_page = 0
        menue_bar_frame = ttk.Frame(self)
        vor_button = ttk.Button(menue_bar_frame, text=">", command = lambda : update_page(False))
        zurueck_button = ttk.Button(menue_bar_frame, text="<", command = lambda : update_page(True))
        buffer_label = ttk.Label(menue_bar_frame, text="sample")
        vor_button.grid(column=2, row=0)
        zurueck_button.grid(column=0, row=0)
        buffer_label.grid(column=1, row=0)
        menue_bar_frame.grid(column=0, row=0)
        display_entry_frames[self.current_page].grid(column=0, row=1)

        def update_page(minus):
            if len(list) is not 1:
                display_entry_frames[self.current_page].grid_forget()

                if minus:
                    self.current_page = (self.current_page - 1) % (len(list) - 1)
                else:
                    self.current_page = (self.current_page + 1) % (len(list) - 1)

                display_entry_frames[self.current_page].grid(column=0, row=1)


class display_entry_frame(ttk.Frame):
    def __init__(self, parent, list):
        super().__init__(parent)
        mask = Mask(self, True)
        for x in range(len(list)):
            if list[x] is None:
                list[x] = "-"
        mask.VornameEntry.insert(0, str(list[0]))
        mask.NachnameEntry.insert(0, str(list[1]))
        mask.StraßeEntry.insert(0, str(list[2]))
        mask.HausNrEntry.insert(0, str(list[3]))
        mask.OrtEntry.insert(0, str(list[4]))
        mask.PLZEntry.insert(0, str(list[5]))
        mask.LandEntry.insert(0, str(list[6]))
        temp = str(list[7]).split('-')
        mask.birthdateDayEntry.insert(0, temp[2])
        mask.birthdateMonthEntry.insert(0, temp[1])
        mask.birthdateYearEntry.insert(0, temp[0])
        mask.NummerEntry.insert(0, str(list[8]))


Main()
