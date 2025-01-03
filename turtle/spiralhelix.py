import turtle
import time

canvas = turtle.Screen()
canvas.bgcolor("white")
canvas.setup(600, 600)

turtle.title("Spiral Helix")
artist = turtle.Turtle()
artist.speed(100)

for i in range(90):
    for j in range(360):
        artist.forward(1)
        artist.right(1)
    artist.right(4)
artist.penup()
artist.goto(0, -400)
artist.pendown()
artist.write("Spiral Helix", move=False, align="center", font=("Arial", 20, "bold"))
artist.penup()
artist.goto(0, -420)
artist.pendown()
artist.write("by ammar", move=False, align="center", font=("Arial", 10, "normal", "italic"))
artist.hideturtle()
turtle.done()