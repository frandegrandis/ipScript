import settings
import tkinter as tk
from PageExportIP import PageExportIP
from PageLoadIP import PageLoadIP
import os
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import tksheet
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from ipAnalyzer import IPAnalyzer
from Page import Page
import tkinter as tk
from tkinter import messagebox



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888", "darkGreen": "#5c8712"}

        p1 = PageLoadIP(self)
        p1.config(bg=color["white"])

        p2 = PageExportIP(self)
        p2.config(bg=color["white"])

        #p3 = Page3(self)

        buttonframe = tk.Frame(self, bg=color["green"])
        container = tk.Frame(self)

        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        homeLabel = tk.Label(buttonframe, text="IP Tracker", font="Bahnschrift 15", bg=color["green"], fg="gray17", height=2, padx=20)
        homeLabel.pack(side="right")

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        #p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Cargar IPs", command=p1.lift, bg= "#dddddd", activebackground="#939393")
        b2 = tk.Button(buttonframe, text="Visualizar IPs", command=p2.updateTable,bg= "#dddddd", activebackground="#939393")
        #b3 = tk.Button(buttonframe, text="Métricas", command=p3.lift)

        b1.pack(side="left",padx = 5, pady=5)
        b2.pack(side="left",padx = 5, pady=5)
        #b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    settings.init()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.resizable(width=False, height=False)
    root.mainloop()