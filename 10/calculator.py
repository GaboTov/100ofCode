from cal import calculator
calculate = True
first = True
while calculate:
    if first:
        number1 = float(input("What's tht first number?: "))
        print ("+, -, *, /")
        operation = str(input("Pick an operator: "))
        number2 = float(input("What's tht next number?: "))
        result = calculator(number1, number2, operation)
        print(f"{number1} {operation} {number2} = {result}")
        next = str(input(f"Type 'y' to continue with {result}, or type 'no' to start a new calculation: "))
    else: 
        new_number1 = result
        operation = str(input("Pick an operator: "))
        new_number2 = float(input("What's tht next number?: "))
        new_res = calculator(new_number1,new_number2, operation )
        print(f"{new_number1} {operation} {new_number2} = {new_res}")
        next = str(input(f"Type 'y' to continue with {new_res}, or type 'no' to start a new calculation: "))
    if next == 'y':
        first = False
    else:
        first = True
