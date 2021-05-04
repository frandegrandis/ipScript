from abc import ABC
from tkinter import *
from tkinter.ttk import *
from MainWindow import MainWindow
from tkinter.filedialog import askopenfile


class LoadIPWindow(MainWindow, ABC):

    def setMainWindow(self):
        super().setMainWindow()
        #self.setBrowseWidget()
        self.setTextBoxWidget()
        # Aca agregamos las cosas extra que hace
        # Setlabels
        # SetWidgets
        # etc...

    def setWidgets(self):
        pass

    # BROWSE FILES WIDGET

    def open_file(self):
        file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt'),
                                                ('XML Files', '*.xml'),
                                                ('JSON Files', '*.json'),
                                                ('CSV Files', '*.csv')])

        if file is not None:
            # Do magic with the IPs
            content = file.read()
            print(content) # To test if it's working

    def setBrowseWidget(self):
        btn = Button(self.root, text='Abrir', command=lambda: self.open_file())
        btn.pack(side=TOP, pady=10)

    # TEXT BOX WIDGET

    def storeInput(self):
        input = self.inputtxt.get("1.0", "end-1c")
        print(input)

    def setTextBoxWidget(self):
        labelTextBox = Label(text="Ingrese las IPs a analizar")

        inputtxt = Text(self.root, bg="#FAFAFA")

        btn = Button(self.root, text="Procesar", command=lambda: self.storeInput())

        labelTextBox.pack()
        inputtxt.pack()
        btn.pack(side=BOTTOM, pady=10)
