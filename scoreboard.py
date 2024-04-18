
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 200)
        self.color('green')
        self.write(f"SCORE: {self.score}", font=('Arial', 30, 'normal'), align="center")
    def win(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", font=('Arial', 30, 'normal'), align="center")