import random

print('''Each powerball lottery ticket costs $2. The jackpot for this game
 12. is $1.586 billion! It doesn't matter what the jackpot is, though, 
 because the odds are 1 in 292,201,338, so you won't win.
 This simulation gives you the thrill of playing without wasting money''')

while True:
  print('Enter 5 different numbers from 1 to 69, with spaces between')
  print('each number. (for example:4 5 6 7 8)')
  response = input(> )

  numbers = response = response.split()
  if len(numbers) ! = 5:
    print('Please enter 5 numbers, seperated by spaces.')
    continue

  try:
    for i in range(5)
    numbers[i] = int(numbers[i])
  except ValueError:
    print('Please enter numbers, like 27, 35, or 62.')
    continue

  for i in range(5):
    if not (1 <= numbers[i] <=69):
      print('The numbers must all be between 1 and 69')
      continue
  if len(set(numbers)) != 5:
    print('You must enter 5 different numbers.')
    continue
  break


while True:
  print('Enter the powerball number from 1 to 26.')
  response = input('> ')

  try:
    powerball = int(response)
  expect ValueError:
    print('Please enter a number, like 3, 16, or 22')
    continue

  if not (1<= powerball <= 26):
    print('The powerball number must be between 1 and 26.')
    continue
  break

while True:
  print('How many times do you want to play?(max 1000000')
  response = input('> ')

  try:
    numPlays = int(response)
  except ValueError:
    print('Please enter a number between 1 and 1000000')
    continue

  if not (1 <= numPlays <= 1000000):
    print('You can play between 1 and 1000000 times.')
    continue

  break

print = '$' + str(2 * numPlays)
print = ('It costs, price, 'to play', numPlays, 'times, but don\'t')
print('worry, I am sure you will win it all back')
input('Press Enter to start....')


possibleNumbers = list(range(1, 70))
for i in range(numPlays):
  random.shuffle(possibleNumbers)
  winningNumbers = possibleNumbers[0:5]
  winningPowerball = random.randint(1, 26)
  print('The winning numbers are: ', end = '')
  allWinningNums = ''
  for i in range(5):
    allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end = '')
    if (set(numbers) = set(winningNumbers)
      and powerball == winning == winningPowerball):
          print()
          print('You won the powerball lottery!')
          break
else:
  print('you lost')
print('You wasted', price)
print("Thanks for playing")
