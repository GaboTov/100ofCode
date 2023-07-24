from turtle import Screen
from player import Player
from cars import Car
from boardlvl import Boardlvl
import time
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
game_on = True
player1 = Player()
car = Car()
lvl = Boardlvl()
screen.listen()
screen.onkey(player1.move_up, 'w')


while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    if player1.ycor() >= 260:
        player1.reset_player()
        lvl.add_lvl()
        car.speed += 1

    for x in car.all_cars:
        if player1.distance(x) <20:
            lvl.game_over()
            game_on = False




screen.exitonclick()







