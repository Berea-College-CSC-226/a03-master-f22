######################################################################
# Author: Mercy Eze
# Username: ezem
#
# Assignment: A03: Functional turtles
# Purpose: A program to understand the importance of functions. Draws a building on grass colored ground and night sky
#
# Google Doc Address: https://docs.google.com/document/d/1VTr6BcgH5Qoi3HjPv-ldchPZL2UAyOanLNxKO5kNF4Y/edit?usp=sharing
######################################################################

import turtle

def draw_rectangle(t, w, h):
    """
    A function to draw all rectangular parts of building
    """
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()



def draw_house(t,x,y):
    """
    Draws buidling structure
    """
    t.penup()
    t.goto(x,y)
    t.fillcolor(191, 128, 6)
    t.begin_fill()
    draw_rectangle(t,400,300)
    t.end_fill()


def draw_roof(t, x, y):
    """
    Draws roof of building
    """
    t.goto(x, y)
    t.fillcolor(77, 50, 15)
    t.begin_fill()
    t.goto(x-20, y)
    t.goto(x, y+20)
    t.goto(x+400, y+20)
    t.goto(x+420, y)
    t.goto(x+420, y)
    t.end_fill()

# draw middle pointed part of roof
    t.begin_fill()
    t.goto(-100, 100)
    t.goto(0, 160)
    t.goto(100, 100)
    t.goto(-100, 100)
    t.end_fill()


def draw_outline(t2, w, h):
    """
     Function to draw outline on middle part of building to give it depth
    """
    # outline for house
    t2.color(0, 0, 0)
    t2.pensize(1)
    t2.goto(-100, 100)
    t2.pendown()
    t2.goto(0, 160)
    t2.goto(100, 100)
    t2.goto(-100, 100)

    # outline for roof
    for i in range(2):
        t2.forward(w)
        t2.right(90)
        t2.forward(h)
        t2.right(90)


def draw_openings(t, w, h):
    """
    A function to draw building openings (door & windows)
    """
    # draws rectangles for windows and doors (start)
    t.goto(-175, 50)
    draw_rectangle(t, w, h)

    t.goto(125, 50)
    draw_rectangle(t, w, h)

    t.goto(-25, 50)
    draw_rectangle(t, w, h)

    t.goto(-40, -90)
    draw_rectangle(t, 80, 110)
    # draws rectangles for windows and doors (end)


def main():
    """
    Execute the whole program with set algorithm
    """
    # Create a screen
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(24,6,95)

    # Create and set turtle
    tess = turtle.Turtle()
    tess.penup()
    tess.goto(-400,-100)
    tess.speed(-1)
    tess.pendown()

    tess.fillcolor(0, 71, 0)
    draw_rectangle(tess, 1000, 600)  # calls draw_rectangle function to draw ground

    draw_house(tess, -200, 100)    # calls draw_house function to draw house

    draw_roof(tess, -200, 100)     # calls draw_roof function to draw roof of house

    tots = turtle.Turtle()        # create and set a different turtle for building outline
    tots.penup()
    draw_outline(tots, 200, 300)

    draw_openings (tess, 50, 65)   # calls draw_opening function to draw windows and door

    tess.hideturtle()
    tots.hideturtle()

    window.exitonclick()


main()


