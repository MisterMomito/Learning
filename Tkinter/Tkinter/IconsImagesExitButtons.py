from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')  # window title
root.iconbitmap('images/death.ico')  # changing icon

my_img = ImageTk.PhotoImage(Image.open('images/picture1.jpg'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)  # quit button
button_quit.pack()

root.mainloop()
