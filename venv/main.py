import turtle
from turtle import Turtle, Screen
from random import randint

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

# Turtles attributes
colours = ['cyan', 'pink', 'green', 'red', 'blue', 'yellow', 'orange']
positions = [0, -100, -200, -300, 100, 200, 300]

turtles_in_race = []
# Creating 6 instances of Turtle

for indx, colour in enumerate(colours):
    player = Turtle(shape='turtle')
    player.color(colour)
    player.shapesize(3)
    player.speed('fast')
    player.penup()
    player.setposition(x=-450, y=positions[indx])
    turtles_in_race.append(player)

# store user's bet
bet = turtle.textinput("Make your bet", "Guess wich turtle will win the race: ")

start_race = False
winner = ""
if bet:
    start_race = True

while start_race:
    for player in turtles_in_race:
        run = randint(0, 10)
        player.forward(run)
        if player.xcor() >= f_line_pos:
            winner = player.fillcolor()
            start_race = False

runners.write(" ")
runners.goto(-100, 0)
if winner == bet:
    runners.write(f"You Won! \nThe winner is {winner.upper()}",
                  align='center',  font=('verdana', 25, 'normal'))
else:
    runners.write(f"Sorry, you lose. \nThe winner is {winner.upper()}",
                  align='center',  font=('verdana', 25, 'normal'))

screen.exitonclick()
