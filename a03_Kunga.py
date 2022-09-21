import turtle

turtle.colormode(255)

print("")

def buildings(building):
    """

    : building: this draws four twin skyscrapers
    :return: none
    """
    building.color('blue')
    building.penup()
    building.setpos(120, -20)
    building.pendown()
    building.begin_fill()
    building.forward(255)
    building.left(180)
    building.forward(260)
    building.left(90)
    building.forward(300)
    building.left(90)
    building.forward(20)
    building.left(90)
    building.forward(280)
    building.right(90)
    building.forward(250)
    building.left(90)
    building.forward(20)
    building.end_fill()
    building.penup()
    building.setpos(134, -41)
    building.color('grey')
    building.pendown()
    building.begin_fill()
    building.right(90)
    building.forward(250)
    building.right(90)
    building.forward(300)
    building.right(90)
    building.forward(247.5)
    building.right(90)
    building.forward(280)
    building.end_fill()
    building.penup()
    building.setpos(-125, -20)
    building.color('orange')
    building.right(-180)
    building.pendown()
    building.begin_fill()
    building.forward(255)
    building.left(180)
    building.forward(255)
    building.left(90)
    building.forward(300)
    building.left(90)
    building.forward(20)
    building.left(90)
    building.forward(280)
    building.right(90)
    building.forward(290)
    building.left(90)
    building.forward(21)
    building.end_fill()
    building.penup()                # I made the code to where it looks like a mirror reflection
    building.setpos(-145, -42)
    building.color('blue')
    building.pendown()
    building.begin_fill()
    building.right(90)
    building.forward(280)
    building.right(90)
    building.forward(330)
    building.right(90)
    building.forward(282)
    building.right(90)
    building.forward(330)
    building.end_fill()
    building.penup()


def windows(glass):
    """

    glass: it creates the windows for the skyscrapers
    :return: none
    """
    glass.pensize(5)
    glass.pencolor(230, 102, 150)
    glass.fillcolor(170, 90, 220)               # the time I utilize the rgb function
    glass.penup()
    glass.setpos(171, -85)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()
    glass.penup()
    glass.setpos(171, -205)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()
    glass.penup()
    glass.setpos(-344, -85)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):                  # this is where I made the same eight windows with four on each skyscraper
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()
    glass.penup()
    glass.setpos(-344, -205)
    glass.pendown()
    glass.begin_fill()
    for i in range(2):
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.forward(45)
        glass.right(90)
        glass.penup()
        glass.forward(115)
        glass.pendown()
    glass.end_fill()




def make_text(john, txt):
    """
    Writes text to the screen.

    john : a Turtle object
    :return: None
    """
    john.color("blue")
    john.setpos(0, 260)
    john.write(txt, move=False, align='center', font=("italic", 20, ("bold", "normal")))


def main():
    """
    this draws every function in order of list
    :return: none
    """
    wn = turtle.Screen()
    wn.bgcolor("yellow")
    wn.title("city")
    john = turtle.Turtle()
    john.hideturtle()
    clouds = turtle.Turtle()
    clouds.hideturtle()
    building = turtle.Turtle()
    building.hideturtle()
    glass = turtle.Turtle()
    glass.hideturtle()
    web = turtle.Turtle()
    web.hideturtle()
    buildings(building)
    windows(glass)
    make_text(john, "City")            # text in turtle

    wn.exitonclick()

main()