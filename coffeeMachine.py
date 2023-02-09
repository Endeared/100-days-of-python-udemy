water = 500
milk = 500
coffee = 500
profit = 0

import pyfiglet
print(pyfiglet.figlet_format('COFFEE MACHINE'))

while True:
    choice = input("What would you like? (espresso / latte / cappucciono)\n").lower()
    if choice == "off":
        exit()
    elif choice == "report":
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}')
    
    if choice == "espresso"