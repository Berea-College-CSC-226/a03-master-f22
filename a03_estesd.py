#################################################################################
# Author: DJ Estes
# Username:estesd
#
# Assignment: A03
# Purpose: To cause conflict
# Google Doc Link: https://docs.google.com/document/d/12lZexEdof82gVZJcv1-DGpB_Y1tlBegZgsiD3QrKA2g/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
from random import randint


def vase():
    """
    This will create the vase for my picture
    """
dj = turtle.Turtle()
dj.color("yellow")
dj.pensize(20)
dj.penup()
dj.goto(450,300)
dj.pendown()
dj.begin_fill()
dj.circle(-100,360)
dj.end_fill()


    # ....


def flower2():
    """
    Docstring for function_2
    """
jc = turtle.Turtle()
jc.pencolor("orange")
jc.speed(10)
jc.pensize(15)
jc.penup()
for i in range(20):
    jc.pendown()
    jc.goto(randint(-550,700), randint(-550,700))
    jc.forward(randint(-200,200))
    jc.right(randint(-180,180))
    jc.forward(-200)

    # ...


def main():
    """
    Making my art picture
    """
    # ...
wg = turtle.Screen()
wg.bgcolor("light blue")
vase()            # Function call to vase():
flower2()         # Function call to flower2():
wg.exitonclick()

main()
