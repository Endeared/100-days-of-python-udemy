from dependencies.caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



while True:

    print(logo)
    option = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input(f"Type your message:\n").lower()
    shift = int(input(f"Type the shift number:\n"))
    newMessage = ""

    if option == 'encode':
        for char in message:
            if char not in alphabet:
                newMessage += char
            else:
                charIndex = alphabet.index(char)
                newIndex = charIndex + shift
                if newIndex > 25:
                    newIndex = newIndex % 26
                newMessage += alphabet[newIndex]
        print(f'Your encoded message is: {newMessage}')
    elif option == 'decode':
        for char in message:
            if char not in alphabet:
                newMessage += char
            else:
                charIndex = alphabet.index(char)
                newIndex = charIndex - shift
                if newIndex < 0:
                    newIndex = 26 - newIndex
                newMessage += alphabet[newIndex]
        print(f'Your decoded message is: {newMessage}')

    goAgain = input('Would you like to go again? (y/n)\n').lower()
    if goAgain == 'y':
        continue
    else:
        print('Thanks for using!\n')
        exit()


