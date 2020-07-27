import tkinter
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()

def roll():
    number = random.randint(1,6)
    print(number)
    return number
    
number = roll()

img = ImageTk.PhotoImage(Image.open(f"diceFaces/{number}.png"))
panel = Label(root, image=img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


roll = Button(root , text = "Roll Dice!", command = roll)
roll.pack()


root.mainloop()

