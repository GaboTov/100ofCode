import random
from random import randint
import os 

def result(player_cards, cpu_cards):
    player_res = sum(player_cards)
    cpu_res = sum(cpu_cards)
    print(f"Your cards: {player_cards}, your current score: {player_res}")
    print(f"Computer's firs card: {cpu_cards[0]}")
    print(f"Your final hand: {player_cards}, final score: {player_res} ")
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_res} ")
    if cpu_res == 21 and player_res == 21:
        print("Push")
    elif player_res == 21:
        print("You win!!!!")
    elif cpu_res == 21:
        print('Computer win!')
    elif player_res > cpu_res and player_res < 21:
        print('You win!!!!')
    elif cpu_res > player_res and cpu_res < 21:
        print('Computer win!')
    elif cpu_res < player_res:
        print('Computer win!')
    else:
        print('You win!!!!')

def cpu_game(cpu_cards):
    cards = cpu_cards
    cpu_risk = random.randint(1,5)
    while sum(cpu_cards) < 21 - cpu_risk:
        cards.append(random.randint(1,10))
    return cards
game = True
while game:
    player_cards = [randint(1, 10) for _ in range(2)]
    cpu_cards = [randint(1, 10) for _ in range(2)]
    print(f"Your cards: {player_cards}, your current score: {sum(player_cards)}")
    print(f"Computer's firs card: {cpu_cards[0]}")
    get_card = str(input("Type 'y' to get another card, type 'n' to pass: "))
    cpu_final = cpu_game(cpu_cards)
    while get_card == 'y':
        player_cards.append(random.randint(1,10))
        if sum(player_cards) > 21:
            break
        print(f"Your cards: {player_cards}, your current score: {sum(player_cards)}")
        print(f"Computer's firs card: {cpu_cards[0]}")
        get_card = str(input("Type 'y' to get another card, type 'n' to pass: "))
    result(player_cards, cpu_final)
    new_game = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n'"))
    if new_game == 'n':
        game == False
    else:
        os.system('clear')
