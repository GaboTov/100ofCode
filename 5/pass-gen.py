import string 
import random
print('Welcome to the PyPassword Generator')

letters = int(input('How many letters would you like in your password? \n'))
symbols = int(input('How many symbols would you like? \n'))
numbers = int(input('How many numbers would you like? \n'))

letras = list(string.ascii_letters)
simbolos = list(string.punctuation)
numeros = list(range(10))
total = letters + symbols + numbers
print_letters = 0
print_symbols = 0
print_numbers = 0

result = []
#not random.shuffle
while len(result) < total:
    r1 = random.randint(0,2)
    if r1 == 0 and print_letters < letters:
        random_letter = random.randint(0, len(letras)-1)
        result.append(letras[random_letter])
        print_letters += 1
    elif r1 == 1 and print_symbols < symbols:
        random_symbol = random.randint(0,len(simbolos)-1)
        result.append(simbolos[random_symbol])
        print_symbols += 1
    elif r1 == 2 and print_numbers < numbers :
        random_number = random.randint(0, len(numeros)-1)
        result.append (str(numeros[random_number]))
        print_numbers += 1
res = "".join(result)
print(res)

password = []
for char in range(0 , letters+1):
    password.append(random.choice(letras))
for number in range(0 , numbers+1):
    password.append(str(random.choice(numeros)))
for symbol in range(0 , symbols+1):
    password.append(random.choice(simbolos))
random.shuffle(password)

res_pass = "".join(password)
print ('You password is: ' , res_pass)


# lection -> read the documentation of modules that we're using