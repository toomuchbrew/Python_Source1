

# from ZetCode.Com

#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Zetcode Tkinter Tutorial

This script shows a simple window on the screen.

author: Jan Bodnar
Last modified: January 2011
website: www.zetcode.com
'''

from Tkinter import Tk, Frame, BOTH
from ttk import Frame, Style, Button

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent) ##, background = "white")

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Quit Button")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand = 1)

        quitButton = Button(self, text = "Quit", command = self.quit)
        quitButton.place(x =50, y = 50)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
