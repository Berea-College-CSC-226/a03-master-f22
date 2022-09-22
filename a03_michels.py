import turtle

wn = turtle.Screen()
wn.bgcolor("cyan")
tree = turtle.Turtle()


def morne(incon):
    tree.color("green")
    tree.speed(70)
    tree.penup()
    tree.goto(-800, 0)
    tree.pendown()
    tree.fillcolor("green")
    tree.begin_fill()
    for i in range(5):
        for i in range(11):
            tree.forward(10)
            tree.left(5)

        for i in range(22):
            tree.forward(12)
            tree.right(5)

        for i in range(10):
            tree.forward(10)
            tree.left(5)

    tree.right(90)
    tree.forward(4000)
    tree.goto(-800, 0)
    tree.end_fill()
    return



johns=turtle.Turtle()
johns.penup()
johns.goto(-100, -100)
johns.pendown()
johns.left(90)

def building(tortue, hauteur):
    tortue.forward(hauteur)
    tortue.right(90)
    tortue.forward(20)
    tortue.left(90)

    tortue.end_fill()
    return




kay = turtle.Turtle()

def construction(valpa):
    valpa.penup()
    valpa.goto(-500, -300)
    valpa.pendown()
    valpa.forward(50)
    valpa.left(90)
    valpa.forward(200)
    valpa.fillcolor("brown")
    valpa.begin_fill()
    valpa.left(90)
    valpa.forward(70)
    valpa.left(-135)
    valpa.forward(130)
    valpa.right(45)
    valpa.forward(300)
    valpa.right(45)
    valpa.forward(130)
    valpa.right(135)
    valpa.goto(-500, -100)
    valpa.end_fill()
    valpa.penup()
    valpa.goto(-500, -300)
    valpa.pendown()
    valpa.fillcolor("gray")
    valpa.begin_fill()
    valpa.forward(-400)
    valpa.right(90)
    valpa.forward(200)
    valpa.left(90)
    valpa.forward(360)
    valpa.left(90)
    valpa.forward(200)
    valpa.end_fill()

michel = turtle.Turtle()
michel.pensize(1)


turtle.colormode(255)
def window(tort):
    tort.pencolor(0, 0, 128)
    tort.fillcolor(0, 0, 128)
    tort.begin_fill()
    tort.forward(20)
    tort.left(90)
    tort.end_fill()
    return

def initial(gang, xn, yn):
    gang.pensize(2)
    gang.color("white")
    gang.penup()
    gang.goto(xn, yn)
    gang.pendown()
    return



def main():
    hauteur = [100, 50, 20, 10, -35, -45, -200]
    for xs in hauteur:
        building(johns, xs)

    morne(tree)
    construction(kay)
    xn = -470
    for i in range(4):
        yn = -90
        xn = xn + 70
        for i in range(4):
            yn = yn - 42
            initial(michel, xn, yn)
            for i in range(4):
                window(michel)




main()

turtle.done()