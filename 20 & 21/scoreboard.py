from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
DATA = open("20 & 21/data.txt", mode='r')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.high_score = int(DATA.read())
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()
    
    def refresh_score (self):
        self.score += 1 
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("20 & 21/data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    """ def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT) """