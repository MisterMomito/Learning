from tkinter import *
from tkinter import ttk

root = Tk()

options = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
           "Septiembre", "Octubre", "Noviembre", "Diciembre"]


def combo_click(event):
    Label(root, text=my_combo.get()).pack()


my_combo = ttk.Combobox(root, value=options)
my_combo.current(1)
my_combo.bind("<<ComboboxSelected>>", combo_click)
my_combo.pack()

mainloop()

birth_month = StringVar()
birth_month.set('Mes de\n Nacimiento')
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
          'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
birth_year_menu = ttk.Combobox(control_frame, value=months)

birth_year_menu.bind('<<ComboboxSelected>>', show_by_month())

birth_year_menu.grid(row=3, column=0, rowspan=1, padx=(0, 1), pady=3, sticky='ew')