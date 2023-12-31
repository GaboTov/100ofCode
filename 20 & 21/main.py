from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
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

    #detect collision with food.
    if snake.head.distance(food) < 17:
        food.refresh()
        score.refresh_score()
        snake.extend()
        
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -300 or snake.head.ycor() > 280:
        snake.reset()
        score.reset()
        

    #detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()







screen.exitonclick()