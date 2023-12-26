import turtle
from turtle import Turtle, Screen

# create screen object and set colour bkacground
screen = Screen()
screen.bgcolor('darkseagreen')

# Write a title
banner = Turtle()
banner.hideturtle()
banner.penup()
banner.goto(0, 400)
banner.color('darkred')
banner.write("Welcome Turtle Race", align='center',  font=('verdana', 25,
                                                           'normal'))
# write turte colours
runners = Turtle()
runners.hideturtle()
runners.penup()
runners.goto(-300, -400)
runners.color('black')
runners.write("Turtles: cyan, pink, green, red, blue, yellow, orange",
              align='left',  font=('verdana', 13, 'normal'))

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
    if player_pos >= f_line_pos:
        return True


# Creating 6 instances of Turtle
def create_turtle(colour, x_pos, y_pos):
    player = Turtle(shape='turtle')
    player.speed('normal')
    player.shapesize(3)
    player.color(colour)
    player.penup()
    player.setposition(x_pos, y_pos)
    return player.fillcolor()


create_turtle('red', -450, 0)
create_turtle('blue', -450, -100)
create_turtle('yellow', -450, -200)
create_turtle('orange', -450, -300)
create_turtle('green', -450, 100)
create_turtle('violet', -450, 200)
create_turtle('cyan', -450, 300)

turtle.textinput("Make your bet", "Guess wich turtle will win the race: ")

screen.exitonclick()
