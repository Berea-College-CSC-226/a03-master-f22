######################################################################
# Author: Emmaley Powell
# Username: powelle
#
# Assignment: A02: Loopy Turtles
# Purpose: Create a more complex drawing using turtles
######################################################################
# Acknowledgements:
#
#
#
#
#
######################################################################
import turtle

#FUNCTIONS

def grass(ground):
    ground.penup()
    ground.backward(382)
    ground.right(90)
    ground.forward(50)
    ground.left(90)
    ground.pendown()

    ground.pencolor("LimeGreen")
    ground.fillcolor("LimeGreen")
    ground.begin_fill()
    ground.forward(757)
    ground.right(90)
    ground.forward(265)
    ground.right(90)
    ground.forward(757)
    ground.right(90)
    ground.forward(265)
    ground.end_fill()

def blue_sky(sky):
    sky.pencolor("DeepSkyBlue")
    sky.fillcolor("DeepSkyBlue")
    sky.begin_fill()
    sky.penup()
    sky.backward(382)
    sky.right(90)
    sky.forward(50)
    sky.left(90)
    sky.pendown()
    sky.forward(757)
    sky.left(90)
    sky.forward(375)
    sky.left(90)
    sky.forward(757)
    sky.left(90)
    sky.forward(375)
    sky.end_fill()

def cave_enterance(enter):
    enter.penup()
    enter.goto(229.00,-231.02)
    enter.pendown()
    enter.begin_fill()
    for x in range(90):
        enter.forward(1)
        enter.right(0.1)
    enter.setheading(90)
    enter.forward(200)
    enter.left(90)
    enter.forward(120)
    enter.left(90)
    enter.forward(180)
    enter.end_fill()

def mistake(filler):
    filler.pencolor(160,80,50)
    filler.fillcolor(160,80,50)
    filler.penup()
    filler.right(180)
    filler.forward(155)
    filler.left(90)
    filler.forward(140)
    filler.pendown()
    filler.begin_fill()
    filler.right(90)
    filler.forward(100)
    filler.left(90)
    filler.forward(20)
    filler.right(90)
    filler.forward(55)
    filler.left(90)
    filler.forward(95)
    filler.left(90)
    filler.forward(87)
    filler.right(90)
    filler.forward(15)
    filler.left(90)
    filler.forward(2)
    filler.left(53)
    filler.forward(145)
    filler.left(90)
    filler.forward(30)
    filler.end_fill()

#DRAW BEAR BODY
def body(bear):
    bear.left(20)
    for x in range(90):
        bear.forward(1)
        bear.left(0.5)
    for x in range(55):
        bear.forward(1)
        bear.left(1)
    for x in range(30):
        bear.forward(2)
        bear.left(0.5)
    for x in range(18):
        bear.forward(2)
        bear.left(2.1)
    for x in range(15):
        bear.forward(1)
        bear.right(2)
    for x in range(40):
        bear.forward(1)
        bear.left(0.8)

    bear.left(150)
    bear.forward(10)
    bear.right(180)
    bear.forward(10)

    for x in range(60):
        bear.forward(1)
        bear.left(2)
    for x in range(15):
        bear.forward(1)
        bear.left(1)
    for x in range(14):
        bear.forward(1)
        bear.right(1.5)
    bear.right(5)
    bear.forward(50)
    for x in range(95):
        bear.forward(0.5)
        bear.left(2)
    bear.right(13)
    bear.forward(70)

    bear.penup()
    bear.right(130)
    bear.forward(172)
    bear.left(30)
    bear.pendown()
    bear.forward(7)

def foot(bear):
    for x in range(6):
        bear.forward(0.75)
        bear.right(10)
    bear.right(20)
    bear.forward(35)
    for x in range(20):
        bear.forward(1)
        bear.right(4)
    bear.right(15)
    bear.forward(10)
    for x in range(10):
        bear.forward(1)
        bear.right(2.5)

def leg(bear):
    bear.forward(2)
    bear.right(120)
    for x in range(15):
        bear.forward(1)
        bear.left(0.75)
    bear.right(180)
    for x in range(15):
        bear.forward(1)
        bear.right(0.75)
    for x in range(100):
        bear.forward(1)
        bear.right(1.5)
    bear.right(10)
    bear.forward(27)
    bear.right(180)
    bear.forward(24)

