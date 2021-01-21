from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry('400x200')


def graph():
    house_prices = np.random.normal(2000000, 25000, 5000)
    plt.polar(house_prices)  # histogram
    plt.show()


my_btn = Button(root, text='Graph It!', command=graph)
my_btn.pack()

root.mainloop()

