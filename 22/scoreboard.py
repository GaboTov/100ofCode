from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")
class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.goto(x, 250)
        self.score = 0
        self.write(f"{self.score}", align=ALIGNMENT , font=FONT)

    def add_score (self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT , font=FONT)