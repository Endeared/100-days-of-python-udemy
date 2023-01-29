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

choice = input("What do you choose? Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS.")
computerChoice = random.choice(options)

print(f'You have chosen {choice}.')
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


