from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x400')


def show():
    Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(text='I DARE you to check this...', variable=var, onvalue='On', offvalue='Off')
c.deselect()
c.pack()

Button(root, text='Show Selection', command=show).pack()

root.mainloop()

