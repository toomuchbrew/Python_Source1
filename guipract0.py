from Tkinter import *

root = Tk()
rootName = Label(root, text = "Inside Sales Buddy")
rootName.grid(row = 0)
label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 1, sticky = W)
label_2.grid(row = 2, stick = W)

entry_1.grid(row = 1, column = 1)
entry_2.grid(row = 2, column = 1)

c = Checkbutton(root, text = "Keep me Logged In")
c.grid(columnspan = 2)

root.mainloop() # Keeps window open / Displays

