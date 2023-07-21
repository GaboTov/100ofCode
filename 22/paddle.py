from turtle import Turtle


class Paddle(Turtle):
    def __init__(self , init_position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(init_position)
        self.setheading(90)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y) 

        