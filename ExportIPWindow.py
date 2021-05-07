from abc import ABC
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from MainWindow import MainWindow
from tkinter.filedialog import asksaveasfile


class ExportIPWindow(MainWindow, ABC):

    def setMainWindow(self):
        super().setMainWindow()
        self.setExportWidget()
        self.setTableWidget()

        # Aca agregamos las cosas extra que hace
        # Setlabels
        # SetWidgets
        # etc...

    def setScreenTitle(self):
        super().setScreenTitle("Visualizar y Exportar IPs del Sistema", 410)

    # TABLE WIDGET

    def setTableWidget(self):
        label2 = tk.Label(self.root, text="IPs procesadas", font="Bahnschrift 13", bg="white")
        label2.place(x=297, y=170)

        # TODO Borrar una vez este la tabla
        label = tk.Label(self.root, text="ACA VA \n LA TABLA", font="System 30", bg="white")
        label.place(x=500, y=300)

    # EXPORT WIDGET

    def saveFile(self):
        files = [('Text Files', '*.txt'),
                 ('XML Files', '*.xml'),
                 ('JSON Files', '*.json'),
                 ('CSV Files', '*.csv')]

        file = asksaveasfile(filetypes=files, defaultextension=files)

    def setExportWidget(self):
        label1 = tk.Label(self.root, text="Exportar IPs", font="Bahnschrift 13", bg="white")
        label1.place(x=297, y=550)

        btn = Button(self.root, text='Exportar', command=lambda: self.saveFile())
        btn.place(x=420, y=585)

        self.setDropdownWidget()

    def setDropdownWidget(self):
        optionsList = ["Text File (*.txt)",
                       "XML File (*.xml)",
                       "JSON File (*.json)",
                       "CSV File (*.csv)"]

        optSelected = StringVar()
        optSelected.set("one") # default value

        dropdown = OptionMenu(self.root, optSelected, *optionsList)
        dropdown.place(x=297, y=586)

        # TODO en base a la opcion elegida deberiamos hacer la conversion a ese formato