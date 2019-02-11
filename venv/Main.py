from __future__ import print_function
from tkinter import *
import tkinter as ttk
from tkinter import Tk
from tkinter import messagebox
from typing import List
import os.path
import numpy as np

import datetime
import mysql.connector


cnx = mysql.connector.connect(user='pi', password='',
                                      host='192.168.2.100',
                                      database='adressbuch')

class Main:
    def __init__(self):

        # Fenster wird erzeugt
        main_win = Tk()
        main_win.title('Adressbuch')

        main_win.columnconfigure(0, weight=1)
        main_win.rowconfigure(0, weight=1)

        self.menue = Menue(main_win)

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
        alleAbrufen_button = ttk.Button(menue_frame, text="Alle Abrufen",command=lambda: alleAbfragen(parent), width=10)

        # Erstellen des Labels
        adressbuch = Label(menue_frame, text="Adressbuch", font=("Helvetica", 16))

        # Widgets werden angeordnet
        adressbuch.grid(column=0, row=0)
        hinzufuegen_button.grid(column=0, row=1)
        abrufen_button.grid(column=0, row=2)
        alleAbrufen_button.grid(column=0, row=3)


class Mask(ttk.Frame):
    def __init__(self, parent, number=False):
        self.dict = {}
        self.parent = parent
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

    def collect(self, number=False, checkForCompleteDate=False):
        """

        :type number: boolean
        """
        is_empty = True

        self.dict.clear()

        # Einsammeln der Einträge in ein dict wenn kein Wert vorhanden Wert = None
        if self.VornameEntry.get():
            self.dict['Vorname'] = self.VornameEntry.get()
            is_empty = False
        else:
            self.dict['Vorname'] = None
        if self.NachnameEntry.get():
            is_empty = False
            self.dict['Nachname'] = self.NachnameEntry.get()
        else:
            self.dict['Nachname'] = None
        if self.StraßeEntry.get():
            is_empty = False
            self.dict['Straße'] = self.StraßeEntry.get()
        else:
            self.dict['Straße'] = None
        if self.HausNrEntry.get():
            is_empty = False
            self.dict['HausNr'] = self.HausNrEntry.get()
        else:
            self.dict['HausNr'] = None
        if self.OrtEntry.get():
            is_empty = False
            self.dict['Ort'] = self.OrtEntry.get()
        else:
            self.dict['Ort'] = None
        if self.PLZEntry.get():
            is_empty = False
            self.dict['PLZ'] = self.PLZEntry.get()
        else:
            self.dict['PLZ'] = None
        if self.LandEntry.get():
            is_empty = False
            self.dict['Land'] = self.LandEntry.get()
        else:
            self.dict['Land'] = None
        if self.birthdateYearEntry.get():
            is_empty = False
            self.dict['birthdateYear'] = self.birthdateYearEntry.get()
        else:
            self.dict['birthdateYear'] = None
        if self.birthdateMonthEntry.get():
            is_empty = False
            self.dict['birthdateMonth'] = self.birthdateMonthEntry.get()
        else:
            self.dict['birthdateMonth'] = None
        if self.birthdateDayEntry.get():
            is_empty = False
            self.dict['birthdateDay'] = self.birthdateDayEntry.get()
        else:
            self.dict['birthdateDay'] = None

        # einsammmeln der Nummer nur wenn Nummer mit angegeben
        if number:
            if self.NummerEntry.get():
                self.dict['Nummer'] = self.NummerEntry.get()
                is_empty = False
            else:
                self.dict['Nummer'] = None

        if checkForCompleteDate is True:
            if self.birthdateYearEntry.get() and (not self.birthdateMonthEntry.get() or not self.birthdateDayEntry.get()):
                return 1
            elif self.birthdateMonthEntry.get() and (not self.birthdateYearEntry.get() or not self.birthdateDayEntry.get()):
                return 1
            elif self.birthdateDayEntry.get() and (not self.birthdateYearEntry.get() or not self.birthdateMonthEntry.get()):
                return 1
        if is_empty is True:
            return None
        else:
            return self.dict


class hinzufügen():
    def __init__(self, parent):
        mask = Mask(parent, False)

        ttk.Button(mask, text='Ausführen', command=(
            lambda: (insert(mask.collect(False)) if mask.collect(False, True) is not None and mask.collect(False, True) is not 1 else (
                messageboxes.incomplete_birthdate() if mask.collect(False, True) is 1 else messageboxes.no_entry_in_mask()),mask.destroy(), hinzufügen(parent))),
                   width=10).grid(
            column=1, row=11)
        ttk.Button(mask, text="zurück", command=mask.destroy, width=10).grid(
            column=0, row=11)


