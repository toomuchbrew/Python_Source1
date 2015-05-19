__author__ = 'cnicholson'
#!/usr/bin/env python
import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButtom = tk.Button(self, text = 'Quit', command = self.quit())
        self.quitButtom.grid()

app = Application()
app.master.title('Sample Application')
app.mainloop()
