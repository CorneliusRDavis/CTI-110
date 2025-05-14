#Davis ,Cornelius
#3/19/2025
#P4Lab1
#Turtle Graphics program to draw triagle and square

import turtle
win = turtle.Screen()
win.bgcolor('yellow')
ti = turtle.Turtle()

# Set the way ti looks

ti.pensize(4)  #how large line looks
ti.pencolor("Purple") #line color
ti.shape("arrow") #end of line symbol


#ti.forward(100)

#for loop that runs 4 times
for i in range(4):
    ti.forward(100)
    ti.right(90)

# while loop that runs 3 times
this_run = 0 

while this_run < 3:
    ti.forward(100) 
    ti.left(120) #the amount sides in triangle
    this_run += 1 # the amount of time the loops going to run

# Keeps the window open after the shape is drawn
range(4) #Loop run

win.mainloop()