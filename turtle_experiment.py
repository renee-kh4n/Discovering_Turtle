#KHAN, Renee Althea F.
import turtle

t = turtle.Turtle()
t.shape("circle")
t.color("white")

s = turtle.Screen()
s.bgcolor("black")

t.speed(2)

# BOX
dist = 10
p = 1
t.pensize(p)

while p<30:
    p += 1
    t.left(90)
    t.forward(dist)
    t.pensize(p)

    dist += 15  

turtle.delay(150)

t.clear()

turtle.delay(0)

# FLOWER
t.hideturtle()
t.penup()
t.goto(0, -5)
t.pendown()
t.pensize(1)

t.color("green")

count = 0
while count < 8:

    rad = 5
    t.circle(rad)
    while rad<100:
        rad += 5
        t.circle(rad)
    
    t.right(45)
    t.forward(1)
    count += 1

turtle.delay(150)

t.clear()

turtle.delay(0)

# SHELL
t.color("cyan")

rad = 1
while rad < 100:
    t.circle(rad)
    t.right(10)
    rad += 1

turtle.delay(150)

t.clear()

turtle.delay(0)

t.showturtle()
# HEART 
# bug: inverted heart (fixed, cause: initial position not taken into consideration)
t.shape("turtle")

t.color("pink")
t.fillcolor("white")
t.begin_fill()


t.penup()
t.goto(0, 0)
t.pendown()

t.right(140)
t.forward(113)


for i in range(200):
    t.left(1)
    t.forward(1)


t.right(120) 
for i in range(200):
    t.left(1)
    t.forward(1)

t.forward(112)
t.end_fill()

turtle.delay(200)

t.clear()

turtle.delay(0)

t.hideturtle()
turtle.hideturtle()
turtle.color("white")
turtle.write("Turtle is fun. . .", move=True, align="center", font=( "Arial", 15, "normal"))

turtle.done()