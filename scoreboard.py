from turtle import Turtle

ALIGN = "center"
MOVE = False
FONT = ('Arial',20,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0, 270))
        self.writeScore()

    def increaseScore(self):
        self.score +=1
        self.writeScore()


    '''common method to update scoreboard'''
    def writeScore(self):
        self.clear();
        self.write(arg=f"Score:{self.score} High Score: {self.high_score}", move=MOVE, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.writeScore()


