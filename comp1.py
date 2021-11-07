"""
    Author: Hayden Hopkinson
    Date started: 1/11/2021
    Description: this program should create a class that takes several parameters on creation, such as the placement, width/height, ect
    Version: 1.1
    Improvements since last version: changed the order of the GUI parameters so that the root was the first thing passed
"""

# libraries
from tkinter import *


# classes

class GUI:

    def __init__(self, parent, graphic_type, width, height, x_placement, y_placement, text = "", color = None, color2 = None, function = "", textvar = "", image = ""):
        
        self._type = graphic_type
        self._parent = parent
        self._text = text
        self._dimentions = (width, height)
        self._location = (x_placement, y_placement)
        self._function = function
        self._textvar = textvar
        self._colors = (color, color2)

        if(self._type == "PhotoImage"):
            self._image = PhotoImage(file = image)
            self._widget = Label(self._parent, image = self._image)
        else:
            if self._textvar == "":
                self._widget = eval(check_type(self._type))(self._parent, text = self._text)
            else:
                self._widget = eval(check_type(self._type))(self._parent, textvariable = self._textvar)
        self._widget.place(anchor = N, width = self._dimentions[0], height = self._dimentions[1], x = self._location[0], y = self._location[1])

        if(self._type == "Button"):
            self._widget.config(command = self._function, bg = self._colors[0], activebackground = self._colors[1])
        elif (self._type == "Entry"):
            self._widget.insert(END, self._text)

    def __repr__(self):
        return "this is a {} type of widget with the dimentions {} by {}, placed at {}, {}.".format(self._type, self._dimentions[0], self._dimentions[1], self._location[0], self._location[1]) + (" its defaut text is {}".format(self._text) if self._text != "" else "it has no default text") + (". it has a main color of {} and a secondary color of {}".format(self._colors[0], self._colors[1]) if self._colors[0] != None else ". it isn't colored")

    def get_img(self):
        return self._image

    def get_widget(self):
        return self._widget
    
#functions


def check_type(provided_type):
    """
    This function check the type of widget trying to be created, and compares it to a list of widgets that my program accepts.
    This is unnecessary once the project is completed, but may help when developing as it returns a list of accepted types in an error message to the shell 
    """
    accepted_types = ["Button", "Label", "Entry", "PhotoImage"]
    if(provided_type in accepted_types):
        return provided_type
    else:
        accepteds = ""
        for i in range(0, len(accepted_types)):
            accepteds = accepteds + " " + accepted_types[i] if i == (len(accepted_types) - 1) else accepteds + " " + accepted_types[i] + ","
        raise Exception("The type provided was not an accepted type, accepted types are:" + accepteds)

# main

#testing to see if this component works 

if(__name__ == "__main__"):

    width = "1000"
    height = "600"

    root = Tk()
    root.geometry(width + "x" + height)

    image = GUI(root, "PhotoImage", 200, 200, int(width)/2, int(height)/10, image = "testing.png")
    label = GUI(root, "Label", 50, 25, int(width)/2, int(height)/2, "Sand")
    entry = GUI(root, "Entry", 150, 25, int(width)/4, int(height)*8/13, "Sand2")
    button = GUI(root, "Button", 50, 25, int(width)/4, int(height)*2/3, "Sand3", "orange", "red")
    entry2 = GUI(root, "Entry", 150, 25, int(width)*3/4, int(height)*8/13, "Sand4")
    button2 = GUI(root, "Button", 50, 25, int(width)*3/4, int(height)*2/3, "Sand5", "cyan", "teal")

    root.mainloop()
