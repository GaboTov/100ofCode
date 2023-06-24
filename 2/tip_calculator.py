
print('Welcome to tip calculator.')
bill = float(input('What was the total bill? $'))
people = int(input('How many people to spilt the bill? '))
percentage = float(input('What percentage tip would you like to give? '))/100
total = (bill + (bill * percentage))/people
print ('Each person should pay: $'+ str(round(total,2)))