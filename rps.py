import random

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