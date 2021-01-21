from tkinter import *

root = Tk()

hello_frame = Frame(root, width=400, height=250, borderwidth=1)
hello_frame.pack(fill=BOTH)

hello_label = Label(hello_frame, text='HELLO')
hello_label.place(relx=0.5, rely=0.5)

mainloop()
