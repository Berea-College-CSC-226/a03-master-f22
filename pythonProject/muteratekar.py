
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(('PyCharm'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Name: Clarisse Muterateka

# Purpose: Draw a cute beach house on green grass with a circular window and a broken down door.

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
cal = turtle.Turtle()
cal.color('White')
cal.shape("classic")
cal.setpos(-310, 20)
cal.pensize(15)
cal.speed(7)

def land_and_sand():                    #This function draws the grass for the house.
  for i in range(2):
      cal.color("green")
      cal.begin_fill()
      cal.forward(750)
      cal.right(90)
      cal.forward(300)
      cal.right(90)
      cal.end_fill()

pat=turtle.Turtle()
pat.color("orange")
pat.pensize(15)
pat.setpos(70, -120)

def draw_house():                              #Draws a house without a roof.
  for i in range(1):
      pat.begin_fill()

      pat.left(90)
      pat.forward(200)
      pat.left(90)
      pat.forward(350)
      pat.left(90)
      pat.forward(200)
      pat.end_fill()


hank=turtle.Turtle()
hank.color("brown")
hank.pensize(15)

def raise_the_roof():              #Draws a roof for the house.

  hank.penup()
  hank.forward(66)
  hank.left(90)
  hank.forward(90)

  hank.pendown()
  hank.begin_fill()
  hank.left(45)
  hank.forward(70)
  hank.left(45)
  hank.forward(250)
  hank.left(45)
  hank.forward(70)
  hank.end_fill()

will=turtle.Turtle()
will.penup()
will.color("brown")
will.setpos(10, -27)
will.pendown()

def draw_window():                                #Draws the circular window.
  for x in range(1):
      will.begin_fill()
      will.circle(50)
      will.end_fill()
      will.left(90)
      will.color("blue")

      will.pensize(15)
      will.forward(99)
      will.penup()
      will.setpos(55, 20)
      will.pendown()
      will.left(90)
      will.forward(90)

g=turtle.Turtle()
g.color("brown")
g.pensize(15)
g.penup()

g.setpos(-200, -118)
g.pendown()

def draw_broken_door():                   #Draws a door missing part of the the bottom right.
  for i in range(1):
      g.begin_fill()
      g.pendown()

      g.speed(7)
      g.left(90)
      g.forward(120)
      g.right(90)
      g.forward(70)
      g.right(90)
      g.forward(120)
      g.right(180)
      g.forward(60)
      g.end_fill()


      g.end_fill()

y=turtle.Turtle()
y.color("white")
y.pensize(10)
y.shape("classic")

y.setpos(-145, -60)
y.speed(7)
def draw_doorknob():

  for i in range(10):
      y.begin_fill()
      y.circle(7)
      y.stamp()
      y.end_fill()

f=turtle.Turtle()



land_and_sand()
draw_house()
raise_the_roof()
draw_window()
draw_broken_door()
draw_doorknob()

wn.exitonclick()


