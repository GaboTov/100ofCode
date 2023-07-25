
def get_names ():
    with open('24/input/names/invited_names.txt', 'r') as f:
        my_list = f.readlines()
    list_of_names = [line.strip() for line in my_list]
    return list_of_names

def change_name(name):
    #get content
    with open('24/input/letter/starting_letter.txt') as letter:
        letter_content = letter.read()
    #edit content
    letter_content = letter_content.replace('person', str(name))
    #write a letter with new content
    with open(f'24/output/readyToSend/{name}_letter.txt',mode='w') as f:
        f.write(letter_content)

list_of_names = get_names()
for name in list_of_names:
    change_name(name)