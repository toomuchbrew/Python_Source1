fromt Tkinter import *
import tkMessageBox

class sftolf:
	def __init__(self):
		self.root = Tk(className = "The Inside Sales Buddy")
		
		self.labelSF = Label (self.root, text = "Square Feet: ")
		self.labelEx = Label (self.root, text = "Exposure: ")
		
		self.labelSF.grid(row = 0, column = 0)
		self.labelEx.grid(row = 1, column = 0)
		
		self.SFEntry = Entry()
		self.ExEntry = Entry()
		
		self.SFEntry.grid(row = 0, column = 1)
		self.ExEntry.grid(row = 1, column = 1)
		
		self.calcbutton = IntVar()
		Button(self.root, text = "Calculate", command = self.clicked3).grid(row = 1, column = 2)
		
		self.output3 = Label (self.root, text = "Lineal Feet: ")
		self.output3.grid(columnspan = 2)
		
		self.root.mainloop()
		
	def clicked3(self):
		input1 = int(self.SFEntry.get())
		input2 = float(self.ExEntry.get())
		result = int((input 1 * 12)/input2)
		self.output.configure(text = result)
		
	def button_click (self, e):
		pass

sftolf()