import turtle
from turtle import Turtle, Screen
from random import randint

# Creating 6 instances of Turtle


def create_turtle(colour, x_pos, y_pos):
    player = Turtle()
    player.shapesize(3)
    player.color(colour)
    player.shape('turtle')
    player.penup()
    player.setposition(x_pos, y_pos)


create_turtle('red', -450, 0)
create_turtle('blue', -450, -100)
create_turtle('yellow', -450, -200)
create_turtle('orange', -450, -300)
create_turtle('green', -450, 100)
create_turtle('violet', -450, 200)
create_turtle('cyan', -450, 300)


guess_the_winner = turtle.textinput("Guess who will win", " ")
print(guess_the_winner)
screen = Screen()
screen.title("Welcome to the Turtle Race!")
screen.exitonclick()
