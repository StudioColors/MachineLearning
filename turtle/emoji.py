import turtle
import math


turtle.speed(10)

turtle.shape('turtle')

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()

turtle.penup()
turtle.setpos(-70, 180)

turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.setpos(70, 180)

turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.setpos(0, 160)

turtle.width(30)

turtle.pendown()
turtle.right(90)
turtle.forward(50)

turtle.penup()
turtle.setpos(0, 50)

turtle.width(25)
turtle.color("red")

turtle.pendown()
turtle.right(270)
turtle.circle(90, 90)
turtle.right(180)

turtle.penup()
turtle.setpos(0, 50)

turtle.right(-270)
turtle.pendown()
turtle.circle(-90, 90)

turtle.penup()
turtle.setpos(0, -100)




    

