# This program uses turtle program (for) to draw a basic square and triangle
# 3/14/21
# CTI-110-0B01
# Tyler Bennett


import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.pencolor("red")
t.shape("turtle")

for i in (1,2,3,4):
    t.forward(100)
    t.left(90)
    
t.right(100)

for i in (1,2,3):
    t.forward(100)
    t.left(120)

win.mainloop()


    
# Set turtle program
# Input command to create a square
# Input command to create a triangle
# End program
