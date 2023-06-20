from turtle import Turtle

ALIGN = "center"
MOVE = False
FONT = ('Arial',20,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0, 270))
        self.writeScore()

    def increaseScore(self):
        self.score +=1
        self.writeScore()

    def writeScore(self):
        self.clear();
        self.write(arg=f"Score:{self.score}", move=MOVE, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write(arg=f"Game Over, You Lose", move=MOVE, align="center", font=FONT)


