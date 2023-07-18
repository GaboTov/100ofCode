from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

race_on = False
bet = 'red'#screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
def go_start (turtle, position):
    turtle.penup()
    turtle.goto(-170, 170 - (position * 55))


for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    all_turtles.append(tim)
    go_start(tim,turtle_index )
    

if bet in colors:
    race_on = True
win_color =''

while race_on:
    
    for turtle in all_turtles:   
        if turtle.xcor() >= 230:
            win_color = turtle.color()[0]
            race_on = False 
        move = random.randint(0, 10)
        turtle.forward(move)
        
if win_color == bet:
    print (f"You win the {win_color} turtle  wins ")
else:
    print(f"You lose the {win_color} turtle  wins")


screen.exitonclick()