from tkinter import *
from tkinter import ttk

class MainScript(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Thermometer")
        self.geometry("200x150")
        self.configure(bg = "#DED789")

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    script = MainScript()
    script.start()
