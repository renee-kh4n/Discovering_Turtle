#code not mine, taken from: https://pythondex.com/awesome-python-turtle-codes#google_vignette 

import turtle

turtle.title("rainbow spiral")

turtle.Screen().bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
r,g,b=255,0,0

for i in range(255*2):
    turtle.colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    pen.forward(50+i)
    pen.right(91)
    pen.pencolor(r,g,b)

turtle.done()