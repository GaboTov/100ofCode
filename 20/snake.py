from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    def create_snake(self):
        for _ in range(0,3):
            segment = Turtle()
            segment.penup()
            segment.shape('square')
            segment.color('white')
            segment.goto((_* -MOVE_DISTANCE), 0)
            self.snake.append(segment)
    
    def move(self):
        for seg_num in range(len(self.snake) -1 ,0,-1):
            new_x = self.snake[seg_num -1].xcor()
            new_y = self.snake[seg_num -1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)
    
    

    def left(self):
    
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self): 
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)