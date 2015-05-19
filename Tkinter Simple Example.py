

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

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand = 1)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
