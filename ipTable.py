import tkinter as tk
import tksheet


class ipTable:

    def __init__(self,data):
        top = tk.Tk()
        headers = ["IP", "Location", "Is Proxy","Tor Node", "ASM"]
        sheet = tksheet.Sheet(top, headers=headers)
        sheet.grid()
        sheet.set_sheet_data(data)
        sheet.enable_bindings(("single_select",
                               "row_select",
                               "column_width_resize",
                               "arrowkeys",
                               "right_click_popup_menu",
                               "rc_select",
                               "copy"))
        sheet.pack(expand=1, fill=tk.BOTH)
        top.mainloop()

