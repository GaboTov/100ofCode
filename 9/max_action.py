import os
def clear_console():
    os.system('clear')
def compare_values(dic):
    if not dic:
        return
    winner = {
        'win': '',
        'bid': 0
    }
    for key in dic:
        if dic[key] > winner['bid']:
            winner['win'] = key
            winner['bid'] = dic[key]
    return winner

actions = {}
bidders = True
while bidders:
    person = str(input('What is your name?: '))
    action = int(input('What is your bind?: $'))
    actions[person] = action
    next = str(input("Are there any other bidders? Type 'yes' or 'no'"))
    if (next == 'no'):
        winner = compare_values(actions)
        print (f"The winner is {winner['win']} with a bid of ${winner['bid']}")
        bidders = False
    else:
        clear_console()
