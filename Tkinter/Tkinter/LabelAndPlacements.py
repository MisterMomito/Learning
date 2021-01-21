from tkinter import *

root = Tk()  # main window

# Creating Labels
my_label1 = Label(root, text='Hello World!')
my_label2 = Label(root, text='My name is Moises')

# Shoving it onto the screen
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=2)

root.mainloop()




