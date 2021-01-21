from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

'''
# Returns file path:
root.filename = filedialog.askopenfilename(initialdir='images', title='Select a file',
                                           filetypes=(('jpg files', '*.jpg'), ('all files', '*.*')))

my_label = Label(root, text=root.filename).pack()
my_img = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_img).pack()  # why don't we need to put this in root?
'''


def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='images', title='Select a file',
                                               filetypes=(('jpg files', '*.jpg'), ('all files', '*.*')))

    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_img).pack()  # why don't we need to put this in root?


my_btn = Button(root, text='Open File', command=open).pack()

root.mainloop()
