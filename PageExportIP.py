from tkinter import *
from tkinter.ttk import *
from ipAnalyzer import IPAnalyzer
from tkinter.filedialog import asksaveasfile
from Page import Page

import tksheet
import settings
import tkinter as tk



class PageExportIP(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.sheet = None
        self.ipAnalyzer = None
        self.color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}

        labelTitle = tk.Label(self, text="Visualizar y Exportar IPs del Sistema", font="Bahnschrift 20 bold", bg="white")
        labelTitle.place(x=120, y=40)

        self.setTableWidget()
        self.setExportWidget()

    # TABLE WIDGET

    def setTableWidget(self):
        label2 = tk.Label(self, text="IPs procesadas", font="Bahnschrift 13", bg="white")
        label2.place(x=10, y=120)

        headers = ["IP", "Location", "Is Proxy", "Tor Node", "ASM"]

        tableFrame = tk.Frame(self, bg=self.color["black"])
        tableFrame.place(x=10, y=160, height=300, width=803)

        # Para más opciones de customizado ver el github del flaco que armo la dependencia tksheet
        self.sheet = tksheet.Sheet(tableFrame, headers=headers, show_x_scrollbar=False, column_width=154)
        self.sheet.set_options(table_bg='white', index_bg='white')

        self.sheet.set_sheet_data(settings.data)
        self.sheet.enable_bindings()
        self.sheet.extra_bindings("column_select", func=self.sortTable)
        self.sheet.pack(expand=1, fill=tk.BOTH)

    def sortTable(self, event=None):
        # Event es una tupla del estilo (evento,columna_seleccionada)
        settings.data = sorted(settings.data, key=lambda x: x[event[1]])
        self.sheet.set_sheet_data(settings.data)

    def updateTable(self):
        self.sheet.set_sheet_data(settings.data)
        self.lift()

    # EXPORT WIDGET

    def saveFile(self):
        self.ipAnalyzer = IPAnalyzer()

        files = [('CSV Files', '*.csv')]

        file = asksaveasfile(filetypes=files, defaultextension='*.csv')

        self.ipAnalyzer.exportCSV(file.name,settings.data)

    def setExportWidget(self):
        label1 = tk.Label(self, text="Exportar IPs", font="Bahnschrift 13", bg="white")
        label1.place(x=10, y=500)

        btn = Button(self, text='Exportar', command=lambda: self.saveFile())
        btn.place(x=145, y=535)

        self.setDropdownWidget()

    def setDropdownWidget(self):
        optionsList = ["CSV File (*.csv)"]

        optSelected = StringVar()
        optSelected.set("one") # default value

        dropdown = OptionMenu(self, optSelected, *optionsList)
        dropdown.place(x=10, y=536)

        # TODO en base a la opcion elegida deberiamos hacer la conversion a ese formato