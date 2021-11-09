"""
    Author: Hayden Hopkinson
    Date started: 8/11/2021
    description: this component should let you repeat some code every x amount of seconds
    Version: 1
    Improvements since last version: N/A

"""

#libraries
import threading
#classes

#functions

def repeat(code, seconds):
    """
this function repeats certain code on a timer, it takes two parameters:
code, the code to be repeated
seconds, the time, in seconds, that the function should wait before repeating
    """
    exec(code)
    threading.Timer(seconds, lambda:repeat(code, seconds)).start()

#main

if(__name__ == "__main__"):
    #testing
    repeat("print('it has been 3 seconds')", 3)
