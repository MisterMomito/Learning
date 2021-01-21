from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Learn to Code at Codemy.com')
root.geometry('500x400')

# Create a Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)  # expands frames to size of their container

# Create a Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a Scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas

my_canvas.configure(yscrollcommand=my_scrollbar.set)  # the scrolling attaches to my_scrollbar
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))  # lambda e because when binding you pass an event
# bbox is a bounding box, and we're saying scroll that whole box

# Create Another Frame Inside the Canvas
second_frame = Frame(my_canvas)

# Add that New frame to a Window In the Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor='nw')  # bounding box starts at 0, 0 top-right corner

for thing in range(100):
    Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)
# put it on the second_frame
mainloop()

# Create a Main Frame
# Create a Canvas
# Add a Scrollbar to the canvas
# configure the canvas
# Create Another Frame Inside the Canvas
# Add that New frame to a Window In the Canvas

