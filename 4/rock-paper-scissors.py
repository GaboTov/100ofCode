import random

choose = int(input('What do you choose? Type 0 for rock, 1 for Paper or 2a for Scissors.'))


paper = """
 _______
|       |
|       |
|_______|
"""
rock = """
   OOO
  OOOOO
   OOO

"""
scissors = """
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

"""
cpu_player = random.randint(0,2)
if(choose == 0):
    print('You Choose',rock)
    if(cpu_player == 1):
        print('cpu Choose ' + paper , 'Cpu wins!!!')
    elif(cpu_player == 0):
        print('cpu Choose ' + rock , "It's a draw!")
    else:
        print('cpu Choose ' + scissors , 'You win!!!')
elif(choose == 1):
    print('You Choose',paper)
    if(cpu_player == 1):
        print('cpu Choose ' + paper , "It's a draw!")
    elif(cpu_player == 0):
        print('cpu Choose ' + rock , 'You win!!!')
    else:
        print('cpu Choose ' + scissors , 'Cpu win!!!')
elif(choose == 2):
    print('You Choose',scissors)
    if(cpu_player == 1):
        print('cpu Choose ' + paper , 'You win')
    elif(cpu_player == 0):
        print('cpu Choose ' + rock , 'Cpu win!!!')
    else:
        print('cpu Choose ' + scissors , "It's a draw!")
else:
    print("that isn't an option")