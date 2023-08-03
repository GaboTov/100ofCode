from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    words_list = pd.read_csv("31/data/words_to_learn.csv")
except FileNotFoundError:
    words_list = pd.read_csv('31/data/words.csv')
words = {}
row = 0
state = True
# flip card


def flip_card():
    global words, state
    # change style & text of card
    card_front.itemconfig(img_card, image=img_card_back)
    card_front.itemconfig(title_text, text="Español", fill="white")
    card_front.itemconfig(word_text, text=f"{words['español']}", fill="white")
    

# next card


def get_words():
    global words, timer, row
    window.after_cancel(timer)
    random_row_n = random.randint(0, len(words_list))
    row = random_row_n
    random_row = words_list.iloc[random_row_n]
    new_word = random_row['english']
    mean_new_word = random_row['español']
    words = {"english": new_word, "español": mean_new_word}
    card_front.itemconfig(img_card, image=img_card_front)
    card_front.itemconfig(title_text, text="English", fill="black")
    card_front.itemconfig(word_text, text=f"{new_word}", fill="black")
    timer = window.after(3000, flip_card)

# remove words


def know_card():
    global row, state
    words_to_learn = words_list.drop(row)
    words_to_learn.to_csv('31/data/words_to_learn.csv', index=FALSE)
    state = True
    get_words()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)
# cards

card_front = Canvas(width=800, height=526,
                    highlightthickness=0, bg=BACKGROUND_COLOR)
img_card_front = PhotoImage(file="31/images/card_front.png")
img_card_back = PhotoImage(file="31/images/card_back.png")
img_card = card_front.create_image(400, 263, image=img_card_front)
card_front.grid(row=1, column=1, columnspan=2)
title_text = card_front.create_text(
    400, 163, fill="black", text="English", font=("Arial", 40, "italic"))
word_text = card_front.create_text(
    400, 280, fill="black", text="word", font=("Arial", 60, "bold"))
get_words()
# buttons
img_wrong_btn = PhotoImage(file="31/images/wrong.png")
wrong_btn = Button(image=img_wrong_btn, highlightthickness=0,
                   bd=0, command=flip_card)
wrong_btn.grid(row=2, column=1)
img_right_btn = PhotoImage(file="31/images/right.png")
right_btn = Button(image=img_right_btn, highlightthickness=0,
                   bd=0, command=know_card)
right_btn.grid(row=2, column=2)


window.mainloop()
