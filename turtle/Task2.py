import turtle
import time

canvas = turtle.Screen()
turtle = turtle.Turtle()
canvas.setup(500, 500)

length = int(input("Enter the length of the cube/ cuboid side: "))
width = int(input("Enter the width of the cube/ cuboid side: "))
height = int(input("Enter the height of the cube/ cuboid side: "))
turtle.color("black")
for i in range(2):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
turtle.penup()
turtle.goto(-72, 72)
turtle.pendown()
for i in range(2):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
turtle.penup()
turtle.goto(0, 0)
turtle.right(225)
turtle.pendown()
for i in range(2):
    turtle.forward(width)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
for i in range(2):
    turtle.forward(width)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
time.sleep(10)
