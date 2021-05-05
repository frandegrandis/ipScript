import tkinter as tk
import tksheet


class ipTable:

    def __init__(self, data):
        top = tk.Tk()
        headers = ["IP", "Location", "Is Proxy", "Tor Node", "ASM"]
        self.data = data
        self.sheet = tksheet.Sheet(top, headers=headers)
        self.sheet.grid()
        self.sheet.set_sheet_data(data)
        self.sheet.enable_bindings()
        self.sheet.extra_bindings("column_select", func=self.sortTable)
        self.sheet.pack(expand=1, fill=tk.BOTH)
        top.mainloop()

    def sortTable(self, event=None):
        # Event es una tupla del estilo (evento,columna_seleccionada)
        self.data = sorted(self.data, key=lambda x: x[event[1]])
        self.sheet.set_sheet_data(self.data)
