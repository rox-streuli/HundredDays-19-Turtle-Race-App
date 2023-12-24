from turtle import Turtle, Screen
from random import randint

# Creating 6 instances of Turtle
red = Turtle()
red.shapesize(3)
red.shape('turtle')
red.color('red')
red.penup()
red.setposition(-450, 0)


blue = Turtle()
blue.shapesize(3)
blue.shape('turtle')
blue.color('blue')
blue.penup()
blue.setposition(-450, -100)


yellow = Turtle()
yellow.shapesize(3)
yellow.shape('turtle')
yellow.color('yellow')
yellow.penup()
yellow.setposition(-450, -200)


orange = Turtle()
orange.shapesize(3)
orange.shape('turtle')
orange.color('orange')
orange.penup()
orange.setposition(-450, -300)


green = Turtle()
green.shapesize(3)
green.shape('turtle')
green.color('green')
green.penup()
green.setposition(-450, 100)


violet = Turtle()
violet.shapesize(3)
violet.shape('turtle')
violet.color('violet')
violet.penup()
violet.setposition(-450, 200)


cyan = Turtle()
cyan.shapesize(3)
cyan.shape('turtle')
cyan.color('cyan')
cyan.penup()
cyan.setposition(-450, 300)


screen = Screen()
screen.exitonclick()
