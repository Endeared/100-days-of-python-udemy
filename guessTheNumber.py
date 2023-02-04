import random
import os
from dependencies.guessNumberArt import logo

clear = lambda: os.system('cls')
guesses = 0

while True:
    clear()
    print(logo)
    print('Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.')
    number = random.randint(1,100)

    while True:
        
        difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard':\n").lower()

        if difficulty == 'easy':
            guesses = 10
            break
        elif difficulty == 'hard':
            guesses = 5
            break
        else:
            print('Invalid input.')
            continue



    

