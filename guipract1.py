__author__ = 'Chris'

from tkinter import *

root = Tk()

def printName(event):
    print("My Name is Chris")

button_1 = Button(root, text = "print name")
button_1.bind("<Button-1>", printName)


button_1.pack()



root.mainloop()
