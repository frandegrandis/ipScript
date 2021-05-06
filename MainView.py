import tkinter as tk
from tkinter import PhotoImage
from LoadIPWindow import LoadIPWindow
from ExportIPWindow import ExportIPWindow
from PageLoadIP import PageLoadIP
from PageExportIP import PageExportIP
import settings

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}

        p1 = PageLoadIP(self)
        p2 = PageExportIP(self)
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

        b1 = tk.Button(buttonframe, text="Cargar IPs", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Visualizar IPs", command=p2.updateTable)
        #b3 = tk.Button(buttonframe, text="Métricas", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        #b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    settings.init()
    root.config(bg="white")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1280x720")
    root.mainloop()