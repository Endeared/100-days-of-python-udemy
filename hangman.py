import random
import pyfiglet
from dependencies.hangman_art import logo, stages
from dependencies.hangman_words import word_list


thisWord = random.choice(word_list)
thisLength = len(thisWord)
lives = 6

wordGuessed = []

print(logo)

for blank in range(thisLength):
    wordGuessed += "_"

while True:
    guess = input("Please guess a letter: ").lower()

    if guess in wordGuessed:
        print(f'You have already guessed that letter.')
    
    for position in range(thisLength):
        char = thisWord[position]
        if char == guess:
            wordGuessed[position] = char
    
    if guess not in thisWord:
        print(f'That letter is not in the word. You lose one life!')
        lives -= 1
        if lives == 0:
            print(pyfiglet.figlet_format('YOU LOSE!'))
            exit()

    print(f"{' '.join(wordGuessed)}")

    if "_" not in wordGuessed:
        print(pyfiglet.figlet_format('YOU WIN!'))
        exit()

    print(stages[lives])