def arm(bear):
    for x in range(50):
        bear.forward(1)
        bear.right(1.7)
    for x in range(13):
        bear.forward(1)
        bear.right(0.3)
    for x in range(25):
        bear.forward(1)
        bear.right(0.2)

def small_arm(bear):
    bear.begin_fill()
    bear.forward(20)
    for x in range(41):
        bear.forward(1)
        bear.right(4)
    bear.end_fill()

def right_ear(bear):
    for x in range(20):
        bear.forward(1)
        bear.right(3)
    for x in range(30):
        bear.forward(1)
        bear.right(4)
    for x in range(10):
        bear.forward(1)
        bear.right(0.5)
    bear.left(50)
    for x in range(17):
        bear.forward(1)
        bear.left(0.5)
    for x in range(15):
        bear.forward(1)
        bear.right(3)

def snout(bear):
    bear.fillcolor("Burlywood")
    bear.begin_fill()
    bear.right(120)
    for x in range(12):
        bear.forward(2)
        bear.left(2.5)
    for x in range(25):
        bear.forward(1)
        bear.left(3.5)
    for x in range(7):
        bear.forward(2)
        bear.left(1.5)
    for x in range(15):
        bear.forward(1)
        bear.left(5)
    for x in range(15):
        bear.forward(1)
        bear.left(1)
    for x in range(13):
        bear.forward(1)
        bear.left(5)

    bear.left(110)
    bear.forward(17)
    bear.right(180)
    bear.forward(17)

    for x in range(22):
        bear.forward(1)
        bear.left(4)
    bear.left(100)
    bear.end_fill()

def nose(bear):
    bear.fillcolor("SaddleBrown")
    bear.begin_fill()
    for x in range(20):
        bear.forward(0.5)
        bear.right(2)
    for x in range(14):
        bear.forward(0.5)
        bear.right(7)
    for x in range(19):
        bear.forward(1)
        bear.right(7)
    for x in range(8):
        bear.forward(1)
        bear.right(11)
        bear.end_fill()

def left_ear(bear):
    bear.penup()
    bear.forward(50)
    bear.left(90)
    bear.forward(5)
    bear.right(90)
    bear.pendown()

    for x in range(20):
        bear.forward(1)
        bear.right(0.2)
    for x in range(16):
        bear.forward(1)
        bear.right(4)
    bear.forward(32)
    bear.left(40)

    for x in range(20):
        bear.forward(1)
        bear.right(3)
    for x in range(30):
        bear.forward(1)
        bear.right(4)
    for x in range(10):
        bear.forward(1)
        bear.right(0.5)

    bear.penup()
    bear.right(45)
    bear.forward(35)
    bear.left(90)
    bear.forward(5)

    bear.pendown()

def eyes(bear):
    bear.right(60)
    for x in range(28):
        bear.forward(0.5)
        bear.left(5)

    bear.penup()
    bear.right(81)
    bear.forward(15)
    bear.pendown()

    bear.right(60)
    for x in range(28):
        bear.forward(0.5)
        bear.left(5)

def right_claw(bear):
    bear.pensize(2)
    bear.right(25)

    for x in range(30):
        bear.forward(0.5)
        bear.right(2)

    bear.right(180)

    for x in range(30):
        bear.forward(0.5)
        bear.left(2)

def left_claw(bear):
    bear.pensize(2)

    for x in range(30):
        bear.forward(0.5)
        bear.left(2)

    bear.right(180)

    for x in range(30):
        bear.forward(0.5)
        bear.right(2)

def tail(bear):
    bear.fillcolor(160,80,50)
    bear.begin_fill()
    bear.left(110)
    bear.pensize(0)
    for x in range(20):
        bear.forward(1)
        bear.left(1)
    for x in range(30):
        bear.forward(0.5)
        bear.left(2)
    for x in range(12):
        bear.forward(0.5)
        bear.left(7)
    for x in range(15):
        bear.forward(1)
        bear.right(0.3)
    bear.end_fill()
