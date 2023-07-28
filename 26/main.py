import pandas as pd

data = pd.read_csv('26/nato_phonetic_alphabet.csv')
dict_nato = {row.letter: row.code for (index, row) in data.iterrows()}

name_user = input("Enter a word: ").upper()
list_name = [dict_nato[letter] for letter in name_user ]
print(list_name)