class abfragen():
    def __init__(self, parent):
        mask = Mask(parent, True)
        ausführen = ttk.Button(mask, text='Ausführen', command=lambda: display_entry(parent, self.search(mask.collect(True))) if mask.collect(True, False) is not None and self.search(mask.collect(True)) else (messageboxes.no_entry_in_mask() if mask.collect(True, False) is None else messageboxes.no_entry_in_DB()),
                                    width=10)
        ausführen.grid(column=1, row=12)
        ttk.Button(mask, text="zurück", command=mask.destroy, width=10).grid(
            column=0, row=12)

    def search(self, dict):


        cursor = cnx.cursor()
        sql_and_data = make_get_and_data_sql(dict)


        cursor.execute(list(sql_and_data)[0], list(sql_and_data)[1])
        result = cursor.fetchall()
        result_list = []
        for x in result:
            result_list.extend(list(x))
        cnx.commit()
        return result_list

class alleAbfragen():
    def __init__(self, parent):
        list
        display_entry(parent, self.get_data())




    def get_data(self):
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM `adressbuch`")
        result = cursor.fetchall()
        result_list = []
        for x in result:
            result_list.extend(list(x))
        cnx.commit()
        return result_list



class display_entry(ttk.Frame):
    def __init__(self, parent, list):
        super().__init__(parent)
        self.grid(column=0, row=0, sticky=(W + N + S + E))

        list = np.array(list).reshape(int(len(list) / 9), 9).tolist()

        display_entry_frames = []
        for x in range(len(list)):
            display_entry_frames.append(display_entry_frame(self, list[x]))

        self.current_page = 0
        menue_bar_frame = ttk.Frame(self)
        vor_button = ttk.Button(menue_bar_frame, text=">", command=lambda: update_page(False))
        zurueck_button = ttk.Button(menue_bar_frame, text="<", command=lambda: update_page(True))
        buffer_label = ttk.Label(menue_bar_frame, text="sample")
        vor_button.grid(column=2, row=0)
        zurueck_button.grid(column=0, row=0)
        buffer_label.grid(column=1, row=0)
        menue_bar_frame.grid(column=0, row=0)
        display_entry_frames[self.current_page].grid(column=0, row=1)
        ttk.Button(self, text="Zurück", command=self.destroy, width=10).grid(
            column=0, row=3)
        ttk.Button(self, text="Aktualisieren ", command=lambda: (parent.destroy(), Main(), sys.exit) if updat_entry(
            display_entry_frames[self.current_page].mask, True) is None else None, width=10).grid(
            column=1, row=3)
        ttk.Button(self, text="Löschen", command=lambda: (parent.destroy(), Main(), sys.exit) if delete_entry(display_entry_frames[self.current_page].mask.collect(True)['Nummer']) is None else None, width=10).grid(
            column=2, row=3)

        def update_page(minus):
            if len(list) is not 1:
                display_entry_frames[self.current_page].grid_forget()
                if minus:
                    self.current_page = (self.current_page - 1) % (len(list))
                else:
                    self.current_page = (self.current_page + 1) % (len(list))

                display_entry_frames[self.current_page].grid(column=0, row=1)


class display_entry_frame(ttk.Frame):
    def __init__(self, parent, list):
        super().__init__(parent)
        self.mask = Mask(self, True)
        self.fillup_None(list)
        self.insert_text(self.mask, list)

    def insert_text(self, mask, list):
        mask.VornameEntry.insert(0, str(list[0]))
        mask.NachnameEntry.insert(0, str(list[1]))
        mask.StraßeEntry.insert(0, str(list[2]))
        mask.HausNrEntry.insert(0, str(list[3]))
        mask.OrtEntry.insert(0, str(list[4]))
        mask.PLZEntry.insert(0, str(list[5]))
        mask.LandEntry.insert(0, str(list[6]))
        if str(list[7]) is not '-':
            temp = str(list[7]).split('-')
        else:
            temp = ['-', '-', '-']
        mask.birthdateDayEntry.insert(0, temp[2])
        mask.birthdateMonthEntry.insert(0, temp[1])
        mask.birthdateYearEntry.insert(0, temp[0])
        mask.NummerEntry.grid_forget()
        NummerLabelDisplay = ttk.Label(mask, text=str(list[8]))
        NummerLabelDisplay.grid(column=1, row=11)
        mask.NummerEntry.insert(0, str(list[8]))

    def fillup_None(self, list):
        for x in range(len(list)):
            if list[x] is None:
                list[x] = "-"


class messageboxes():

    @staticmethod
    def incomplete_birthdate():
        messagebox.showerror("Error", "Sie haben nur Teile des Geburtsdatums angegeben. Bitte vervollständigen sie es.")

    @staticmethod
    def no_entry_in_mask():
        messagebox.showerror("Error", "Sie haben keinen Wert eingegeben. Bitte versuchen sie es erneut.")

    @staticmethod
    def no_entry_in_DB():
        messagebox.showerror("Error", "Ihr angeforderter Eintrag existiert nicht")

    @staticmethod
    def entry_updated():
        messagebox.showinfo("Updated", "Eintrag erfolgreich aktuallisiert")

