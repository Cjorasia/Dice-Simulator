import random
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

def dice():

    number = random.randint(1,6)

    if number == 1:

        img = ImageTk.PhotoImage(Image.open("Dice face/1.png"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    if number == 2:
        img = ImageTk.PhotoImage(Image.open("Dice face/2.png"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    if number == 3:
        img = ImageTk.PhotoImage(Image.open("Dice face/3.png"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    if number == 4:
        img = ImageTk.PhotoImage(Image.open("Dice face/4.png"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    if number == 5:
        img = ImageTk.PhotoImage(Image.open("Dice face/5.png"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

    if number == 6:
        img = ImageTk.PhotoImage(Image.open("Dice face/6.jpeg"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

roll = Button(root , text = "Roll Dice!", command = dice )
roll.pack()
btn = Button(root, text = 'Exit', 
                command = root.destroy) 
btn.pack(side = 'top') 

root.mainloop()