def large_stone(cave):
    cave.fillcolor("gray")
    cave.begin_fill()
    for x in range(130):
        cave.forward(1)
        cave.left(0.5)
    for x in range(30):
        cave.forward(0.5)
        cave.right(1)
    for x in range(40):
        cave.forward(0.75)
        cave.left(2)
    for x in range(10):
        cave.forward(1)
        cave.left(0.2)
    for x in range(30):
        cave.forward(0.75)
        cave.right(4)
    cave.left(30)
    for x in range(135):
        cave.forward(1)
        cave.left(0.3)
    for x in range(25):
        cave.forward(0.75)
        cave.left(3)
    cave.left(25)
    for x in range(140):
        cave.forward(1)
        cave.left(0.2)
    cave.setheading(270)
    cave.forward(30)
    cave.left(90)
    cave.forward(5)
    cave.right(90)
    cave.forward(10)
    cave.left(90)
    for x in range(110):
        cave.forward(1)
        cave.left(0.2)
    for x in range(10):
        cave.forward(1)
        cave.right(0.5)
    cave.left(90)
    for x in range(125):
        cave.forward(1)
        cave.right(0.2)
    for x in range(70):
        cave.forward(1)
        cave.right(1)
    for x in range(50):
        cave.forward(1)
        cave.right(0.2)
    cave.left(139)
    cave.forward(137)
    cave.end_fill()

def fourth_stone(cave):
    cave.fillcolor("Gray")
    cave.begin_fill()
    for x in range(110):
        cave.forward(1)
        cave.right(0.3)
    for x in range(27):
        cave.forward(0.5)
        cave.right(4)
    cave.left(30)
    for x in range(20):
        cave.forward(1)
        cave.right(2)
    for x in range(55):
        cave.forward(0.5)
        cave.left(1)
    for x in range(25):
        cave.forward(1)
        cave.right(0.1)
    cave.setheading(0)
    cave.forward(75)
    cave.right(90)
    cave.forward(105)
    cave.end_fill()

def third_stone(cave):
    cave.fillcolor("DarkGray")
    cave.begin_fill()
    cave.right(180)
    cave.forward(90)
    cave.pencolor("black")
    cave.left(110)
    for x in range(80):
        cave.forward(1)
        cave.right(0.6)
    for x in range(20):
        cave.forward(1)
        cave.right(5)
    cave.left(30)
    for x in range(55):
        cave.forward(1)
        cave.right(0.2)
    cave.setheading(0)
    cave.forward(69)
    cave.right(90)
    cave.forward(75)
    cave.end_fill()

def first_stone(cave):
    cave.fillcolor("DimGray")
    cave.begin_fill()
    cave.forward(25)
    for x in range(22):
        cave.forward(2)
        cave.left(3)
    for x in range(45):
        cave.forward(1)
        cave.left(0.1)
    for x in range(24):
        cave.forward(1)
        cave.right(3)
    for x in range(50):
        cave.forward(1)
        cave.left(0.85)
    cave.right(10)
    for x in range(7):
        cave.forward(6)
        cave.left(1)
    for x in range(22):
        cave.forward(1)
        cave.left(2)
    cave.right(10)
    for x in range(55):
        cave.forward(1)
        cave.left(0.5)
    for x in range(15):
        cave.forward(1)
        cave.left(7)
    cave.right(10)
    for x in range(80):
        cave.forward(1.5)
        cave.right(0.75)
    for x in range(25):
        cave.forward(1)
        cave.left(3)
    cave.right(20)
    for x in range(30):
        cave.forward(1)
        cave.left(0.2)
    for x in range(20):
        cave.forward(1)
        cave.left(3)
    cave.forward(17)
    cave.setheading(90)
    cave.forward(50)
    cave.forward(50)
    cave.forward(50)
    cave.forward(44)
    cave.end_fill()

def second_stone(cave):
    cave.fillcolor("LightGray")
    cave.begin_fill()
    cave.forward(110)
    cave.right(90)
    for x in range(60):
        cave.forward(1)
        cave.left(0.1)
    for x in range(35):
        cave.forward(0.75)
        cave.right(3)
    cave.left(10)
    for x in range(75):
        cave.forward(1)
        cave.left(0.1)
    cave.end_fill()

