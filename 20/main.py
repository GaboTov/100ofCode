from turtle import Screen
from snake import Snake
import time 

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
snake = Snake()
screen.update()
screen.listen()
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='d', fun=snake.right)
screen.onkey(key='s', fun = snake.down)
game_is_on = True 

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()








screen.exitonclick()