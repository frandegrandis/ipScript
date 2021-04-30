from tkinter import PhotoImage
import tkinter as tk

# dictionary of colors:
color = {"nero": "#252726", "green": "#85BC26", "black": "#000000", "white": "#FFFFFF", "grey": "#BBBBBB", "darkgrey": "#888888"}

# setting root window:
root = tk.Tk()
root.title("IP Tracker")
root.config(bg="white")
root.geometry("1600x900")


# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="white", fg="green")
        homeLabel.config(bg=color["green"])
        topFrame.config(bg=color["green"])
        root.config(bg="white")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["grey"], fg="#5F5A33")
        homeLabel.config(bg=color["darkgrey"])
        topFrame.config(bg=color["darkgrey"])
        root.config(bg=color["grey"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


# top Navigation bar:
topFrame = tk.Frame(root, bg=color["green"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Deloitte", font="Bahnschrift 15", bg=color["green"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="IP\nTracker", font="System 30", bg="white", fg="green")
brandLabel.place(x=750, y=450)

# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["green"], activebackground=color["green"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["green"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Cargar IPs", "Visualizar IPs", "Exportar IPs", "Acerca de", "Contacto"]
# Navbar Option Buttons:
for i in range(5):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["white"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["green"], activebackground=color["green"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

# window in mainloop:
root.mainloop()