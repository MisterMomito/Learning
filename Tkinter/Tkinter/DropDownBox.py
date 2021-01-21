from tkinter import *

root = Tk()
root.geometry('400x400')


def show():
    Label(root, text=clicked.get()).pack()


clicked = StringVar()


drop = OptionMenu(root, clicked, 'item 1', 'item2', 'item 3').pack()
clicked.set('DefaultVariable')

# or you can replace the items with a list
list_of_items = ['item 1', 'item 2', 'item 3']

drop2 = OptionMenu(root, clicked, *list_of_items).pack()

button = Button(root, text='Show Selection', command=show).pack()

root.mainloop()
