#Elyse Randolph
#November 3 2024
#P4LAB1
#Program draws initals using turtle

import turtle
t = turtle.Turtle()
t.color("purple")
t.pensize(25)

for x in range(1,3):
    t.forward(50)
    t.left(180)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
t.forward(50)

t.penup()
t.forward(50)
t.pendown()
for x in range(1,5):
    t.forward(50)
    t.right(90)
t.right(90)
t.forward(100)
t.left(180)
t.forward(50)
t.right(130)
t.forward(70)
    
