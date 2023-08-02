import pandas as pd

data = pd.read_csv('26/nato_phonetic_alphabet.csv')
dict_nato = {row.letter: row.code for (index, row) in data.iterrows()}
def name_nato ():
    name_user = input("Enter a word: ").upper()
    try:
        list_name = [dict_nato[letter] for letter in name_user ]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        name_nato()
    else:
        print(list_name)

name_nato()