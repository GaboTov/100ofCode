import random
from words import word_list
from stages import stages 
list_words = word_list

word = random.choice(list_words)

list_answer = list(word)

hints = ['_' for _ in word]
print(f'word is {word}') #test code

lifes = len(stages) -1 
while lifes >= 0 :
    user_letter=input('Guess a letter: ').lower()
    guessed = False
    for index ,letter in enumerate(list_answer):
        if user_letter == letter:
            hints[index] = letter
            guessed = True
    if not guessed:
        print (f"You gessed {user_letter}, that isn't in the word. You lose a life")
        print (' '.join(str(hint) for hint in hints))
        lifes -= 1
        print (stages[lifes])
        if lifes == 0:
            print('you lose :(')
            break
    else:
        
        print (' '.join(str(hint) for hint in hints))
        print (stages[lifes])
    if not '_' in hints:
        print(f'The word was {word}')
        print('you win!!')
        break
        
