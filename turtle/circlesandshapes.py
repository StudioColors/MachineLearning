import turtle
import math

def tast(x):
    R=25
    turtle.shape('turtle')
    turtle.speed(10)
    n=3
    for i in range(0,x):
        turtle.color("black")
        turtle.pendown()
        turtle.circle(R)
        a = 360/n
        S = R*2*math.sin(math.pi/n)
        for j in range(1,n+1):
            turtle.color("red")
            turtle.setheading(a*j-a/2)
            turtle.forward(S)
            turtle.setheading(a*j)
        turtle.penup()
        turtle.setpos(0.00 ,0.00 - R)
        R = R+25
        n=n+1

tast(7)
    


    

