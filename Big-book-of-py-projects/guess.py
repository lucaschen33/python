import random

def askForGuess():
    while True:
        guess = input('> ')
        
        if guess.isdecimal():
            return int(guess)
        print('enter a integer between 1 and 100')
        
        
print()
secretNumber = random.randint(1, 100)
print("I am thinking of a number between 1 and 100")

for i in range(10):
    print('You have {} guesses left. Take a guess'. format(10-i))
    guess  = askForGuess()
    if guess == secretNumber:
        break
    
    if guess < secretNumber:
        print('Your guess is too low')
    if guess > secretNumber:
        print('Your guess is too high')
        
if guess == secretNumber:
    print("You guessed the secret number")
else:
    print('Game over, the number I was thinking of was', secretNumber)