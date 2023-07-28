import turtle
import pandas as pd
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
screen = turtle.Screen()
screen.title("U.S States game")
image = "25/blank_states_img.gif"
screen.addshape(image)
guessed_states = []
turtle.shape(image)

data = pd.read_csv("25/50_states.csv")
list_states = data.state.tolist()



while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states", prompt="What's another state's name?")
    capitalized_answer = answer_state.title()
    if capitalized_answer == 'Exit':
        missing_states = [state for state in list_states if state not in guessed_states ]
        """ for state in list_states:
            if state not in guessed_states:
                missing_states.append(state) """
        pd.DataFrame(missing_states).to_csv("25/states_to_learn.csv")
        break

    if capitalized_answer in list_states:
        guessed_states.append(capitalized_answer)
        cor_state = data[data.state == capitalized_answer].iloc[0].to_list()
        write_cor = turtle.Turtle()
        write_cor.hideturtle()
        write_cor.penup()
        write_cor.goto(cor_state[1], cor_state[2])
        write_cor.write(f"{capitalized_answer}",align=ALIGNMENT,font=FONT)


state_learned = pd.DataFrame(guessed_states).to_csv("25/sates_learned.csv")
