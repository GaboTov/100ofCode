from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)
screen.title('Pong')
player_r = Paddle((350,0))
player_l = Paddle((-350, 0))
ball = Ball()
score_r = Scoreboard(-30)
score_l = Scoreboard(30) 
screen.update()
screen.listen()
screen.onkey(key='Up', fun=player_r.move_up)
screen.onkey(key='Down', fun=player_r.move_down)
screen.onkey(key='w', fun=player_l.move_up)
screen.onkey(key='s', fun=player_l.move_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(player_r) < 50 and ball.xcor() > 320 or ball.distance(player_l) < 50 and ball.xcor() < -320:
        ball.paddle_collision()
    #add score to left player
    if ball.xcor() < -380: 
        score_l.add_score()
        ball.rest_position()
    #add score to right player
    if ball.xcor() > 380:
        score_r.add_score()
        ball.rest_position()
    
screen.exitonclick()

