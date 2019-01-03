from __future__ import print_function
from tkinter import *
import tkinter as ttk
from typing import List
import os.path

import datetime
import mysql.connector

class Main:
    def __init__(self):
        # Fenster wird erzeugt
        mainWin = Tk()
        mainWin.title('Adressbuch')
        mainWin.geometry('200x200+200+200')

        mainWin.columnconfigure(0, weight=1)
        mainWin.rowconfigure(0, weight=1)

        Menue(mainWin)

        mainWin.mainloop()




class Menue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        #erstellen des MenueFrames
        menueFrame = ttk.Frame()
        menueFrame.grid(column=0, row=0, sticky=(W+ N+S+E))

        # Frame wird dynamisch
        menueFrame.columnconfigure(0, weight=1)
        menueFrame.rowconfigure(0, weight=1)
        menueFrame.rowconfigure(1, weight=1)

        #erstellen der Buttons
        hinzufuegenButton = ttk.Button(menueFrame,text = "hinzufügen", command = lambda: Mask(parent))
        abrufenButton  = ttk.Button(menueFrame,text = "abrufen", command = lambda: Mask(parent, False))

        hinzufuegenButton.grid( column=0, row=0, sticky=(W+ N+S+E))
        abrufenButton.grid( column=0, row=1, sticky=(W+ N+S+E))



class Mask(ttk.Frame):

    def collect(self, Nummer = False):

        if self.VornameEntry.get():
            self.dict['Vorname'] = self.VornameEntry.get()
        else:
            self.dict['Vorname'] = None
        if self.NachnameEntry.get():
           self.dict['Nachname'] = self.NachnameEntry.get()
        else:
            self.dict['Nachname']= None
        if self.StraßeEntry.get():
            self.dict['Straße'] = self.StraßeEntry.get()
        else:
            self.dict['Straße'] = None
        if self.HausNrEntry.get():
            self.dict['HausNr']= self.HausNrEntry.get()
        else:
            self.dict['HausNr'] = None
        if  self.OrtEntry.get():
            self.dict['Ort']= self.OrtEntry.get()
        else:
            self.dict['Ort'] = None
        if  self.PLZEntry.get():
            self.dict['PLZ'] = self.PLZEntry.get()
        else:
            self.dict['PLZ'] = None
        if  self.LandEntry.get():
            self.dict['Land']= self.LandEntry.get()
        else:
            self.dict['Land'] = None
        if self.birthdateYearEntry.get():
            self.dict['birthdateYear'] = self.birthdateYearEntry.get()
        if self.birthdateMonthEntry.get():
            self.dict['birthdateMonth'] = self.birthdateMonthEntry.get()
        if self.birthdateDayEntry.get():
            self.dict['birthdateDay'] = self.birthdateDayEntry.get()
        if Nummer == True and  self.NummerEntry.get() :
            self.dict['Nummer'] = self.NummerEntry.get()




        return self.dict


    def __init__(self, parent, Nummer = False ):
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
        if Nummer == True:
            NummerLabel = ttk.Label(self, text="Nummer")


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
        if Nummer == True:
            NummerLabel.grid(column=0, row=11)



        # erstellen und einfügen der Entrys zu den jeweiligen Labels
        if Nummer == True:
            self.NummerEntry = ttk.Entry(self)
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
        self.birthdateYearEntry.grid(column=1, row=8)
        self.birthdateMonthEntry.grid(column=1, row=9)
        self.birthdateDayEntry.grid(column=1, row=10)
        if Nummer == True:
            self.NummerEntry.grid(column=1, row=11)
            ttk.Button(self, text='collect', command=lambda: abfragen((self.collect(Nummer)))).grid(column=1, row=12)
        else:
            ttk.Button(self, text='collect', command= lambda: abfragen((self.collect(Nummer)))).grid(column=1, row=11)

class abfragen():
    def __init__(self, dict):
        cnx = mysql.connector.connect(user='python', password='',
                                      host='127.0.0.1',
                                      database='adressbuch')

        cursor = cnx.cursor()
        add = ("INSERT INTO  `adressbuch` (`Vorname`, `Nachname`, `Straße`, `HausNr`, `Ort`, `PLZ`, `Land`, `birthdate`)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        Month = int(dict['birthdateMonth'])
        Day =int(dict['birthdateDay'])
        Year = int(dict['birthdateYear'])


        date = datetime.datetime(Year, Month, Day)
        date = datetime.datetime

        data = [(dict['Vorname'], dict['Nachname'], dict['Straße'], dict['HausNr'], dict['Ort'], dict['PLZ'], dict['Land'], date)]
        cursor.executemany(add, data)


        cnx.commit()

        cnx.close()






Main()