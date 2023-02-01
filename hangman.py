import random
from dependencies.hangman_art import logo
from dependencies.hangman_words import word_list


thisWord = random.choice(word_list)
thisLength = len(thisWord)
lives = 6

wordGuessed = []

print(logo)

for blank in range(thisLength):
    wordGuessed += "_"

while True:
    guess = input("Please gues a letter: ").lower()

    if guess in wordGuessed