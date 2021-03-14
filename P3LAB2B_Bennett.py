# This program will use turtle to spell out my initials, "T B" 
# 3/14/21
# CTI-110 P3LAB2B
# Tyler Bennett
# 
import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(10)
t.pencolor("orange")
t.shape("turtle")

t.forward(100)
t.right(180)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.penup()
t.forward(100)
t.pendown()
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(180)
t.forward(75)
t.right(90)
t.forward(50)
t.right(90)
t.forward(75)

win.mainloop()



# Set turtle program
# Input commands to spell out your initials
# Input penup and pendown commands when necessary to seperate letters
# End turtle program
