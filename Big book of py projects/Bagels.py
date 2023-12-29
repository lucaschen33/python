import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''I am thinking of a {}-digit number. Try to guess what it is. The number will not have any repeting digits. Here are some clues. 
 When I say Pico, it means one diget is correct but in the wrong spot. 
When I say Fermi, it means one digit is correct and in the right position. 
When I say Bagels, it means that no digit is correct'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print('''You will have {} guesses to guess the secret number. Each round you play, the number will change randomly.'''.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
        
            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The correct number was {}.'.format(secretNum))
            
        print("Would you like to play again?")
        if not input('> ').lower().startswith('y'):
            break
        print("Thank you for playing.")
        
def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got the secret number"
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)



def getSecretNum():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

        
if __name__ == '__main__':
    main()