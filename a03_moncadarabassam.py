# Michel Moncada moncadarabassam, https://docs.google.com/document/d/1heUL1h_w2XBbGpfoDPkpWXY_ID8Kib05DVTrHAi_eE0/edit?usp=sharing


import turtle
p = turtle.Turtle()
wn = turtle.Screen()


def function1():
    spiral.speed(10)
    spiral.goto(0,0)
    spiral.width(2)
    spiral.color("red")

    for i in range(500):  # this "for" loop will repeat these functions 500 times
        spiral.forward(i)
        spiral.left(91)
        pass


def main():
  wn.bgcolor("lightblue")
  spiral = turtle.Turtle()

  def eye(col, rad):
      p.down()
      p.fillcolor(col)
      p.begin_fill()
      p.circle(rad)
      p.end_fill()
      p.up()

# draw face
  p.width(4)
  p.fillcolor("yellow")
  p.begin_fill()
  p.circle(100)
  p.end_fill()
  p.up()

# draw eyes
  p.goto(-40, 120)
  eye('white', 15)
  p.goto(-37, 130)
  eye('black', 5)
  p.goto(40, 120)
  eye('white', 15)
  p.goto(37, 130)
  eye('black', 5)

# draw mouth
  p.goto(-40, 85)
  p.down()
  p.right(90)
  p.circle(40, 180)
  p.up()

# draw tongue
  p.goto(-10, 45)
  p.down()
  p.right(180)
  p.fillcolor("red")
  p.begin_fill()
  p.circle(10, 180)
  p.end_fill()


# it is made to create a spiral around the pacman face
def spiral():
    s = turtle.Turtle()
    wn = turtle.Screen()
    s.speed(10)
    s.goto(0,0)
    s.width(2)
    s.color("red")

    for i in range(500):  # this "for" loop will repeat these functions 500 times
        s.forward(i)
        s.left(91)





main()
spiral()
