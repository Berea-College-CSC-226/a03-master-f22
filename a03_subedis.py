#Shidartha Subedu
#Username- Shidartha1
#Repo link - https://github.com/Berea-College-CSC-226/a03-master-f22.git
#Google Doc -https://docs.google.com/document/d/1qXlDsPViiKJjbj_CfzpLxdugGlLMePXoc9WpAfjJLPw/edit?usp=sharing


import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.bgcolor("lightblue")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.speed(10)

jeff = turtle.Turtle()
jeff.shape("turtle")
jeff.color("blue")
jeff.speed(10)

jim = turtle.Turtle()
jim.shape("turtle")
jim.color("green")
jim.speed(10)

son = turtle.Turtle()
son.shape("turtle")
son.color("yellow")
son.speed(10)



tess.penup()
tess.size = 10
tess.pensize(10)
tess.setpos(-250, 100)

def make_house():
    for i in range(2):
        tess.pendown()
        tess.forward(200)
        tess.right(90)
        tess.forward(200)
        tess.right(90)

jeff.penup()
jeff.size = 5
jeff.pensize(5)
jeff.speed(10)
jeff.setpos(-225, 50)

def make_window():
    for i in range(2):
        jeff.pendown()
        jeff.begin_fill()
        jeff.forward(35)
        jeff.right(90)
        jeff.forward(35)
        jeff.right(90)
        jeff.end_fill()
        jeff.penup()

def make_door():
    for i in range(2):
        jeff.pendown()
        jeff.begin_fill()
        jeff.forward(35)
        jeff.right(90)
        jeff.forward(60)
        jeff.right(90)
        jeff.end_fill()

def make_roof():
    for i in range(1):
        tess.pendown()
        tess.begin_fill()
        tess.left(45)
        tess.forward(141)
        tess.right(90)
        tess.forward(141)
        tess.right(135)
        tess.forward(200)
        tess.end_fill()
jim.size = 5
jim.pensize(20)

def make_grass():
    for i in range(2):
        jim.pendown()
        jim.begin_fill()
        jim.forward(750)
        jim.right(90)
        jim.forward(200)
        jim.right(90)
        jim.end_fill()

def make_sun():
    for i in range(1):
        son.pendown()
        son.begin_fill()
        son.circle(40)
        son.end_fill()

def main():
    make_house()
    make_window()
    jeff.setpos(-115, 50)
    make_window()
    jeff.setpos(-150, -25)
    make_door()
    jeff.penup()
    jeff.setpos(-250, 100)
    make_roof()
    jim.penup()
    jim.setpos(-370, -110)
    make_grass()
    son.penup()
    son.setpos(250, 100)
    make_sun()





main()



wn.exitonclick()