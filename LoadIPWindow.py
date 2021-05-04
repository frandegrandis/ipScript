from abc import ABC
from tkinter import *
from tkinter.ttk import *
from MainWindow import MainWindow
from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename
import tkinter as tk


class LoadIPWindow(MainWindow, ABC):

    def __init__(self):

        # dictionary of colors:
        self.color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}
        self.root = tk.Tk()
        self.btnState = False
        self.inputTxt = None
        self.entry = None

    def setMainWindow(self):
        super().setMainWindow()
        self.setBrowseFileWidget()
        self.setTextBoxWidget()
        # Aca agregamos las cosas extra que hace
        # Setlabels
        # SetWidgets
        # etc...

    # BROWSE FILES WIDGET

    def openFile(self):
        file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt'),
                                                ('XML Files', '*.xml'),
                                                ('JSON Files', '*.json'),
                                                ('CSV Files', '*.csv')])

        if file is not None:
            # Show directory path

            filename = askopenfilename()

            self.entry.insert(0, filename)
            # Do magic with the IPs
            content = file.read()
            print(content) # To test if it's working

    def setBrowseFileWidget(self):
        label2 = tk.Label(self.root, text="O cargue un archivo con las IPs", font="Bahnschrift 13", bg="white")
        label2.place(x=297, y=450)

        btn = Button(self.root, text='Abrir', command=lambda: self.openFile())
        btn.place(x=297, y=485)

        self.entry = Entry(self.root, width=90, state=DISABLED)
        self.entry.place(x=400, y=487)

        # TODO a este boton hay que ponerle el comando (metodo) que hace la magia del procesamiento de ips
        btnPr = Button(self.root, text="Procesar", command=lambda: self.storeInput())
        btnPr.place(x=580, y=533)

    # TEXT BOX WIDGET

    def storeInput(self):
        input = self.inputTxt.get("1.0", "end-1c")
        print(input)

    def setTextBoxWidget(self):
        label1 = tk.Label(self.root, text="Ingrese las IPs a analizar:", font="Bahnschrift 13", bg="white")
        label1.place(x=297, y=170)

        self.inputTxt = Text(self.root, bg="#FAFAFA", height=10)
        self.inputTxt.place(x=300, y=200)

        btn = Button(self.root, text="Procesar", command=lambda: self.storeInput())
        btn.place(x=580, y=390)
