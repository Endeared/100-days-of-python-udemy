import string
import random


letters = input("How many letters would you like in your password?\n")
symbols = input("How many symbols would you like in your password?\n")
numbers = input("How many numbers would you like in your password?\n")

password = ""

letters = int(letters)
symbols = int(symbols)
numbers = int(numbers)

while letters > 0 or symbols > 0 or numbers > 0:
    char = random.choice(string.ascii_letters)
    num = random.randint(0,9)
    symbol = random.choice(string.punctuation)
    choose = [char, num, symbol]
    thisValue = random.choice(choose)
    if thisValue == char and letters > 0:
        password += char
        letters -= 1
    elif thisValue == symbol and symbols > 0:
        password += symbol
        symbols -= 1
    elif thisValue == num and numbers > 0:
        password += str(num)
        numbers -= 1

print(f'Your password is: {password}')
