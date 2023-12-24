import turtle
from turtle import Turtle, Screen
from random import randint

# Draw finish line
finish_line = Turtle()
finish_line.pensize(3)
finish_line.hideturtle()
finish_line.penup()
finish_line.speed('fastest')
finish_line.setposition(400, -400)
finish_line.left(90)
finish_line.pendown()
finish_line.forward(800)
f_line_pos = 400


def winner(player_pos):
    if player_pos == f_line_pos:
        return True

# Creating 6 instances of Turtle
def create_turtle(colour, x_pos, y_pos):
    player = Turtle()
    player.speed('normal')
    player.shapesize(3)
    player.color(colour)
    player.shape('turtle')
    player.penup()
    player.setposition(x_pos, y_pos)


red = create_turtle('red', -450, 0)
blue = create_turtle('blue', -450, -100)
yellow = create_turtle('yellow', -450, -200)
orange = create_turtle('orange', -450, -300)
green = create_turtle('green', -450, 100)
violet = create_turtle('violet', -450, 200)
cyan = create_turtle('cyan', -450, 300)


guess_the_winner = turtle.textinput("Guess who will win", " ")
print(guess_the_winner)
screen = Screen()
screen.exitonclick()
