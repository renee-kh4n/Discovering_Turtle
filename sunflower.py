# KHAN, Renee Althea F.

import turtle

pen = turtle.Turtle()

s = turtle.Screen()

s.bgcolor("black")

pen.speed(0)

def curve(length):
    for i in range(100):
        pen.left(1)
        pen.forward(length)


def petal():
    
    pen.color("yellow")
    curve(2)
    pen.left(75)
    curve(2)

pen.goto(18, 20)
for i in range(10):
    petal()
    pen.left(120)

pen.goto(0,0)
turtle.colormode(255)
pen.color(181, 101, 29)
for i in range(50):
    pen.circle(20)
    pen.left(10)


turtle.done()
