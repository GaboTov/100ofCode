from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.back(10)

def counter_clockwise():
    tim.left(15)
def clockwise():
    tim.right(15)
def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset)
screen.exitonclick()