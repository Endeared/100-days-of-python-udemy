import random
import time
import pyfiglet

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ['rock', 'paper', 'scissors']

choice = input("What do you choose? Type 'rock', 'paper', or 'scissors'.\n")
computerChoice = random.choice(options)

print(f'You have chosen {choice.upper()}.')
if choice.lower() == 'rock':
    print(rock)
elif choice.lower() == 'paper':
    print(paper)
elif choice.lower() == 'scissors':
    print(scissors)
else:
    print('Your input is invalid. Please restart the game.')
    exit()

print(f'Computer is choosing...')
time.sleep(1)
print(f'Computer has chosen {computerChoice.upper()}.')
if computerChoice.lower() == 'rock':
    print(rock)
elif computerChoice.lower() == 'paper':
    print(paper)
elif computerChoice.lower() == 'scissors':
    print(scissors)

if choice.lower() == computerChoice:
    print(pyfiglet.figlet_format('TIE!'))
elif choice.lower() == 'rock' and computerChoice != 'paper':
    print(pyfiglet.figlet_format('PLAYER WINS!'))
elif choice.lower() == 'paper' and computerChoice != 'scissors':
    print(pyfiglet.figlet_format('PLAYER WINS!'))
elif choice.lower() == 'scissors' and computerChoice != 'rock':
    print(pyfiglet.figlet_format('PLAYER WINS!'))
elif choice.lower() == 'rock' and computerChoice == 'paper':
    print(pyfiglet.figlet_format('COMPUTER WINS!'))
elif choice.lower() == 'paper' and computerChoice == 'scissors':
    print(pyfiglet.figlet_format('COMPUTER WINS!'))
elif choice.lower() == 'scissors' and computerChoice == 'rock':
    print(pyfiglet.figlet_format('COMPUTER WINS!'))
exit()

