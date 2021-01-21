from tkinter import *
from PIL import ImageTk, Image

root = Tk()


def open():
    global my_img
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open('images/picture1.jpg'))
    my_label = Label(top, image=my_img).pack()
    Button(top, text='Close Window', command=top.destroy).pack()

# lbl = Label(top, text='Hello My World').pack()


button = Button(root, text='Open Second Window', command=open)
button.pack()


mainloop()
