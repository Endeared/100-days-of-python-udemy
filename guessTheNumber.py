import random
import os
from dependencies.guessNumberArt import logo

clear = lambda: os.system('cls')
guesses = 0
guessing = False

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

    guessing = True
    while guessing == True:

        print(f'You have {guesses} attempt(s) remaining to guess the number.')
        guess = input('Make a guess: ')

        if int(guess) == number:
            print('Correct guess! You win!')
            playAgain = input(f'Would you like to play again? (y/n)\n').lower()

            while True:
                if playAgain == 'y':
                    guessing = False
                    break
                elif playAgain == 'n':
                    print('Thanks for playing!')
                    exit()
                else:
                    print('Invalid input.')
                    continue

        elif int(guess) < number:
            print('Too low.\nGuess again.')
            guesses -= 1
        elif int(guess) > number:
            print('Too high.\nGuess again.')
            guesses -= 1
        elif int(guess) < 1 or int(guess) > 100:
            print('Guess is outside range.\nGuess again.')
        else:
            print('Invalid input. Guess again.')

        if guesses == 0:
            print('You ran out of guesses! You lose.')
            playAgain = input(f'Would you like to play again? (y/n)\n').lower()

            while True:
                if playAgain == 'y':
                    guessing = False
                    break
                elif playAgain == 'n':
                    print('Thanks for playing!')
                    exit()
                else:
                    print('Invalid input.')
                    continue
        
    



    

