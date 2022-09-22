######################################################################
# Author: Michael Tsige
# Username: tsigem
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: is used to practice how to effectively use functions.
######################################################################


import turtle

def house_body(wn, jess):
    jess.penup()
    jess.setpos(-100, -200)
    jess.pendown()

    jess.color("#a52a2a")
    jess.begin_fill()
    for i in range(2):
        jess.forward(200)
        jess.left(90)
        jess.forward(250)
        jess.left(90)
    jess.end_fill()
    print(jess.pos())


def house_roof(wn, jess):
    jess.penup()
    jess.setpos(-100, 50)
    jess.pendown()
    jess.left(60)


    jess.color("gray")
    jess.begin_fill()
    for i in range(3):
        jess.forward(200)
        jess.right(120)
    jess.end_fill()


def house_door(wn, jess):
    jess.penup()
    jess.setpos(-30, -200)

    jess.right(60)
    jess.color('gray')
    jess.begin_fill()
    for i in range(2):
        jess.forward(60)
        jess.left(90)
        jess.forward(120)
        jess.left(90)
    jess.end_fill()

def house_window(wn, jess):
    jess.penup()
    jess.setpos(0, 0)
    jess.pendown()

    jess.color('#000000')
    for i in range(20):
        jess.forward(18)
        jess.left(18)
        jess.left(90)
        jess.forward(30)

        jess.backward(30)
        jess.right(90)

def house_tree(wn, jess):
    jess.penup()
    jess.setpos(-300, -200)
    jess.pendown()

    jess.color('#a52a2a')
    jess.begin_fill()
    for i in range(2):
        jess.forward(30)
        jess.left(90)
        jess.forward(70)
        jess.left(90)
    jess.end_fill()

    jess.setpos(-300, -150)
    jess.color('#00FF00')
    jess.shape("circle")
    jess.shapesize(10, 5, 2)
    jess.begin_fill()
    for i in range(20):
        jess.forward(30)
        jess.left(18)
    jess.end_fill()



def main():
    turtle.colormode(255)
    wn = turtle.Screen()
    jess = turtle.Turtle()
    jess.hideturtle()

    wn.bgcolor('#ffff00')

    house_body(wn, jess)
    house_roof(wn, jess)
    house_door(wn, jess)
    house_tree(wn, jess)
    house_window(wn, jess)

    wn.exitonclick()

main()
