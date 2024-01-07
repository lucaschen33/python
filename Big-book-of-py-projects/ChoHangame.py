import random, sys

JAP_NUM = {1: 'ICHI', 2: 'NI', 3: 'SAN',4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

wallet = 5000

while True:
    print('You have', wallet, 'mon. How much do you bet? Please enter "QUIT" to exit the game')
    while True: 
        pot = input('>  ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing.')
            sys.exit
        elif not pot.isdecimal:
            print("Please enter a number.")
        elif int(pot) > wallet:
            print("You do not have enough mon to place this bet. Please enter an amount equal or under your balance.")
        else:
            pot = int(pot)
            break
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')
    
    while True:
        bet = input('>  ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please either enter CHO or HAN. CHO meaning even and HAN meaning ODD')
            continue
        else:
            break
        
    print('The dealer lifts the up to reveal...')
    print('  ', JAP_NUM[dice1], '-', JAP_NUM[dice2])
    
    print('  ',dice1, '-', dice2)
    
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
        
        playerWon = bet == correctBet
        
        if playerWon:
            print('You win! You take', pot, 'mon.')
            wallet = wallet + pot
            print('The house collects a', pot // 10, 'mon fee')
            wallet = wallet - (pot // 10)
            
        else: wallet = wallet - pot
        print('You lost!')
        
        if wallet == 0: 
            print("You ran out of money!")
            print("Thanks for playing")
            sys.exit()