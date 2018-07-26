import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout): # where our functions are supposed to be
    #getting the '=' sign to work
    def calculate(self, calculation):
        if calculation: #if something was passd over
            try:
                #if I want to get the text out of the text input area (display: entry)
                self.display.text = str(eval(calculation))
            except Exception: #if some type of error occured
                self.display.text = "Error" # if I want to change the text that is in my text area   
                #go back to the kivy file so that I could point to this calculate() and have it execute whenever '=' is pressed

class CalculatorApp(App):
    
    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()#runs the entire application
