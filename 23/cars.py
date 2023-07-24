from turtle import Turtle
import random
import time
COLORS = ['green','yellow','blue','red','orange','purple']
SPEEDLVL = 10
STARTING_MOVE_DISTANCE = 5
class Car(Turtle):
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1: 
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200,200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    