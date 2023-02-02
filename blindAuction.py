from dependencies.auctionArt import logo
import os

clear = lambda: os.system('cls')
addingPlayers = True

while True:

    playerDict = {}
    highestBid = 0
    highestBidder = ''
    print(logo)

    while addingPlayers == True:
        name = input(f'What is your name? ').lower()
        bid = int(input(f'What is your bind? $'))
        playerDict[name] = bid
        check = input(f'Are there any other bidders? (y/n)\n')

        if check == 'y':
            clear()
            continue
        else:
            addingPlayers = False

    for key, value in playerDict.items():
        if value > highestBid:
            highestBid = value
            highestBidder = key
        
    print(f'The winner is {highestBidder} with a bid of ${highestBid}.')

    repeat = input('Would you like to use this tool again? (y/n)\n')

    if repeat == 'y':
        continue
    else:
        print('Thank you for using this tool!')
        exit()