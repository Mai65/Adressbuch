from tkinter import *
import tkinter as ttk
from typing import List
import os.path

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
        menueFrame.grid()

        # Frame wird dynamisch
        menueFrame.columnconfigure(0, weight=1)
        menueFrame.rowconfigure(0, weight=1)
        menueFrame.rowconfigure(1, weight=1)

        #erstellen der Buttons
        hinzufuegenButton = ttk.Button(menueFrame,text = "hinzufügen")
        abrufenButton  = ttk.Button(menueFrame,text = "abrufen")

        hinzufuegenButton.grid( column=0, row=0, sticky=(W+ N+S+E))
        abrufenButton.grid( column=0, row=1, sticky=(W+ N+S+E))



Main()