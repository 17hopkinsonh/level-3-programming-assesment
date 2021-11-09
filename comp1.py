"""
    Author: Hayden Hopkinson
    Date started: 1/11/2021
    Description: this program should create a class that takes several parameters on creation, such as the placement, width/height, ect
    Version: 1.2
    Improvements since last version: merged GUI class with the old class from comp5 
"""

# libraries

from tkinter import *

# classes

class GUI:

    
    current_img = 0

    def __init__(self, parent, graphic_type, width, height, x_placement, y_placement, text = "", color = None, color2 = None, function = "", textvar = "", image = ""):
        
        self._type = graphic_type
        self._parent = parent
        self._text = text
        self._dimentions = (width, height)
        self._location = (x_placement, y_placement)
        self._function = function
        self._textvar = textvar
        self._colors = (color, color2)

        #if the type provided was a Photoimage, create a Photoimage with the provided file, and then make a label that displays the photoimage
        if(self._type == "PhotoImage"):
            self._image = PhotoImage(file = image)
            self._widget = Label(self._parent, image = self._image)
        else:
            #if a TextVar was not provided set the text to be the provided text, else a TextVar must've been provided, set the textvariable to be the provided TextVar
            #the difference between using a textvar or a text is that the textvar can be more easily updated later on,
            #as if the text stored in the TextVar is updated, the displayed text will also change
            if self._textvar == "":
                #eval is used here to change the provided graphic_type from a string to code,
                #for example if "Label" was passed as the graphic type the code runs Label(self._parent, text = self._text)
                self._widget = eval(check_type(self._type))(self._parent, text = self._text)
            else:
                self._widget = eval(check_type(self._type))(self._parent, textvariable = self._textvar)
        #place the widget at the provided location, with the provided width and height, anchored at the centre northmost point of the widget 
        self._widget.place(anchor = N, width = self._dimentions[0], height = self._dimentions[1], x = self._location[0], y = self._location[1])

        #if the provided type was a button it needs to be configured to be able to run a command when it is pressed
        if(self._type == "Button"):
            self._widget.config(command = self._function, bg = self._colors[0], activebackground = self._colors[1])
        #if the provided type was an entry box then setting the text needs to be done differently
        elif (self._type == "Entry"):
            self._widget.insert(END, self._text)

    def __repr__(self):
        return "this is a {} type of widget with the dimentions {} by {}, placed at {}, {},".format(self._type, self._dimentions[0], self._dimentions[1], self._location[0], self._location[1]) + (" its defaut text is {}".format(self._text) if self._text != "" else "it has no default text") + (". it has a main color of {} and a secondary color of {}".format(self._colors[0], self._colors[1]) if self._colors[0] != None else ". it isn't colored")

    def get_img(self):
        return self._image

    def get_widget(self):
        return self._widget

    def get_img_value():
        return GUI.current_img

    def set_img_value(new_img):
        GUI.current_img = new_img

    
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
        #an invalid type was provided, raise an exception that shows the accepted types that are currently accepted
        accepteds = ""
        for i in range(0, len(accepted_types)):
            accepteds = accepteds + " " + accepted_types[i] if i == (len(accepted_types) - 1) else accepteds + " " + accepted_types[i] + ","
        raise Exception("The type provided was not an accepted type, accepted types are:" + accepteds)

def print_test():
    """
    simple function to text if the button pressing works
    """
    print("button pressed")

# main
if(__name__ == "__main__"):

    #testing to see if this component works as expected
    width = "1000"
    height = "600"

    root = Tk()
    root.geometry(width + "x" + height)

    image = GUI(root, "PhotoImage", 200, 200, int(width)/2, int(height)/10, image = "testing.png")
    label = GUI(root, "Label", 50, 25, int(width)/2, int(height)/2, "Sand")
    entry = GUI(root, "Entry", 150, 25, int(width)/4, int(height)*8/13, "Sand2")
    button = GUI(root, "Button", 50, 25, int(width)/4, int(height)*2/3, "Sand3", "orange", "red", function = print_test)
    entry2 = GUI(root, "Entry", 150, 25, int(width)*3/4, int(height)*8/13, "Sand4")
    button2 = GUI(root, "Button", 50, 25, int(width)*3/4, int(height)*2/3, "Sand5", "cyan", "teal", function = print_test)

    print(label)

    root.mainloop()
