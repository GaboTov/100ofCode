from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.reset_player()

    def move_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)
    def reset_player (self):
        self.seth(90)
        self.goto(0, -250)