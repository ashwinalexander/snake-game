from turtle import Turtle

START_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        # set the start position of each of the snake body parts
        for position in START_COORDINATES:
            part = Turtle(shape="square")
            part.color("white")
            part.penup()
            part.goto(position)
            self.segments.append(part)


    # This is the core snake motion algorithm
    def move(self):
        # range(start, stop, step)
        # working from the rear, move each of the body parts
        # forward to the location of the body part in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Now move the first body part someplace
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if (self.head.heading() != DOWN):
            # we do not want the snake to reverse direction
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading() != UP):
            # we do not want the snake to reverse direction
            self.head.setheading(DOWN)

    def left(self):
        # we do not want the snake to reverse direction
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def right(self):
        # we do not want the snake to reverse direction
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
