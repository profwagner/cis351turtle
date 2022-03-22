"""
gui4.py
"""

from tkinter import *
import turtle

class Box(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("My popup")
        self.grid()
        
        self._label = Label (self, text = "Hello, world!")
        self._label.grid()
        
        self._numberLabel = Label(self, text = "Number")
        self._numberLabel.grid (row = 1, column =0)
        self._numberVar = DoubleVar() #protected variable floating point
        self._numberEntry = Entry (self, textvariable = self._numberVar)
        self._numberEntry.grid(row = 1, column =1)

        self._doubleLabel = Label(self, text = "Double")
        self._doubleLabel.grid (row = 2, column =0)
        self._doubleVar = DoubleVar()
        self._doubleEntry = Entry (self, textvariable = self._doubleVar)
        self._doubleEntry.grid(row = 2, column =1)
        
        self._button = Button(self, text = "Click", command=self._switch)
        self._button.grid(row = 3, column = 0)

        self._doubleButton = Button (self, text = "Double", command=self._double)
        self._doubleButton.grid(row = 3, column = 1)
        
        self._canvas = Canvas()
        self._canvas.config(width=600, height=200)
        
        self._canvas.grid(row = 4, column = 0)
        self._screen = turtle.TurtleScreen(self._canvas)
        self.my_lovely_turtle = turtle.RawTurtle(self._screen, shape="turtle")
        self.my_lovely_turtle.fd(100)
        

    def _switch(self):
   
       if self._label["text"][:5]=="Hello":
            self._label["text"]="Hi, world!"
       else:
            self._label["text"]="Hello, world!"

    def _double(self):
        number = self._numberVar.get() #Retrieve value from text box
        double = 2*number
        self._doubleVar.set(double) #Store value into _doubleVar
        self.my_lovely_turtle.fd(double)
      
            
    

def main():

    Box().mainloop()
    
main()

