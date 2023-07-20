from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    def create_snake(self):
        for cor in POSITIONS:
            self.add_segment(cor)
    
    def move(self):
        for seg_num in range(len(self.snake) -1 ,0,-1):
            new_x = self.snake[seg_num -1].xcor()
            new_y = self.snake[seg_num -1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)
    
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape('square')
        segment.color('white')
        segment.goto(position)
        self.snake.append(segment)

    def extend(self ):
        self.add_segment(self.snake[-1].position())
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