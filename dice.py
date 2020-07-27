import tkinter
from tkinter import *
import random

root = Tk()

def dice():
    number = random.randint(1,6)
    img = PhotoImage(file =f"diceFaces/{number}.png")
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side = "bottom", fill = "both", expand = "yes")


roll = Button(root , text = "Roll Dice!", command = dice)
roll.pack()
roll = Button(root , text = "Exit", command = root.destroy)
roll.pack()

root.mainloop()

