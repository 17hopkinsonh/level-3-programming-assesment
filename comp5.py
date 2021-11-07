"""
    Author: Hayden Hopkinson
    Date started: 6/11/2021
    description: this component will make a image gallery that should be displayed near the top of the canvas
    Version: 1
    Improvements since last version: N/A

"""

#libraries
from comp1 import *
import os
#classes

"""
this is seeminly the only way to handle what is trying to be achieved, if i find a better way in the future this will change
"""
class image_displayed():
    
    current_value = 0

    def get_value():
        return image_displayed.current_value

    def set_value(new_value):
        image_displayed.current_value = new_value

#functions

def get_images():
    images = []

    for file in os.listdir():
        if(file.endswith(".png") and file != "testing.png"):
            images.append(file)

    return images

def create_gallery(root, images, links, resolution):
    image_widget = create_image(root, images[0], links[0], resolution)
    buttons = create_buttons(root, images, resolution, links, image_widget)
    return (image_widget, buttons)

def create_image(root, default_img, default_link, res):
    image = GUI(root, "PhotoImage", 300, 200, int(res[0])/2, int(res[1])/6, image = default_img)
    credit_label = GUI(root, "Label", int(res[0])-50, 50, int(res[0])/2, int(res[1])/6+200, text = "image from: " + default_link)
    return [image, credit_label]

def create_buttons(root, images, res, links, img_widget):
    buttons = []
    current_value = 0
    buttons.append(GUI(root, "Button", 100, 80, int(res[0])/2-50, int(res[1])/6 + 250, text = "<---", function = lambda: choose_img(images, links, img_widget, False)))
    buttons.append(GUI(root, "Button", 100, 80, int(res[0])/2+50, int(res[1])/6 + 250, text = "--->", function = lambda: choose_img(images, links, img_widget, True)))

def choose_img(images, links, widget, foward):

    old_value = image_displayed.get_value()
    if(abs(old_value) == len(images)-1):
        print(0)
        image_displayed.set_value(0)
        change_img(widget, images[0], links[0])
    else:
        new_num = old_value + (1 if foward else -1)
        print(new_num)
        image_displayed.set_value(new_num)
        change_img(widget, images[new_num], links[new_num])
        

def change_img(widget, image, link):
    widget[0].get_img().config(file = image)
    widget[1].get_widget().config(text = "image from: " + link)

#main

if(__name__ == "__main__"):

    width = "1000"
    height = "600"

    root = Tk()
    root.title("Title Here")
    root.geometry(width + "x" + height)

    links = [
    "https://publicdomainvectors.org/en/free-clipart/Vector-graphics-of-AZERTY-computer-keyboard/13672.html",
    "https://publicdomainvectors.org/en/free-clipart/LCD-screen-with-shadow-vector-graphics/13214.html",
    "https://publicdomainvectors.org/en/free-clipart/Photorealistic-vector-image-of-computer-mouse/12989.html"
    ]


    test = create_gallery(root, get_images(), links, (width, height))

    #GUI(root, "PhotoImage", 400, 400, 400, 400, image = "testing.png")

    root.mainloop()
