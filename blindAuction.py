from dependencies.auctionArt import logo
import os

clear = lambda: os.system('cls')
addingPlayers = True

while True:

    playerDict = {}
    print(logo)

    while addingPlayers == True:
        name = input(f'What is your name? ').lower()
        bid = int(input(f'What is your bind? $'))
