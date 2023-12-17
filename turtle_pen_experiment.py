# KHAN, Renee Althea F.
# learning python: turtle
# December 17, 2023 2:50pm - 3:05pm

# code from: https://www.youtube.com/watch?v=N1SXaowmTEM&list=PLxLRoXCDIaldQiNKMyuGfZPuNqeV6p-Bg



import turtle

t = turtle.Turtle()

s = turtle.Screen()

s.bgcolor("black") #screen background color

t.pencolor("cyan") #sets the line color

t.pensize(1) #sets the line's thickness

a = 0
b = 0

t.speed(0) #sets the drawing speed
t.penup()
t.goto(0, 200)
t.pendown()

while True:
    t.forward(a) # allows the pen to write froward
    # t.backward(a) --> allows the pen to write opposite the specified direction
    # a (argument) is the distance in pixels

    t.right(b) #sets the direction of the pen
    # t.left(b) --> turns the pen to the left
    # (argument) is the angle in degrees 


    #                  north (90 deg)
    #                       |
    #                       |
    #   (180 deg) west ------------ east (0 deg)
    #                       |
    #                       |
    #                  south (270 deg)
    
    a+=3
    b+=1

    if b==210:
        break
    t.hideturtle()

turtle.done()