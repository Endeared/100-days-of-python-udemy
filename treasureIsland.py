print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

firstInput = input("You are at a fork in the road. Would you like to go left or right?\n")
if firstInput.lower() != 'left':
    print('You fell into a hole! Game over.')
    exit()

secondInput = input("You come across flooded river. Will you swim or wait for the level to lower?\n")
if secondInput.lower() != 'wait':
    print('You were attacked by an alligator! Game over.')
    exit()

thirdInput = input('You come across a set of three doors - one red, one blue, one yellow. Which door will you go through?\n')
if thirdInput.lower() == 'red':
    print('You were burned alive! Game over.')
    exit()
elif thirdInput.lower() == 'blue':
    print('You were eaten by beasts! Game over.')
    exit()
elif thirdInput.lower() == 'yellow':
    print('You open the door to find a massive cave filled with treasure. You win!')
    exit()
else:
    print('You decide to give up. Game over.')
    exit()