def tiny_stone(cave):
    cave.fillcolor("DimGray")
    cave.begin_fill()
    for x in range(50):
        cave.forward(1)
        cave.left(0.2)
    for x in range(20):
        cave.forward(1)
        cave.left(2)
    for x in range(45):
        cave.forward(1)
        cave.right(0.1)
    for x in range(20):
        cave.forward(1)
        cave.left(5)
    cave.left(20)
    for x in range(90):
        cave.forward(1)
        cave.left(0.2)
    for x in range(15):
        cave.forward(1)
        cave.left(5)
    for x in range(50):
        cave.forward(1)
        cave.left(0.2)
    for x in range(41):
        cave.forward(0.5)
        cave.left(1.5)
    cave.end_fill()


def main():
    wn = turtle.Screen()

    bear = turtle.Turtle()
    filler = turtle.Turtle()
    ground = turtle.Turtle()
    sky = turtle.Turtle()
    cave = turtle.Turtle()
    enter = turtle.Turtle()

    enter.hideturtle()
    ground.hideturtle()
    sky.hideturtle()
    filler.hideturtle()
    cave.hideturtle()
    bear.hideturtle()

    turtle.colormode(255)

    grass(ground)
    blue_sky(sky)
    mistake(filler)
    cave_enterance(enter)

    # POSITION TURTLE FOR BEAR
    bear.penup()
    bear.right(90)
    bear.forward(164)
    bear.right(90)
    bear.forward(141)
    bear.right(90)
    bear.pendown()

    bear.fillcolor(160, 80, 50)
    bear.begin_fill()
    body(bear)

    # FOOT
    foot(bear)

    # LEG
    leg(bear)

    # ARM 2
    arm(bear)

    bear.end_fill()

    bear.penup()
    bear.right(60)
    bear.forward(7)
    bear.left(90)
    bear.forward(15)
    bear.pendown()
    bear.right(25)

    # SMALL ARM
    small_arm(bear)

    bear.penup()
    bear.left(45)
    bear.forward(95)
    bear.right(90)
    bear.forward(27)
    bear.left(70)
    bear.pendown()

    # HEAD
    # RIGHT EAR
    right_ear(bear)

    # SNOUT
    snout(bear)

    # NOSE
    nose(bear)

    # LEFT EAR
    left_ear(bear)

    # EYES
    eyes(bear)

    bear.penup()
    bear.right(92)
    bear.backward(6)
    bear.right(90)
    bear.forward(79)

    bear.left(105)

    bear.pendown()
    # CLAWS (going right)

    right_claw(bear)
    bear.penup()
    bear.right(125)
    bear.forward(7)
    bear.right(30)
    bear.pendown()
    right_claw(bear)
    bear.penup()
    bear.right(125)
    bear.forward(7)
    bear.right(30)
    bear.pendown()
    right_claw(bear)

    bear.penup()
    bear.left(10)
    bear.forward(30)
    bear.left(90)
    bear.forward(21)
    bear.pendown()
    bear.right(45)

    # CLAWS (going left)

    left_claw(bear)
    bear.penup()
    bear.left(125)
    bear.forward(7)
    bear.left(45)
    bear.pendown()
    left_claw(bear)
    bear.penup()
    bear.left(125)
    bear.forward(7)
    bear.left(45)
    bear.pendown()
    left_claw(bear)

    bear.penup()
    bear.left(63)
    bear.forward(183)
    bear.right(90)
    bear.forward(73)
    bear.pendown()

    # TAIL
    tail(bear)

    cave.penup()
    cave.forward(375)
    cave.left(90)
    cave.forward(170)
    cave.left(90)
    cave.forward(194)
    cave.left(90)
    cave.forward(146)
    cave.right(90)
    cave.pendown()

    large_stone(cave)
    cave.penup()
    cave.goto(375.00, -290.00)
    cave.pendown()
    cave.setheading(180)
    fourth_stone(cave)
    third_stone(cave)

    cave.right(180)
    cave.forward(185)
    cave.right(180)

    second_stone(cave)
    cave.penup()
    cave.setheading(90)
    cave.forward(215)
    cave.right(90)
    cave.forward(81)
    cave.right(180)
    cave.pendown()

    first_stone(cave)

    cave.penup()
    cave.goto(120.00, -182.00)
    cave.setheading(180)
    cave.pendown()
    tiny_stone(cave)

    wn.exitonclick()

main()