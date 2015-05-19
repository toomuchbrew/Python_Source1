__author__ = 'Chris'

from Tkinter import *


def doNothing():
    print("Okay.  Okay.  I won't.")

root = Tk(className = "Inside Sales Buddy")


menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "Lineal to Board", command = doNothing)
subMenu.add_command(label = "Board to Lineal", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Square to Lineal", command = doNothing)
subMenu.add_command(label = "Lineal to Square",command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "SonoTube Calc", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = root.quit)




#tkinter.messagebox.showinfo('Inside Sales Buddy', "money rules all")

root.mainloop()


