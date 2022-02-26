from tkinter import *
from tkinter import ttk

class MainScript(Tk):
    entry = None
    scale = None
    
    __previous_temperature = ""
       
    def __init__(self):
        Tk.__init__(self)
        self.title("Thermometer")
        self.geometry("210x150")
        self.configure(bg = "#ECECEC")
        self.resizable(0, 0)
        
        self.temperature = StringVar(value = "")
        self.temperature.trace("w", self.validate_temperature)
        self.scale = StringVar(value = "F")
        
        self.create_layout()
    
    def create_layout(self):
        self.entry = ttk.Entry(self, textvariable = self.temperature).place(x = 10, y = 10)
        
        self.temperature_scale = ttk.Label(self, text = "Degrees:").place(x = 10, y = 45)        
        self.radio_button_f = ttk.Radiobutton(self, text = "Fahrenheit", variable = self.scale, value = "F" , command = self.selected_scale).place(x = 20, y = 70)
        self.radio_button_c = ttk.Radiobutton(self, text = "Celsius", variable = self.scale, value = "C" , command = self.selected_scale).place(x = 20, y = 95)
    
    def start(self):
        self.mainloop()
    
    def validate_temperature(self, *args):
        new_value = self.temperature.get()
        try:
            float(new_value)
            self.__previous_temperature = new_value
        except:
            self.temperature.set(self.__previous_temperature)
    
    def selected_scale(self):
        result = 0
        to_scale = self.scale.get()
        degree = float(self.temperature.get())
        
        if to_scale == 'F':
            result = degree * 9 / 5 + 32
        elif to_scale == 'C':
            result = (degree - 32) * 5 / 9
        else:
            result = degree
        
        self.temperature.set(result)

if __name__ == '__main__':
    script = MainScript()
    script.start()
