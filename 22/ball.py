from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = 0.1
        
    def move(self):    
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
    def bounce(self):
        self.move_y *= -1
    def paddle_collision(self):
        self.move_x *= -1
        self.ball_speed *= 0.9
    def rest_position(self):
        self.ball_speed = 0.1
        self.goto(0,0)