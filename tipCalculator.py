print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n")
percent = input("What percent tip would you like to give? (i.e 15)\n")
people = input("How many people should split the bill?\n")

split = float(bill) / int(people)
afterTip = split + split * (int(percent) / 100)
print(f'Each person should pay {round(afterTip, 2)}.')