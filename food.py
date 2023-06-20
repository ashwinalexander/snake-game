from turtle import Turtle
import random

LOWER_BOUND = -280
UPPER_BOUND = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")

        self.moveSomeplace()

    def moveSomeplace(self):
        '''Go to a random location'''
        random_x = random.randint(LOWER_BOUND, UPPER_BOUND)
        random_y = random.randint(LOWER_BOUND, UPPER_BOUND)
        self.goto((random_x, random_y))