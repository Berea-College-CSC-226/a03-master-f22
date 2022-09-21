######################################################################
# Author: Melany Casanova-Maldonado
# Username: casanovamaldonadom
# Assignment: A03: A Pair of Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To create useful functions
# Google Doc Link: https://docs.google.com/document/d/1O4429F5CyyDgYA5l3CZfSW88ajpoBmokd15yLaS0NAg/edit?usp=sharing
######################################################################
import turtle  # allows us to use the turtles library

bird_turtle = turtle.Turtle()  # creates a turtle named bird_turtle
bird_turtle.shape('turtle')  # changes the turtle's shape to a turtle shape
bird_turtle.color('black')  # changes the turtle's color to black
bird_turtle.pensize(5)  # changes the writing size to 5
bird_turtle.speed(0)  # changes the turtle's speed to the maximum speed


def drawbird():

    """Uses two semicircles to create the birds in the sky."""

    bird_turtle.right(30)  # turns the turtle to the right 30 degrees
    bird_turtle.pendown()  # allows the turtle to write
    bird_turtle.circle(-50, 100)  # creates a semicircle
    bird_turtle.left(75)  # turns the turtle to the left 75 degrees
    bird_turtle.circle(-50, 100)  # creates a semicircle


def main():
    """Draws the sea, the sun, birds, and a sailboat against a blue background"""

    wn = turtle.Screen()  # creates a graphics window
    wn.bgcolor('#c4ebf8')  # changes window color to #c4ebf8

    water_turtle = turtle.Turtle()  # creates a turtle named water_turtle
    water_turtle.shape('turtle')  # gives turtle a turtle shape
    water_turtle.color('darkblue')  # gives the turtle a dark blue color
    water_turtle.speed(0)  # changes the turtle's speed to the maximum speed
    water_turtle.pensize(10)  # changes the writing size to 10

    water_turtle.penup()  # stops the turtle from writing
    water_turtle.right(90)  # turns the turtle right 90 degrees
    water_turtle.forward(170)  # moves the turtle forward 170 units
    water_turtle.pendown()  # allows the turtle to start writing again
    water_turtle.begin_fill()  # instructs the turtle to fill in the shape it is drawing
    water_turtle.left(90)  # turns the turtle left 90 degrees
    water_turtle.forward(350)  # moves the turtle forward 350 units
    water_turtle.right(180)  # turns the turtle right 180 degrees
    water_turtle.forward(710)  # moves the turtle forward 710 units

    water_turtle.left(90)  # turns the turtle left 90 degrees
    water_turtle.forward(160)  # moves the turtle forward 160 degrees
    water_turtle.left(90)  # turns the turtle left 90 degrees
    water_turtle.forward(710)  # moves the turtle forward 710 units
    water_turtle.left(90)  # turns the turtle left 90 degrees
    water_turtle.forward(160)  # moves the turtle forward 160 units
    water_turtle.end_fill()  # stops the turtle from being given the filling instructions
    water_turtle.hideturtle()  # hides the turtle from view

    bird_turtle.penup()  # stops the turtle from writing
    bird_turtle.left(90)  # turns the turtle left 90 degrees
    bird_turtle.forward(130)  # moves the turtle forward 130 units

    drawbird()  # calls the drawbird() function

    bird_turtle.penup()  # stops the turtle from writing
    bird_turtle.right(115)  # turns the turtle right 115 degrees
    bird_turtle.forward(420)  # moves the turtle forward 420 units
    bird_turtle.right(90)  # turns the turtle right 90 degrees

    drawbird()  # calls the drawbird() function

    bird_turtle.penup()  # stops the turtle from writing
    bird_turtle.right(22)  # turns the turtle 22 degrees to the right
    bird_turtle.forward(130)  # moves the turtle forward 130 unita
    bird_turtle.left(90)  # the turtle turned left 90 degrees
    bird_turtle.forward(250)  # turtle moves forward 250 degrees
    bird_turtle.left(90)  # turns turtle left 90 degrees

    drawbird()  # calls the drawbird() function

    bird_turtle.hideturtle()  # hides the turtle from view

    sun_turtle = turtle.Turtle()  # creates a turtle called sun_turtle
    sun_turtle.pensize(10)  # changes the writing size to 10
    sun_turtle.speed(0)  # changes the turtle's speed to maximum speed
    sun_turtle.color('#fdd102')  # changes turtle's color to #fdd102
    sun_turtle.shape('turtle')  # changes turtle's shape to turtle

    sun_turtle.penup()  # stops turtle from writing
    sun_turtle.left(90)  # turns turtle left 90 degrees
    sun_turtle.forward(220)  # moves turtle forward 220 units
    sun_turtle.right(90)  # turns turtle right 90 degrees
    sun_turtle.forward(300)  # moves turtle forward 300 units
    sun_turtle.begin_fill()  # instructs turtle to fill in shape it draws with color
    sun_turtle.pendown()  # allows the turtle to start writing again
    sun_turtle.circle(100)  # instructs turtle to draw a circle
    sun_turtle.end_fill()  # stops instructing the turtle to fill in the shapes it draws
    sun_turtle.hideturtle()  # hides the turtle from view

    boat_body_turtle = turtle.Turtle()  # creates a turtle named boat_body_turtle
    boat_body_turtle.color('#895009')  # changes turtle color to #895009
    boat_body_turtle.pensize(7)  # changes writing size to 7
    boat_body_turtle.speed(0)  # changes turtle's speed to maximum speed
    boat_body_turtle.shape('turtle')  # changes turtle;s shape to turtle

    boat_body_turtle.penup()  # stops the turtle from writing
    boat_body_turtle.right(90)  # turns the turtle right 90 degrees
    boat_body_turtle.forward(165)  # moves the turtle forward 165 units
    boat_body_turtle.right(90)  # turns the turtle right 90 degrees
    boat_body_turtle.forward(110)  # moves the turtle forward 110 units
    boat_body_turtle.pendown()  # allows the turtle to start writing again
    boat_body_turtle.begin_fill()  # instructs the turtle to fill in the shapes it draws with color
    boat_body_turtle.forward(170)  # moves the turtle forward 170 units
    boat_body_turtle.right(60)  # turns the turtle right 60 degrees
    boat_body_turtle.forward(94)  # moves the turtle forward 94 units
    boat_body_turtle.right(120)  # turns turtle right 120 degrees
    boat_body_turtle.forward(250)  # moves turtle forward 250 units
    boat_body_turtle.right(110)  # turns turtle right 110 degrees
    boat_body_turtle.forward(85)  # moves turtle forward 85 units
    boat_body_turtle.end_fill()  # stops instructing turtle to fill in the shapes it draws

    boat_body_turtle.penup()  # stops the turtle from writing
    boat_body_turtle.color('black')  # changes turtle color to black
    boat_body_turtle.right(70)  # turns the turtle 70 degrees to the right
    boat_body_turtle.forward(90)  # moves the turtle forward 90 degrees
    boat_body_turtle.right(90)  # turns the turtle to the right 90 degrees
    boat_body_turtle.forward(80)  # moves the turtle forward 80 degrees
    boat_body_turtle.pendown()  # allows the turtle to start writing again
    boat_body_turtle.forward(170)  # moves the turtke forward 170 units
    boat_body_turtle.penup()  # stops the turtle from writing

    boat_body_turtle.color('white')  # changes the turtle's color to white
    boat_body_turtle.right(130)  # turns the turtle 130 degrees to the right
    boat_body_turtle.pendown()  # allows the turtle to start writing again
    boat_body_turtle.begin_fill()  # instructs the turtle to fill in the shapes it draws
    boat_body_turtle.forward(170)  # moves the turtle forward 170 units
    boat_body_turtle.right(140)  # turns the turtle right 140 degrees
    boat_body_turtle.forward(130)  # moves the turtle forward 130 units
    boat_body_turtle.right(90)  # turns the turtle right 90 degrees
    boat_body_turtle.forward(110)  # moves the turtle forward 110 units
    boat_body_turtle.end_fill()  # stops instructing the turtle from filling in the shapes it draws
    boat_body_turtle.penup()  # stops the turtle from writing

    boat_body_turtle.right(180)  # turns the turtle right 180 degrees
    boat_body_turtle.forward(220)  # moves the turtle forward 220 units
    boat_body_turtle.right(90)  # turns the turtle right 90 degrees
    boat_body_turtle.color('black')  # makes the turtle black
    style = ('Bradley Hand', 20, 'bold')  # sets the font, its size, and makes it bold
    boat_body_turtle.write('Melany wuz heer', font=style, align='center')  # writes "Melany wuz heer" using the font
    # written above and centers the alignment of the text
    boat_body_turtle.hideturtle()  # hides the turtle from view

    wn.exitonclick()  # Closes the program when a user clicks in the window

main()  # calls the main() function
