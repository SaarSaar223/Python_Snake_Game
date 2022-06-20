import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.updatescore(0)
        self.ht()

    def updatescore(self, score):
        self.goto(10, 250)
        self.clear()
        self.write(f"Score = {score}", True, "center", ('Arial', 25, 'normal'))

    def gameovermessage(self):
        self.goto(0, 0)
        self.write("Game Over", True, "center", ('Arial', 25, 'normal'))
