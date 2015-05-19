from Tkinter import *
import tkMessageBox

class LtoB:
	def __init__(self):
	self.root = Tk(className = "The Inside Sales Buddy")
	
	self.labelBft (self.root, text = "Board Feet: ")
	self.labelThi (self.root, text = "Thickness: ")
	self.labelWid (self.root, text = "Width: ")
	
	self.labelBft.grid(row = 0, column = 0)
	self.labelThi.grid(row = 1, column = 0)
	self.labelWid.grid(row = 2, column = 0)
	
	self.BdfEntry = Entry()
	self.ThiEntry = Entry()
	self.WidEntry = Entry()
	
	self.BdfEntry.grid(row = 0, column = 1)
	self.ThiEntry.grid(row = 1, column = 1)
	self.WidEntry.grid(row = 2, column = 1)
	
	self.calcbutton = IntVar()
	Button(self.root, text = "Calculate", command = self.clicked2).grid(row 1, column 2)
	
	self.output2 = Label (self.root, text "Board Feet: ")
	self.output2.grid(columnspan = 2)
	
	self.root.mainloop()
	
def clicked2(self):
	input1 = int(self.BdfEntry.get())
	input2 = int(self.ThiEntry.get())
	input3 = int(self.WidEntry.get())
	result = int(((input1 * 12.0)/input2)/input3), "Lineal Feet "
	self.output2.configure(text = result)
	
def button_click(self, e)
	pass
	
LtoB()