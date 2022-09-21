
#################################################################################
# Author: Andrea Maria Ola Mejicanos
# Username: olaa
#
# Assignment: A03
# Purpose: Learn more about github and turtles
# Google Doc Link: https://docs.google.com/document/d/1WuR25eMACasUy5ly7iKKFu9rJpgOwS2YfhSm11IcdRw/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle


def circleflowers(t):
    """
    Docstring circleflowers
    This function is intended to draw a backgroung flower in the design, by using circles of two sizes.
    """

    # ...
    for i in range(6):
        t.circle(120,95)
        t.circle(120,85)
        t.circle(60,95)
        t.circle(60, 170)
        t.circle(60, 95)
        t.circle(120, 85)
        t.circle(120, 95)
        t.left(60)


def honeycomb(t):
    """
    Docstring for function_2
    This second function has a purpose to draw a honey comb pattern using hexagons.
    """

    # ...
    for i in range (6):
        t.forward(50)
        t.left(60)

def wings(t):
    """
        Docstring for function_3
        This second function is supposed to draw the wings of the bee.
    """
    for i in range(1):
        t.left(180)
        t.right(30)
        t.forward(150)
        honeycomb(t)
        t.left(60)
        honeycomb(t)
        t.forward(50)
        t.left(120)
        t.forward(155)
        t.left(-152)
        t.forward(92)
        t.left(80)
        t.forward(50)
        t.left(125)
        t.forward(120)
        t.left(180)
        t.forward(120)
        t.left(130)
        t.forward(50)
        t.left(75)
        t.forward(99)

def wing2(t):
    """
            Docstring for function_4
            This second function is supposed to draw the second wing of the bee.
        """
    t.forward(45)

    t.right(-30)
    t.forward(150)
    t.right(120)
    honeycomb(t)
    t.left(-60)
    honeycomb(t)
    t.left(-60)
    t.forward(-50)
    t.left(60)
    t.forward(160)
    t.left(152)
    t.forward(97)
    t.left(-80)
    t.forward(50)
    t.left(-125)
    t.forward(120)
    t.left(180)
    t.forward(120)
    t.left(-130)
    t.forward(50)
    t.left(-75)
    t.forward(99)

def main():
    """
    Docstring for main: Here, all the parts of the bee are put toguether and the backdroung and details are set.
    """
    # Creation of turtles
    screen = turtle.Screen()
    bee = turtle.Turtle()
    flora=turtle.Turtle()
    tulip=turtle.Turtle()
    tess=turtle.Turtle()
    frida=turtle.Turtle()
    bee.speed(0)
    flora.speed(0)
    frida.speed(0)
    tulip.speed(0)
    tess.speed(0)
    #Call the first function, start drawing the background
    screen.bgcolor('#331900')
    flora.color('#99CCFF')
    flora.forward(22)
    circleflowers(flora)

    #Drawing the Bee
    #body
    tulip.pencolor('goldenrod')
    tulip.pensize(10)
    bee.pencolor('black')

    bee.color('goldenrod')
    bee.begin_fill()

    bee.pensize(10)

    bee.left(180)
    bee.left(30)
    bee.forward(50)

    bee.left(60)
    bee.forward(110)

    bee.right(-60)
    bee.forward(70)

    bee.left(60)
    bee.forward(70)

    bee.left(60)
    bee.forward(110)

    bee.left(60)
    bee.forward(50)

    bee.left(30)
    bee.forward(40)


    #head

    bee.left(180)
    honeycomb(bee)
    bee.end_fill()
    #wings

    wings(bee)
    wing2(tulip)

    # Black lines
    tess.penup()
    tess.left(180)
    tess.left(30)
    tess.forward(50)
    tess.left(60)
    tess.forward(10)
    tess.pendown()
    tess.pensize(20)
    tess.left(90)
    tess.color('black')

    tess.forward(120)

    tess.penup()

    tess.right(90)
    tess.forward(30)
    tess.right(90)
    tess.pendown()
    tess.pensize(20)

    tess.color('black')



    tess.forward(120)

    tess.penup()

    tess.right(90)
    tess.forward(-30)
    tess.right(90)
    tess.pendown()
    tess.pensize(20)

    tess.color('black')

    tess.forward(120)

    tess.penup()

    tess.right(90)
    tess.forward(30)
    tess.right(90)
    tess.pendown()
    tess.pensize(20)

    tess.color('black')

    tess.forward(120)

#Change background
    screen.bgcolor('#99CCFF')
    frida.pencolor('#331900')
    frida.penup()
    frida.pensize(5)
    frida.forward(20)
    frida.right(90)
    frida.forward(270)
    frida.pendown()
    honeycomb(frida)# Function call to function_2
    frida.left(120)
    honeycomb(frida)
    frida.left(120)
    honeycomb(frida)
    frida.forward(50)
    frida.right(60)
    honeycomb(frida)
    frida.forward(50)
    frida.right(60)
    honeycomb(frida)
    frida.forward(50)
    frida.right(60)
    honeycomb(frida)
    frida.forward(50)
    frida.right(60)
    honeycomb(frida)
    frida.forward(50)
    frida.right(60)
    honeycomb(frida)

    turtle.exitonclick()
main()
