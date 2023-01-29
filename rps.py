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

