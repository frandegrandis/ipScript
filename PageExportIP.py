import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import tksheet

from ipAnalyzer import IPAnalyzer
from Page import Page
import tkinter as tk
from tkinter.filedialog import asksaveasfile


class PageExportIP(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.sheet = None

        self.color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}

        labelTitle = tk.Label(self, text="Visualizar y Exportar IPs del Sistema", font="Bahnschrift 20 bold", bg="white")
        labelTitle.place(x=450, y=80)

        self.setTableWidget()
        self.setExportWidget()

    # TABLE WIDGET

    def setTableWidget(self):
        label2 = tk.Label(self, text="IPs procesadas", font="Bahnschrift 13", bg="white")
        label2.place(x=297, y=170)

        headers = ["IP", "Location", "Is Proxy", "Tor Node", "ASM"]
        data = [["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1],["Fran","arg",1,1]]

        tableFrame = tk.Frame(self, bg=self.color["white"])
        tableFrame.place(x=400, y=230, height=200, width=800)

        self.sheet = tksheet.Sheet(tableFrame, headers=headers)

        self.sheet.set_sheet_data(data)
        self.sheet.enable_bindings()
        self.sheet.extra_bindings("column_select", func=self.sortTable)
        self.sheet.pack(expand=1, fill=tk.BOTH)

    def sortTable(self, event=None):
        # Event es una tupla del estilo (evento,columna_seleccionada)
        self.data = sorted(self.data, key=lambda x: x[event[1]])
        self.sheet.set_sheet_data(self.data)

    # EXPORT WIDGET

    def saveFile(self):
        files = [('Text Files', '*.txt'),
                 ('XML Files', '*.xml'),
                 ('JSON Files', '*.json'),
                 ('CSV Files', '*.csv')]

        file = asksaveasfile(filetypes=files, defaultextension=files)

    def setExportWidget(self):
        label1 = tk.Label(self, text="Exportar IPs", font="Bahnschrift 13", bg="white")
        label1.place(x=297, y=550)

        btn = Button(self, text='Exportar', command=lambda: self.saveFile())
        btn.place(x=420, y=585)

        self.setDropdownWidget()

    def setDropdownWidget(self):
        optionsList = ["Text File (*.txt)",
                       "XML File (*.xml)",
                       "JSON File (*.json)",
                       "CSV File (*.csv)"]

        optSelected = StringVar()
        optSelected.set("one") # default value

        dropdown = OptionMenu(self, optSelected, *optionsList)
        dropdown.place(x=297, y=586)

        # TODO en base a la opcion elegida deberiamos hacer la conversion a ese formato