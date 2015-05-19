__author__ = 'cnicholson'

from Tkinter import *
import tkMessageBox

class App:
    def __init__(self):
        self.root = Tk(className = "The Inside Sales Buddy")

        self.labelLen = Label (self.root, text = "Length: ")
        self.labelThi = Label(self.root, text = "Thickness: ")
        self.labelWid = Label (self.root, text = "Width: ")

        self.labelLen.grid(row = 0, column =0)
        self.labelThi.grid(row = 1, column = 0)
        self.labelWid.grid(row = 2, column = 0)

        self.LenEntry = Entry()
        self.ThiEntry = Entry()
        self.WidEntry = Entry()

        self.LenEntry.grid(row = 0, column = 1)
        self.ThiEntry.grid(row = 1, column = 1)
        self.WidEntry.grid(row = 2, column = 1)

        self.calcbutton = IntVar()
        # self.calcbutton.set("Calculate")
        Button(self.root, text = "Calculate", command = self.clicked1).grid(row = 1, column =2)

        self.output = Label (self.root, text = "Board Feet: ")
        self.output.grid(columnspan = 2)


        self.root.mainloop()

    def clicked1(self):
        input1 = int(self.LenEntry.get())
        input2 = int(self.ThiEntry.get())
        input3 = int(self.WidEntry.get())
        result = float((input1 * input2 * input3)/12.0), " Board Feet "
        self.output.configure(text = result)

    def button_click(self, e):
        pass

App()