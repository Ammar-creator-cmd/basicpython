import turtle as t
t.title("panda")

turtle = t.Turtle()
screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("lightgray")

turtle.up()
turtle.setpos(0, 35)
turtle.down()

def draw_face(rad=50):
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fillcolor("white")
    turtle.circle(rad)
    turtle.end_fill()

def draw_circle(color, rad):
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(rad)
    turtle.end_fill()

def draw_ears():
  # Draw first ear
  turtle.up()
  turtle.setpos(-35, 95)
  turtle.down()
  draw_circle('black', 18)

  # Draw second ear
  turtle.up()
  turtle.setpos(35, 95)
  turtle.down()
  draw_circle('black', 18)

def draw_eyes_black():
    turtle.up()
    turtle.setpos(-20, 70)
    turtle.down()
    draw_circle('black', 10)

    turtle.up()
    turtle.setpos(20, 70)
    turtle.down()
    draw_circle('black', 10)

def draw_eyes_white():
    turtle.up()
    turtle.setpos(-20, 70)
    turtle.down()
    draw_circle('white', 5)

    turtle.up()
    turtle.setpos(20, 70)
    turtle.down()
    draw_circle('white', 5)

def draw_nose():
    turtle.up()
    turtle.setpos(0, 60)
    turtle.down()
    draw_circle('black', 5)

def draw_mouth():
    turtle.up()
    turtle.color("black")
    turtle.setpos(-5, 50)
    turtle.down()
    turtle.right(90)
    turtle.circle(5, 180)
    turtle.up()
    turtle.setpos(5, 50)
    turtle.down()
    turtle.left(360)
    turtle.circle(5, -180)
def draw_panda():
    draw_face()
    draw_ears()
    draw_eyes_black()
    draw_eyes_white()
    draw_nose()
    draw_mouth()
    turtle.hideturtle()

if __name__ == "__main__":
    draw_panda()
    t.done()

