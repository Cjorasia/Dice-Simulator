import tkinter
from tkinter import *
import random

root = Tk()
root.geometry('250x325')
root.resizable(0,0)
def dice():
    number = random.randint(1,5)
    img = PhotoImage(file =f"diceFaces/{number}.png")
    panel = Label(root, image=img)
    panel.image = img
    panel.place(relx = 0.5, rely = 0.6, anchor = CENTER)


roll = Button(root , text = "Roll Dice!", command = dice)
roll.pack()
roll = Button(root , text = "Exit", command = root.destroy)
roll.pack()

root.mainloop()

