from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('images/death.ico')

# r = IntVar()
# r.set('2')

modes = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')  # this selects pepperoni as the default option

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    label = Label(root, text=value)
    label.pack()


# Radiobutton(root, text='Option1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text='Option2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

# my_label = Label(root, text=pizza.get())
# my_label.pack()

my_button = Button(root, text='Click Me!',  command=lambda: clicked(pizza.get()))
my_button.pack()

mainloop()

# UP TO MESSAGE BOXES CURRENT TASK IS TO FIND HOW VARIABLES WORK AND LOG IT ON NOTES
