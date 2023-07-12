# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food + add more food
# Keep track of score, scoreboard
# Detect collision with wall
# Detect collision with tail

import time
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard

screen = Screen()
scoreboardnew = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.moveSomeplace()
        scoreboardnew.increaseScore()
        snake.extend()

    # Detect collision with self
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboardnew.reset()
            snake.reset()
            game_is_on = True

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <=-280:
        game_is_on = False
        scoreboardnew.reset()
        snake.reset()
        game_is_on = True

    # Detect collision with tail
    

screen.exitonclick()