######################################################################
# Author: Easton Mason         TODO: Change this to your name, if modifying
# Username: masone3                  TODO: Change this to your username, if modifying
#
# Google Doc Link: https://docs.google.com/document/d/1o-DD_sso7X1Lzyg4ulpvtvCBHjpvTfT0pVIr9V1vAP4/edit?usp=sharing
#
# Assignment: A02: Loopy Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes
######################################################################
# Acknowledgements:
#
# originally created by Dr. Jan Pearce and Dr. Scott Heggen
#
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Dr. Jan Pearce - this file is modified from her original work
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle
turtle.colormode(255)  # change color modes

wn = turtle.Screen()  # Initializes the Screen object to draw on
wn.bgcolor(66, 245, 173)  # Sets background to a teal color

# List of turtles used to build the house
r = turtle.Turtle()
h = turtle.Turtle()
w1 = turtle.Turtle()
w2 = turtle.Turtle()
wf1 = turtle.Turtle()
wf2 = turtle.Turtle()
d = turtle.Turtle()

def build_roof():
    """
    Makes a triangular roof.

    :param r: a Turtle object
    :return: None
    """

    r.hideturtle() # Hides turtle
    r.pensize(20)

    r.color(120, 120, 120) # Makes the roof a light gray color

    r.penup()
    r.setpos(0, 70) # Sets position for roof
    r.pendown()

    r.begin_fill() # Starts the fill

    r.back(100)
    r.forward(200)

    r.left(120)
    r.forward(200)

    r.left(120)
    r.forward(200)

    r.end_fill() # Ends the fill

    pass

def build_house():
    """
    Makes a square body for the house.

    :param h: a Turtle object
    :return: None
    """

    h.hideturtle() # Hides turtle
    h.pensize(20)

    h.color(150, 10, 0)  # Makes the roof a brick red color

    h.penup()
    h.setpos(-100, 65)  # Sets position for the base of the house
    h.pendown()

    h.begin_fill() # Starts the fill

    h.forward(200)
    h.right(90)
    h.forward(200)
    h.right(90)
    h.forward(200)
    h.right(90)
    h.forward(200)

    h.end_fill() # Ends the fill

    pass

def build_windows():
    """
    Makes 2 windows.

    :param w1: a Turtle object
    :param w2: a Turtle object
    :return: None
    """

    # Makes first window for house
    w1.hideturtle() # Hides turtle
    w1.pensize(20)

    w1.color(120, 120, 120)  # Makes the first window a light gray color

    w1.penup()
    w1.setpos(-80, 0)  # Sets position for the base of the house
    w1.pendown()

    w1.begin_fill() # Starts the fill

    w1.forward(40)
    w1.right(90)
    w1.forward(40)
    w1.right(90)
    w1.forward(40)
    w1.right(90)
    w1.forward(40)
    w1.right(90)

    w1.end_fill() # Ends the fill

    # Makes second window for house
    w2.hideturtle() # Hides turtle
    w2.pensize(20)

    w2.color(120, 120, 120)  # Makes the second window a light gray color

    w2.penup()
    w2.setpos(80, 0)  # Sets position for the base of the house
    w2.pendown()

    w2.begin_fill()  # Starts the fill

    w2.back(40)
    w2.left(90)
    w2.back(40)
    w2.left(90)
    w2.back(40)
    w2.left(90)
    w2.back(40)
    w2.left(90)

    w2.end_fill() # Ends the fill


    pass

def build_windowframe():
    """
    Makes 2 window frames.

    :param wf1: a Turtle object
    :param wf2: a Turtle object
    :return: None
    """

    # Makes first window frame for house
    wf1.hideturtle() # Hides turtle
    wf1.pensize(10)

    wf1.penup()
    wf1.setpos(-85, 5)  # Sets position for the base of the house
    wf1.pendown()

    wf1.forward(50)
    wf1.right(90)
    wf1.forward(50)
    wf1.right(90)
    wf1.forward(50)
    wf1.right(90)
    wf1.forward(50)
    wf1.right(90)
    wf1.forward(25)
    wf1.right(90)
    wf1.forward(50)
    wf1.back(25)
    wf1.right(90)
    wf1.back(25)
    wf1.forward(50)

    # Makes second window frame for house
    wf2.hideturtle()
    wf2.pensize(10)

    wf2.penup()
    wf2.setpos(85, 5)  # Sets position for the base of the house
    wf2.pendown()

    wf2.back(50)
    wf2.left(90)
    wf2.back(50)
    wf2.left(90)
    wf2.back(50)
    wf2.left(90)
    wf2.back(50)
    wf2.left(90)
    wf2.right(90)
    wf2.forward(25)
    wf2.right(90)
    wf2.forward(50)
    wf2.back(25)
    wf2.right(90)
    wf2.back(25)
    wf2.forward(50)


    pass

def build_door():
    """
    Makes a rectangular door for the house.

    :param d: a Turtle object
    :return: None
    """

    d.hideturtle() # Hides turtle
    d.pensize(10)

    d.color(66, 45, 37) # Makes the door into a nice oak brown color

    d.penup()
    d.setpos(-25, -40)  # Sets position for the door
    d.pendown()

    d.begin_fill()  # Starts the fill

    d.forward(50)
    d.right(90)
    d.forward(100)
    d.right(90)
    d.forward(50)
    d.right(90)
    d.forward(100)

    d.end_fill()  # Ends the fill

    pass

# Runs all the functions that build the house
def main():
    """
    Runs all of the components of the house in order to build it.

    """


    build_roof()
    build_house()
    build_windows()
    build_windowframe()
    build_door()



    # Exits turtle program on click
    wn.exitonclick()
    pass


main()
