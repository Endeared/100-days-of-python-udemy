import pyfiglet


while True:
    print(pyfiglet.figlet_format('CALCULATOR'))

    firstNum = float(input(f'What is the first number?\n'))
    operation = input('Choose an operation.\n+\n-\n*\n/\n')
    secondNum = float(input(f'What is the second number?\n'))