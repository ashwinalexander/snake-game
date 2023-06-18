# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food + add more food
# Keep track of score, scoreboard
# Detect collision with wall
# Detect collision with tail
import turtle
import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start_coordinates = [(0,0), (-20,0), (-40,0)]
segments = []

# set the start position of each of the snake body parts
for position in start_coordinates:
    print("coming here")
    part = Turtle(shape="square")
    part.color("white")
    part.penup()
    part.goto(position)
    segments.append(part)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    # range(start, stop, step)
    # working from the rear, move each of the body parts
    # forward to the location of the body part in front of it
    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    # Now move the first body part someplace
    segments[0].forward(20)
    segments[0].left(90)

    # game_is_on = False

screen.exitonclick()

