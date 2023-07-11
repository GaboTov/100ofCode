
""" 
from turtle import Turtle, Screen
timmy = Turtle()


timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() """

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Pokemon name','Type']
table.add_rows([
    ['Pickachu','Electric'],
    ['Squirtel','Water'],
    ['Charmander','Fire'],
    
])
print(table)