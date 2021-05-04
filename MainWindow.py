from abc import abstractmethod, ABC
from tkinter import PhotoImage
import tkinter as tk


class MainWindow(ABC):

    def __init__(self):

        # dictionary of colors:
        self.color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}
        self.root = tk.Tk()
        self.navRoot = None
        self.homeLabel = None
        self.topFrame = None
        self.brandLabel = None
        self.navbarBtn = None
        self.closeBtn = None
        self.navIcon = None
        self.closeIcon = None
        self.btnState = False

    def setRoot(self):
        # setting root window:
        self.root.title("IP Tracker")
        self.root.config(bg="white")
        self.root.geometry("1600x900")

    @abstractmethod
    def setMainWindow(self):
        self.setRoot()
        self.setNavBar()

    def setNavBar(self):
        # option in the navbar:
        navbar_options = ["Home", "Cargar IPs", "Exportar IPs", "Métricas", "Mapa", "Ejemplo"]

        # loading Navbar icon image:
        self.navIcon = PhotoImage(file="Resources/menu.png")
        self.closeIcon = PhotoImage(file="Resources/close.png")

        # top Navigation bar:
        self.topFrame = tk.Frame(self.root, bg=self.color["green"])
        self.topFrame.pack(side="top", fill=tk.X)

        # Header label text:
        self.homeLabel = tk.Label(self.topFrame, text="IP Tracker", font="Bahnschrift 15", bg=self.color["green"], fg="gray17", height=2, padx=20)
        self.homeLabel.pack(side="right")

        # Main label text:
        # self.brandLabel = tk.Label(self.root, text="Pantalla\nPrincipal", font="System 30", bg="white", fg="green")
        # self.brandLabel.place(x=750, y=450)

        # Navbar button:
        self.navbarBtn = tk.Button(self.topFrame, image=self.navIcon, bg=self.color["green"], activebackground=self.color["green"], bd=0, padx=20, command=self.switch)
        self.navbarBtn.place(x=10, y=10)

        # setting Navbar frame:
        self.navRoot = tk.Frame(self.root, bg="gray17", height=1000, width=300)
        self.navRoot.place(x=-300, y=0)
        tk.Label(self.navRoot, font="Bahnschrift 15", bg=self.color["green"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

        # set y-coordinate of Navbar widgets:
        y = 80

        # Navbar Option Buttons:
        for i in range(len(navbar_options)):
            tk.Button(self.navRoot, text=navbar_options[i], font="BahnschriftLight 15", bg="gray17", fg=self.color["white"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
            y += 40

        # Navbar Close Button:
        self.closeBtn = tk.Button(self.navRoot, image=self.closeIcon, bg=self.color["green"], activebackground=self.color["green"], bd=0, command=self.switch)
        self.closeBtn.place(x=250, y=10)

    def configureOpeningNavbar(self):
        # make root dim:
        # self.brandLabel.config(bg=self.color["grey"], fg="#5F5A33")
        self.homeLabel.config(bg=self.color["darkgrey"])
        self.topFrame.config(bg=self.color["darkgrey"])
        self.root.config(bg=self.color["grey"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            self.navRoot.place(x=x, y=0)
            self.topFrame.update()

        # turing button ON:
        self.btnState = True

    def configureClosingNavbar(self):
        # create animated Navbar closing:
        for x in range(301):
            self.navRoot.place(x=-x, y=0)
            self.topFrame.update()

        # resetting widget colors:
        # self.brandLabel.config(bg="white", fg="green")
        self.homeLabel.config(bg=self.color["green"])
        self.topFrame.config(bg=self.color["green"])
        self.root.config(bg="white")

        # turning button OFF:
        self.btnState = False

    def switch(self):

        if self.btnState is True:
            self.configureClosingNavbar()
        else:
            self.configureOpeningNavbar()