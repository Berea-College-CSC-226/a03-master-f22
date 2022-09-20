# This is a sample Python script.
#################################################################################
# Author: Bless Iteka
# Username:Itekab
#
# Assignment: a03: functional turtles
# Purpose: learn more about functions and using git hub
# Google Doc Link: https://docs.google.com/document/d/1UxgqWoiPeY33pZSU195gzhnM_nKpCbBLP9B87UYdKRI/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
wn = turtle.Screen()
sun = turtle.Turtle()
house = turtle.Turtle()
grass = turtle.Turtle()
roof = turtle.Turtle()
eye1 = turtle.Turtle()
eye2 = turtle.Turtle()
smile = turtle.Turtle()
cloud = turtle.Turtle()

wn.bgcolor("#BFEFFF")
sun.color("#FFEC8B")
house.color("#F5F5DC")
grass.color("#66CD00")
roof.color("#A0522D")
eye1.color("#ffffff")
eye2.color("#FFCCFF")
cloud.color("#ffffff")

sun.speed(10)
house.speed(10)
grass.speed(10)
roof.speed(10)
eye1.speed(10)
eye2.speed(10)
smile.speed(10)
cloud.speed(10)



def here_comes_the_sun():
    sun.penup()
    for x in range(2):
        sun.left(90)
        sun.forward(300)
    sun.pendown()
    sun.fillcolor("#FFEC8B")
    sun.begin_fill()
    for x in range(8):
        sun.circle(25)
        sun.left(45)
    sun.end_fill()
    pass
    #this function makes the sun

def and_the_green_grass_grew_all_around():
    grass.penup()
    grass.right(90)
    grass.forward(150)
    grass.right(90)
    grass.forward(800)
    grass.left(180)
    grass.pendown()
    grass.fillcolor("#66CD00")
    grass.begin_fill()
    for x in range(4):
        grass.forward(1600)
        grass.right(90)
    grass.end_fill()
    pass
#this function makes the grass

def welcome_home():
    house.penup()
    house.fillcolor("#F5F5DC")
    house.begin_fill()
    house.left(90)
    house.forward(100)
    house.pendown()
    house.right(180)
    for x in range(4):
        house.forward(250)
        house.right(90)
    house.end_fill()
    pass
    #this function makes the house

def raise_the_roof():
    roof.penup()

    roof.left(90)
    roof.forward(100)
    roof.left(90)
    roof.fillcolor("#A0522D")
    roof.begin_fill()
    roof.pendown
    roof.forward(250)
    roof.right(135)
    roof.forward(175)
    roof.right(90)
    roof.forward(175)
    roof.end_fill()
    pass
    #this function makes the roof

def open_your_eyes():
    eye1.penup()
    eye1.backward(50)
    eye1.fillcolor("#FFFFFF")
    eye1.begin_fill()
    for x in range(2):
        eye1.circle(45)
        eye1.backward(150)
    eye1.end_fill()
    pass
    #this function makes the eyes

def iris():
    eye2.penup()
    eye2.backward(50)
    eye2.fillcolor("#FFCCFF")
    eye2.begin_fill()
    for x in range(2):
        eye2.circle(25)
        eye2. backward(150)
    eye2.end_fill()
    pass
    #this function makes the irises

def say_cheese():
    smile.penup()
    smile.backward(225)
    smile.right(90)
    smile.forward(30)
    #smile.left(10)
    smile.pendown()
    smile.fillcolor("#000000")
    smile.begin_fill()
    for x in range(1):
        smile.circle(100,180)
    smile.end_fill()
    pass
    #this function makes the mouth

def cloudy_day():
    cloud.penup()
    cloud.left(90)
    cloud.forward(250)
    cloud.fillcolor()
    cloud.begin_fill()
    cloud.pendown()
    for x in range(8):
        cloud.circle(40)
        cloud.right(45)
        cloud.forward(10)
    cloud.end_fill()
    cloud.penup()
    cloud.right(90)
    cloud.forward(150)
    cloud.pendown()
    pass
    #this function makes the cloud

def quote():
    turtle.write("✨Welcome home✨")
    pass
    #this funciton writes the text

def main():
    here_comes_the_sun()
    and_the_green_grass_grew_all_around()
    welcome_home()
    raise_the_roof()
    open_your_eyes()
    iris()
    say_cheese()
    quote()
    cloudy_day()

main()

wn.exitonclick()
