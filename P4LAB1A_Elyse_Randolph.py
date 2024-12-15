#Elyse Randolph
#November 3 2024
#P4LAB1
#Program uses turtle to draw a square and triangle

import turtle


win = turtle.Screen()      
t = turtle.Turtle()    
x=1


for x in range (1,5):
    t.forward(50)          
    t.left(90)             
for x in range (1,4):
    t.forward(100)
    t.left(120)


win.mainloop()           
