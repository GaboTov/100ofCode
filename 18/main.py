import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
t.color('red')
def random_colors ():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color=(r,g,b)
    return random_color 

t.shape('turtle')
t.color('white')
t.speed('faster')
colors = random_colors()
def line(num):
    for _ in range(0,num):
        t.dot(10, random_colors ())
        t.penup()
        t.forward(25)
        t.pendown()
direction = 'left'
def change_direction(dir):
    if dir == 'left':
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(25)
    elif dir == 'right':
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(25)


for _ in range(0,5):
    line(10)
    change_direction('left')
    line(10)
    change_direction('right')
    


























screen.exitonclick()