def insert(dict, withNumber=False):
    cursor = cnx.cursor()
    if withNumber is True:
        add = (
            "INSERT INTO  `adressbuch` (`Vorname`, `Nachname`, `Straße`, `HausNr`, `Ort`, `PLZ`, `Land`, `birthdate`, `Nummer`)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

        data = [(dict['Vorname'], dict['Nachname'], dict['Straße'], dict['HausNr'], dict['Ort'], dict['PLZ'],
                 dict['Land'], make_date(dict), dict['Nummer'])]

    else:
        add = (
            "INSERT INTO  `adressbuch` (`Vorname`, `Nachname`, `Straße`, `HausNr`, `Ort`, `PLZ`, `Land`, `birthdate`)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        data = [(dict['Vorname'], dict['Nachname'], dict['Straße'], dict['HausNr'], dict['Ort'], dict['PLZ'],
                 dict['Land'], make_date(dict))]

    cursor.executemany(add, data)
    cnx.commit()



def make_date(dict):
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


def updat_entry(mask, withNumber=False):

    cursor = cnx.cursor()

    dict = mask.collect(withNumber)
    for x in dict:
        if dict[x] is '-':
            dict[x] = None

    delete_entry(dict['Nummer'], cursor)
    insert(dict, True)
    messageboxes.entry_updated()

def delete_entry(nummer):

    cursor = cnx.cursor()
    delete = "DELETE FROM `adressbuch` WHERE (Nummer = %s)"
    data = (nummer,)

    cursor.execute(delete, data)
    cnx.commit()

def make_get_and_data_sql(dict):
    vorgaenger = False
    get = "SELECT * FROM `adressbuch` "

    if dict['Vorname'] is not None and vorgaenger is False:
        get += " WHERE Vorname = %s"
        data = (dict['Vorname'],)
        vorgaenger = True
    if dict['Nachname'] is not None and vorgaenger is False:
        get += " WHERE Nachname = %s"
        data = (dict['Nachname'],)
        vorgaenger = True
    elif dict['Nachname'] is not None and vorgaenger is not False:
        get += " and Nachname = %s"
        li = list(data)
        li.append(dict['Nachname'])
        data = tuple(li)
    if dict['Straße'] is not None and vorgaenger is False:
        get += " WHERE Straße = %s"
        data = (dict['Straße'],)
        vorgaenger = True
    elif dict['Straße'] is not None and vorgaenger is not False:
        get += " and Straße = %s"
        li = list(data)
        li.append(dict['Straße'])
        data = tuple(li)
    if dict['HausNr'] is not None and vorgaenger is False:
        get += " WHERE HausNr = %s"
        data = (dict['HausNr'],)
        vorgaenger = True
    elif dict['HausNr'] is not None and vorgaenger is not False:
        get += " and HausNr = %s"
        li = list(data)
        li.append(dict['HausNr'])
        data = tuple(li)
    if dict['Ort'] is not None and vorgaenger is False:
        get += " WHERE Ort = %s"
        data = (dict['Ort'],)
        vorgaenger = True
    elif dict['Ort'] is not None and vorgaenger is not False:
        get += " and Ort = %s"
        li = list(data)
        li.append(dict['Ort'])
        data = tuple(li)
    if dict['PLZ'] is not None and vorgaenger is False:
        get += " WHERE PLZ = %s"
        data = (dict['PLZ'],)
        vorgaenger = True
    elif dict['PLZ'] is not None and vorgaenger is not False:
        get += " and PLZ = %s"
        li = list(data)
        li.append(dict['PLZ'])
        data = tuple(li)
    if dict['Land'] is not None and vorgaenger is False:
        get += " WHERE Land = %s"
        data = (dict['Land'],)
        vorgaenger = True
    elif dict['Land'] is not None and vorgaenger is not False:
        get += " and Land = %s"
        li = list(data)
        li.append(dict['Land'])
        data = tuple(li)

    if dict['birthdateDay'] is not None and vorgaenger is False:
        get += " WHERE DAY(birthdate)= %s"
        data = (dict['birthdateDay'],)
        vorgaenger = True
    elif dict['birthdateDay'] is not None and vorgaenger is not False:
        get += " and DAY(birthdate) = %s"
        li = list(data)
        li.append(dict['birthdateDay'])
        data = tuple(li)
    if dict['birthdateMonth'] is not None and vorgaenger is False:
        get += " WHERE MONTH(birthdate)= %s"
        data = (dict['birthdateMonth'],)
        vorgaenger = True
    elif dict['birthdateMonth'] is not None and vorgaenger is not False:
        get += " and MONTH(birthdate) = %s"
        li = list(data)
        li.append(dict['birthdateMonth'])
        data = tuple(li)
    if dict['birthdateYear'] is not None and vorgaenger is False:
        get += " WHERE YEAR(birthdate)= %s"
        data = (dict['birthdateYear'],)
        vorgaenger = True
    elif dict['birthdateYear'] is not None and vorgaenger is not False:
        get += " and YEAR(birthdate) = %s"
        li = list(data)
        li.append(dict['birthdateYear'])
        data = tuple(li)

    if dict['Nummer'] is not None and vorgaenger is False:
        get += " WHERE Nummer = %s"
        data = (dict['Nummer'],)
    elif dict['Nummer'] is not None and vorgaenger is not False:
        get += " and Nummer = %s"
        li = list(data)
        li.append(dict['Nummer'])
        data = tuple(li)

    return get, data

Main()
