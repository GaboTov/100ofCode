from data import data
import random 
import os
from art import logo, vs
def new_data(prev_data):
    result = random.choice(data)
    if result != prev_data:
        return result
    else:
        result = random.choice(data)
        return result

def print_compare(compare1, a):
    if a == 'a':
        print (f"Compare A: {compare1['name']}, a {compare1['description']}, from {compare1['country']}")
    elif a == 'b':
        print (f"Against B: {compare1['name']}, a {compare1['description']}, from {compare1['country']}")
prev_data = None
score = 0
win = True

while win:
    os.system('clear')
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    if not prev_data:
        compare1 = new_data(prev_data)
    else:
        compare1 = prev_data
    print_compare(compare1, 'a')
    print(vs)
    compare2 = new_data(compare1)
    print_compare(compare2, 'b')
    if compare1['follower_count'] > compare2['follower_count']:
        winner = 'a'
        prev_data = compare1
    else:
        winner = 'b'
        prev_data = compare2
    player_choose  = str(input("who has more followers? Type 'A' or 'B': ")).lower()
    if player_choose != winner:
        print(f"Sorry, that's wrong. Final score: {score}")
        win = False
    elif player_choose == winner:
        score += 1
        
        

