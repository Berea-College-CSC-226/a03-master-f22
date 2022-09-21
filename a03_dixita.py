
#################################################################################
# Author:Anupriya Dixit
# Username: dixita
#
# Assignment: A03
# Purpose:
# Google Doc Link:https://docs.google.com/document/d/1W4iI9CVKjUvOkS0H_6SpX3ix9gOI5fasaZY_HmKlHlo/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('#f08080')


def ocean():
    """
       Makes an ocean using different shades of orange and blue
        """
    t.pensize(50)
    t.up()
    t.setpos(-315, 50)
    t.down()
    for i in ('#FF0000','#8B4000', '#FF7F50','#DA70D6','#6A5ACD','#191970','#191970'):
         t.pencolor(i)
         t.forward(630)
         t.penup()
         t.forward(-630)
         t.right(90)
         t.forward(50)
         t.right(-90)
         t.pendown()
    t.penup()

def sun():
    """
        Makes a sun using three different shades of color
        """
    t.setpos(140,75)
    t.pensize(0)
    t.left(90)
    size=150
    place=155

    for i in ('orangered','darkorange','tomato'):
        t.setpos(place, 75)
        t.fillcolor(i)
        t.begin_fill()
        t.circle(size,180)
        t.end_fill()
        t.left(180)
        size = size// 2
        place= place//2


def boat(x,y):
    """
        Makes a boat
        """
    t.setpos(x,y)
    t.pendown()
    t.fillcolor(0,0,0)
    t.begin_fill()
    t.right(90)
    t.forward(300)
    t.left(45)
    t.forward(75)
    t.left(135)
    t.forward(405)
    t.left(135)
    t.forward(75)
    t.end_fill()
    t.penup()

def people():
    """
        Makes people on the boat
        """
    t.left(135)
    t.pencolor(0,0,0)
    t.pensize(15)
    for i in range(-180,120,40):
        t.setpos(i,-45)
        t.pendown()
        t.forward(20)
        t.right(90)
        t.circle(6, 360)
        t.penup()
        t.right(-90)

def boatpaddle():
    """
        Makes boat paddles
        """
    for x in (100,60,20, -180,-140,-100, -20, -60):
        t.setx(x)
        t.pensize(2)
        t.pendown()
        t.right(-145)
        t.forward(150)
        t.shape('arrow')
        t.left(180)
        t.stamp()
        t.forward(150)
        t.penup()
        t.left(35)


def main():
    """
        Makes the drawing
        """
    t.speed(0)
    ocean()
    sun()
    boat(-200,-100)
    people()
    boatpaddle()

main()


wn.exitonclick()

