"""
    Author: Hayden Hopkinson
    Date started: 6/11/2021
    description: this component will make a image gallery that should be displayed near the top of the canvas
    trial: 2
    trial changes: this should display all images at once instead of scrolling through them with buttons
"""

#libraries

from comp1 import *
import os, webbrowser

#classes

#functions

def get_images():
    """
gets and returns a list of images that are stored in the same filepath as this file 
    """
    images = []

    #get a list of every file stored in the same filepath as this
    for file in os.listdir():
        #check that the file ends in .png and is not the image i had used for testing
        if(file.endswith(".png") and file != "testing.png"):
            images.append(file)
    return images


def create_gallery(root, images, links, resolution):
    """
creates the image, credit button, and buttons to scroll throught the images
takes four parameters:
    root, the parent window to assign the GUI objects to
    images, a list of images to display
    links, a list of links to the website where the related image is from
    resolution, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    """
    image_widget = create_image(root, images, links, resolution)
    return image_widget


def create_image(root, images, links, res):
    """
this function creates the image, and the button that links to the source of the image, returning them in a list.
this takes four parameters:
    root, the parent window to assign the GUI objects to
    images, a list of image names to be displayed
    links, a list of links parallel to the images
    res, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    """
    image_labels = []
    link_buttons = []
    for i in range(0, len(images)):
        image_labels.append(GUI(root, "PhotoImage", 300, 200, int(res[0])/2 - 300 + (300*i), int(res[1])/6, image = images[i]))
        link_buttons.append(GUI(root, "Button", 300, 50, int(res[0])/2 - 300 + (300*i), int(res[1])/6+200, text = "image source", function = lambda i = i: open_page(links[i])))
    return [image_labels, link_buttons]

def open_page(page_to_open):
    """
this component should take the user to a specified webpage
it takes one parameter:
    page_to_open, the link to the webpage that should be opened
    """
    webbrowser.open(page_to_open)


#main

if(__name__ == "__main__"):

    #testing
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
