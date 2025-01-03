import turtle
import time

canvas = turtle.Screen()
turtle = turtle.Turtle()
canvas.setup(500, 500)
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

#set the pen color to green
turtle.color("green")

#set the fil color to blue
turtle.fillcolor("blue")

#begin filling the shape
turtle.begin_fill()

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

#Draw a triangle
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.penup()
turtle.goto(-100, 200)
turtle.pendown()


#draw circle
for i in range(360):
    turtle.forward(1)
    turtle.right(1)

turtle.end_fill()
time.sleep(10)
turtle.reset()

#activity 2: Polygon generator

canvas.setup(500, 500)
canvas.title("Polygon Generator")
length = int(input("Enter the length of the polygon side: "))
num_sides = int(input("Enter the number of sides: "))
angle = 360 / num_sides
for i in range(num_sides):
    turtle.forward(length)
    turtle.right(angle)
time.sleep(10)
