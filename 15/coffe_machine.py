from data import resources, MENU

ESPRESSO = 'espresso'
LATTE = 'latte'
CAPPUCCINO = 'cappuccino'
COFFEE_TYPES = [ESPRESSO, LATTE, CAPPUCCINO]
    
def take_money():
    print('Please insert coins.')
    quarters = int(input("How mane quarters? :"))
    dimes = int( input("How many dimes?: "))
    nickles = int( input("How many nickles?: "))
    pennies = int( input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies*0.01
    return total
def check_resources(coffee):
    for ingredients in coffee['ingredients']:
        if resources[str(ingredients)] < coffee['ingredients'][ingredients]:
            print(F"Sorry there is not {ingredients}")
            return False
        else:
            continue 
    return True
        
def prep_coffee(coffee):
    for ingredients in coffee['ingredients']:
        resources[ingredients] -= coffee['ingredients'][ingredients]
def report():
    print(f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g \nMoney: ${resources['money']}")
    
def validate_and_prep_coffee(coffee_choice):  # CHANGE: Extract logic into separate function
    if coffee_choice in COFFEE_TYPES:
        prep = MENU[coffee_choice]
        if check_resources(prep):
            money = take_money()
            if money >= prep['cost']:
                prep_coffee(prep)
                change = round(money - prep['cost'], 2)
                resources['money'] += money - change
                print (f"Here is ${change} in change.")
                print(f"Here is your {coffee_choice}. Enjoy!")
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
    return False   
def coffee_machine():
    on = True
    while on: 
        coffee = str(input("What would you like? (espresso/latte/cappuccino): "))
        if coffee == 'report':
            report()
        elif validate_and_prep_coffee(coffee):
            continue
        elif coffee == 'off':
            break
        else:
            print('Select a correct option ')



coffee_machine()