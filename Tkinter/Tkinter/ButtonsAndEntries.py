from tkinter import *

root = Tk()

e = Entry(root, width=50, fg='white', bg='blue', borderwidth=5)
e.pack()
e.insert(0, 'Enter Your Name')


def my_click():
    my_label = Label(root, text='hello ' + e.get())
    my_label.pack()


my_button = Button(root, text='Enter Your Name', command=my_click)
my_button.pack()

root.mainloop()
