# Author: Bishal Timalsina
# Username: timalsinab
#Assignment:A03
# google document link:https://docs.google.com/document/d/1nPnYo2oSViRl-FMzVC1zfp-ibYaHTY7O00mf7e0Uvkc/edit?usp=sharing

import turtle

def square(bishal, x,y):
    """I am making a function that makes a rectangle like a house."""
    for b in range(4):
        bishal.forward(x)
        bishal.left(y)

def traingle(bishal,x,y,z):
    for c in range(2):
        bishal.left(x)
        bishal.forward(y)
        bishal.right(z)
def circle(bishal,x):
    bishal.fillcolor("yellow")
    bishal.begin_fill()
    bishal.circle(x)
    bishal.end_fill()
def road(bishal,x,y):
    bishal.pensize(y)
    bishal.color("black")
    bishal.forward(x)
def main():
    turtle.colormode(255)
    wn = turtle.Screen()
    wn.bgcolor("sky blue")
    bishal = turtle.Turtle()
    bishal.color("red")
    bishal.penup()
    bishal.goto(-100, -100)
    bishal.pendown()
    bishal.speed(0)
    bishal.begin_fill()
    bishal.fillcolor("purple")
    square(bishal, 202, 90)
    bishal.end_fill()
    bishal.penup()
    bishal.goto(-100, 100)
    bishal.pendown()
    bishal.fillcolor("purple")
    bishal.begin_fill()
    traingle(bishal,30, 118, 90)
    bishal.end_fill()
    bishal.penup()
    bishal.goto(-60, 0)
    bishal.left(120)
    bishal.pendown()
    square(bishal,40, 90)
    bishal.penup()
    bishal.goto(0, 0)
    bishal.goto(30, 0)
    bishal.pendown()
    square(bishal,40, 90)
    bishal.penup()
    bishal.goto(0, 0)
    bishal.goto(-30, -100)
    bishal.pendown()
    square(bishal,70, 90)
    bishal.penup()
    bishal.goto(-180,270)
    bishal.pendown()
    circle(bishal,50)
    bishal.penup()
    bishal.goto(-750, -160)
    bishal.pendown()
    road(bishal,1500,4)
    bishal.penup()
    bishal.goto(0, 0)
    bishal.goto(-750, -260)
    bishal.pendown()
    road(bishal,1500,4)
    bishal.penup()
    bishal.goto(-180,-100)
    bishal.pendown()
    bishal.begin_fill()
    bishal.fillcolor("brown")
    square(bishal,50,90)
    bishal.end_fill()
    bishal.penup()
    bishal.goto(-180,-50)
    bishal.pendown()
    bishal.begin_fill()
    bishal.fillcolor("green")
    traingle(bishal,60,50,180)
    bishal.end_fill()
    bishal.penup()
    bishal.goto(-180,-10)
    bishal.left(-120)
    bishal.pendown()
    bishal.begin_fill()
    bishal.fillcolor("green")
    traingle(bishal,60,50,180)
    bishal.left(60)
    bishal.forward(50)
    bishal.end_fill()
    bishal.penup()
    bishal.goto(180,-90)
    bishal.left(180)
    wn.exitonclick()


main()
