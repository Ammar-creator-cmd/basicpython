import turtle as t

t.title("Pac-Man")

turtle = t.Turtle()
screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("white")

turtle.up()
turtle.setpos(0, -50)
turtle.down()

def draw_face(rad=100):
    turtle.penup()
    turtle.goto(80, 165)
    turtle.right(210)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(rad, 290)
    turtle.goto(30, 70)
    turtle.right(45)
    turtle.goto(80, 165)
    turtle.end_fill()

def draw_circle(color, rad):
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(rad)
    turtle.end_fill()

def draw_eyes_black():
    turtle.up()
    turtle.setpos(30, 135)
    turtle.down()
    draw_circle('black', 10)

def coin1():
    turtle.up()
    turtle.setpos(225, 100)
    turtle.down()
    draw_circle("yellow", 10)

def coin2():
    turtle.up()
    turtle.setpos(175, 100)
    turtle.down()
    draw_circle("yellow", 10)

def coin3():
    turtle.up()
    turtle.setpos(125, 100)
    turtle.down()
    draw_circle("yellow", 10)

def coin4():
    turtle.up()
    turtle.setpos(75, 100)
    turtle.down()
    draw_circle("yellow", 10)

def coins():
    coin1()
    coin2()
    coin3()
    coin4()

def draw_pac_man():
    draw_face()
    draw_eyes_black()
    coins()
    turtle.hideturtle()

if __name__ == "__main__":
    draw_pac_man()
    t.done()



