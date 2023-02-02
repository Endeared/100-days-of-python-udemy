import random
from dependencies.blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


startGame = input("Would you like to play a game of blackjack? (y/n)\n").lower()

if startGame == 'y':

    print(logo)

    card1 = random.choice(cards)
    card2 = random.choice(cards)
    currentScore = card1 + card2

    computerFirst = random.choice(cards)
    computerScore = computerFirst

    print(f'Your cards: {[card1, card2]}, current score: {currentScore}\n')
    print(f"Computer's first card: {[computerFirst]}, current score: {computerScore}\n")

    toContinue = input("Type 'y' to get another card, type 'n' to pass.\n")
