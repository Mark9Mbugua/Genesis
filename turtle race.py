from turtle import *
from random import randint

penup()
goto(-140, 40)

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    speed(10)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle() #we create a turtle object called ada
ada.color('red') # the color of the title object is red
ada.shape('turtle') # the shape of the turtle object is that of a turtle

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

affy = Turtle()
affy.color('yellow')
affy.shape('turtle')

# we send the turtle to the starting line
ada.penup()
ada.goto(-140, 20)
ada.pendown()

bob.penup()
bob.goto(-140, 10)
bob.pendown()

affy.penup()
affy.goto(-140, -10)
affy.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    affy.forward(randint(1,5))
    
    



    
    

