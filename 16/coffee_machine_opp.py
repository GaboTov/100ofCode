from data import MENU

ESPRESSO = 'espresso'
LATTE = 'latte'
CAPPUCCINO = 'cappuccino'
COFFEE_TYPES = [ESPRESSO, LATTE, CAPPUCCINO]

class CoffeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0
        }
    def check_resources(self, coffee):
        for ingredients in coffee['ingredients']:
            if self.resources[ingredients] < coffee['ingredients'][ingredients]:
                print (f"Sorry there is not {ingredients}")
                return False
            else:
                continue
        return True
    def make_coffee(self,prep, coffee):
        for ingredients in prep['ingredients']:
            self.resources[ingredients] -= prep['ingredients'][ingredients]
        print(f"Here is your {coffee}. Enjoy!")
        self.resources['money'] += prep['cost']
    def report(self):
        print(f"Water: {self.resources['water']} ml \nMilk: {self.resources['milk']} ml\nCoffee: {self.resources['coffee']} g \nMoney: ${self.resources['money']}")
    def init_machine (self):
        coffee = str(input("What would you like? (espresso/latte/cappuccino): "))
        return coffee
class MoneyMachine:
    def __init__(self):
        self.money = 0
    def take_money(self):
        self.money = 0
        print('Please insert coins.')
        try:
            quarters = int(input("How many quarters? :"))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies*0.01
            self.money = total
        except ValueError:
            print("Invalid input, only numeric values accepted.")
    def change(self, cost):
        if self.money >= cost:
            new_change = round(self.money - cost, 2)
            print(f"Here is ${new_change} in change.")
            self.money = 0
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money = 0
            return False
        return True
    
machine = CoffeMachine()
money = MoneyMachine()
def coffee_machine():
    on = True
    while on:
        coffee = machine.init_machine()
        if coffee in COFFEE_TYPES:
            prep = MENU[coffee]
            money.take_money()
            if machine.check_resources(prep) and money.change(prep['cost']):
                machine.make_coffee(prep, coffee)
        elif coffee == 'off':
            on = False
        elif coffee == 'report':
            machine.report()
        else:
            print ('Select a correct option')

coffee_machine()