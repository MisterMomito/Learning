from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Learn to Code at Codemy.com')
root.geometry('500x400')

# Create a Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a Scrollbar to a Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Canvas
my_canvas.configure(yscrollcommand=my_scrollbar)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))
# ^^ what is binding and lambda e???

# Create ANOTHER frame Inside the Canvas
second_frame = Frame(my_canvas)

# Add that New Frame to a Window in the Canvas
my_canvas.create_window((0, 0), window=second_frame)  # what is creating a window???

for thing in range(100):
    Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, padx=10, pady=10)


mainloop()

