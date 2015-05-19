__author__ = 'Chris'

from Tkinter import *

class ToBoardFeet:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.lengthLabel = Label(frame, text = "Length: ")
        self.lengthLabel.grid(row = 0, sticky = W)

        self.thicknessLabel = Label(frame, text = "Thickness: ")
        self.thicknessLabel.grid(row = 1, sticky = W)

        self.widthLabel = Label(frame, text = "Width: ")
        self.widthLabel.grid(row = 2, sticky = W)

        self.lengthEntry = Entry(frame)
        self.lengthEntry.grid(row = 0, column = 1)

        self.thicknessEntry = Entry(frame)
        self.thicknessEntry.grid(row = 1, column = 1)

        self.widthEntry = Entry(frame)
        self.widthEntry.grid(row =2, column = 1)

    #def TheMagic(self):


root = Tk(className = "Inside Sales Buddy")
b = ToBoardFeet(root)

root.mainloop()
