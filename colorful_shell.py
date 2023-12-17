#KHAN, Renee Althea F.
import turtle

pen = turtle.Turtle()
pen.shape("circle")
pen.color("white")

s = turtle.Screen()
s.bgcolor("black")

turtle.title("Shell")
pen.speed(0)
pen.hideturtle()
turtle.colormode(255)
r, g, b = 255, 0, 0
for i in range(5, 150):
    pen.color(r,g,b)
    pen.circle(i)
    pen.right(10)

    if b < 255:
        b += 3

    if b == 255 and r-3 > -1:
        r -= 3




turtle.done()

