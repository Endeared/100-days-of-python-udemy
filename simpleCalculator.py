import pyfiglet


while True:
    print(pyfiglet.figlet_format('CALCULATOR'))

    firstNum = float(input(f'What is the first number?\n'))

    calculating = true


    while calculating = True:
        operation = input('Choose an operation.\n+\n-\n*\n/\n')
        secondNum = float(input(f'What is the second number?\n'))



        if operation == '+':
            sum = firstNum + secondNum
            print(f'{firstNum} + {secondNum} = {sum}')
            firstNum = sum
            secondNum = None
        elif operation == '-':
            sum = firstNum - secondNum
            print(f'{firstNum} - {secondNum} = {sum}')
            firstNum = sum
            secondNum = None
        elif operation == '*':
            product = firstNum * secondNum
            print(f'{firstNum} * {secondNum} = {product}')
            firstNum = product
            secondNum = None
        elif operation == '/':
            divisor = firstNum / secondNum
            print(f'{firstNum} / {secondNum} = {divisor}')
            firstNum = divisor
            secondNum = None
        else:
            print('Invalid operation / number(s). Please retry.')
            continue

        check = input(f"Type 'y' to continue calculating with {firstNum}, or type 'n' to start with a new number.")