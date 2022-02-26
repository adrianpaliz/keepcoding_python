from tkinter import *
from tkinter import ttk

class MainScript(Tk):
    entry = None
    scale = None
       
    def __init__(self):
        Tk.__init__(self)
        self.title("Thermometer")
        self.geometry("210x150")
        self.configure(bg = "#ECECEC")
        self.resizable(0, 0)
        
        self.temperature = StringVar(value = "")
        self.scale = StringVar(value = "C")
        
        self.create_layout()
    
    def create_layout(self):
        self.entry = ttk.Entry(self, textvariable = self.temperature).place(x = 10, y = 10)
        
        self.temperature_scale = ttk.Label(self, text = "Degrees:").place(x = 10, y = 45)
        
        self.radio_button_f = ttk.Radiobutton(self, text = "Fahrenheit", variable = self.scale, value="F").place(x = 20, y = 70)
        self.radio_button_c = ttk.Radiobutton(self, text = "Celsius", variable = self.scale, value="C").place(x = 20, y = 95)
    
    def start(self):
        self.mainloop()

if __name__ == '__main__':
    script = MainScript()
    script.start()


