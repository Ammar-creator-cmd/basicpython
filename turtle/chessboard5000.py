import turtle
import time

canvas = turtle.Screen()
artist = turtle.Turtle()
canvas.setup(400, 600)
turtle.title("Chessboard")
artist.speed(50)

for i in range(8):
    artist.penup()
    artist.goto(-100, i * 30)
    artist.pendown()
    for j in range(8):
        if (i + j) % 2 == 0:
           col = "black"
        else:
           col = "white"
        artist.fillcolor(col)
        artist.begin_fill()
        for _ in range(4): #draw a square
            artist.forward(30)
            artist.left(90)
        artist.forward(30)
        artist.end_fill()
artist.penup()
artist.goto(20, -50)
artist.pendown()
artist.write("Chessboard", move=False, align="center", font=("Arial", 20, "bold"))
artist.penup()
artist.goto(20, -70)
artist.pendown()
artist.write("by ammar", move=False, align="center", font=("Arial", 10, "normal", "italic"))
artist.hideturtle()
turtle.done()
time.sleep(10)
