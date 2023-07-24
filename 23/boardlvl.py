from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")
class Boardlvl (Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220,240)
        self.lvl = 1
        self.write
        self.write(f"Level: {self.lvl}", align=ALIGNMENT , font=FONT)
    
    def add_lvl(self):
        self.lvl += 1
        self.clear()
        self.write(f"Level: {self.lvl}", align=ALIGNMENT , font=FONT)

    def game_over(self):
        writer_turtle = Turtle()
        writer_turtle.hideturtle()
        writer_turtle.penup()
        writer_turtle.write("GAME OVER", align=ALIGNMENT , font=FONT)