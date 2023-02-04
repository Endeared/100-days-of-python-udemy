import random
import os
from dependencies.blackjack_art import logo


while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    clear = lambda: os.system('cls')

    startGame = input("Would you like to play a game of blackjack? (y/n)\n").lower()

    if startGame == 'y':

        clear()
        print(logo)

        card1 = random.choice(cards)
        card2 = random.choice(cards)
        currentScore = card1 + card2

        computerFirst = random.choice(cards)
        computerScore = computerFirst

        print(f'Your cards: {[card1, card2]}, current score: {currentScore}\n')
        print(f"Computer's first card: {[computerFirst]}, current score: {computerScore}\n")

        if currentScore == 21:
            print("Blackjack! You win.")
            exit()

        while currentScore < 21:
            toContinue = input("Type 'y' to get another card, type 'n' to pass.\n")
            if toContinue == 'y':
                newCard = random.choice(cards)
                currentScore = currentScore + newCard
                print(f'The card was {newCard}. Your current score is {currentScore}.')
            elif toContinue == 'n':
                while computerScore < 17:
                    computerNew = random.choice(cards)
                    computerScore = computerScore + computerNew
                break

        if currentScore > 21:
            print(f'You broke over 21. You lose!')
        elif currentScore == 21:
            print(f'Blackjack! You win.')
        print(f'Your score is {currentScore}.')
        print(f'The computer score is {computerScore}.')
    
    elif startGame == 'n':
        print(f'Thank you for trying this software!')
        exit()

    else:
        print(f'Invalid input. Try again.')
