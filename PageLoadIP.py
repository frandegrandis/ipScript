import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from ipAnalyzer import IPAnalyzer
from Page import Page
import tkinter as tk
from tkinter import messagebox
import settings

class PageLoadIP(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}
        self.inputTxt = None
        self.entry = None
        self.filepath = tk.StringVar()
        self.ipAnalyzer = None
        self.directoryPath = None

        labelTitle = tk.Label(self, text="Cargar IPs en el Sistema", font="Bahnschrift 20 bold", bg="white")
        labelTitle.place(x=450, y=40)

        self.setTextBoxWidget()
        self.setBrowseFileWidget()

    def analysis(self):
        self.ipAnalyzer = IPAnalyzer()
        self.ipAnalyzer.read(self.directoryPath)
        self.ipAnalyzer.processIpList()
        settings.data = self.ipAnalyzer.getIPList()
        messagebox.showinfo(title="Operacion exitosa", message="La operacion se ha realizado de forma exitosa")


    # TEXT BOX WIDGET

    def storeInput(self):
        input = self.inputTxt.get("1.0", "end-1c")
        text_file = open("ips.txt", "w")
        self.directoryPath = "ips.txt"
        text_file.write(input)
        text_file.close()

        self.analysis()
        os.remove("ips.txt")

    def setTextBoxWidget(self):
        label1 = tk.Label(self, text="Ingrese las IPs a analizar:", font="Bahnschrift 13", bg="white")
        label1.place(x=297, y=120)

        self.inputTxt = Text(self, bg="#FAFAFA", height=10)
        self.inputTxt.place(x=300, y=150)

        btn = Button(self, text="Procesar", command=lambda: self.storeInput())
        btn.place(x=580, y=340)
        btn.config()

    # BROWSE FILES WIDGET

    def openFile(self):
        file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt'),
                                                ('XML Files', '*.xml'),
                                                ('JSON Files', '*.json'),
                                                ('CSV Files', '*.csv')])

        if file is not None:
            # X-Scrollbar in case path is longer than entry box
            #TODO tampoco me voy a calentar haciendo esto ahora, no es tan importante

            # Show directory path
            self.directoryPath = file.name
            self.filepath.set(file.name)
            self.entry = Entry(self, textvariable=self.filepath, width=90, state=DISABLED)
            self.entry.place(x=400, y=447)

    def setBrowseFileWidget(self):
        label2 = tk.Label(self, text="O cargue un archivo con las IPs:", font="Bahnschrift 13", bg="white")
        label2.place(x=297, y=410)

        btn = Button(self, text='Abrir', command=lambda: self.openFile())
        btn.place(x=297, y=445)

        self.entry = Entry(self, width=90, state=DISABLED)
        self.entry.place(x=400, y=447)

        btnPr = Button(self, text="Procesar", command=lambda: self.analysis())
        btnPr.place(x=580, y=493)