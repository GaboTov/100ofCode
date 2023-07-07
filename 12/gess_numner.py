import random

def result(guess, number):
    if guess < number:
        return ('Too low')
    elif guess > number:
        return('Too high')
    elif guess == number:
        return('You win!!!')
def set_difficulty():
    difficulty = input(str("Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty == 'easy':
        attempts = easy
    elif difficulty == 'hard':
        attempts = hard
    return attempts
easy  = 10
hard = 5 
print("Welcome to the Number Guessing Game!")
attempts = set_difficulty()
number = random.randint(0, 100)
while attempts > 0:
    print (f"You have {attempts} remaining to guess the number.")
    guess = input(str("Make a guess: "))
    res = result(int(guess),number)
    print (res)
    if res == 'You win!!!':
        break
    attempts -= 1 

if attempts == 0:
    print('Game over')