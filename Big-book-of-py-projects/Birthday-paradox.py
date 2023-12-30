import datetime, random

def getBirthdays(numofbday):
    birthdays = []
    for i in range(numofbday):
        startofyear  = datetime.date(2000, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 365))
        birthday = randomNumberOfDays + startofyear
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None 
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA

print('''The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. In a group of 70people, there’s a 99.9 percent chance of two people having a matching birthday. 
      But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday. This program performs several probability experiments to determine the percentages for groups of different sizes. 
      We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.''')

MONTHS = ('jan', 'feb', 'mar','apr', 'may', 'jun', 'jul', 'aug,','sep','oct', 'nov', 'dec')

while True:
    response = input('''"How many birthdays should I generate?(Max is 50)
               ''')
    if response.isdecimal() and (1 <= int(response) <= 50):
        numBdays = int(response)
        break
    else:
        print("Please only type integers under 50 and over 0.")
        response = input('''"How many birthdays should I generate?(Max is 50)
               ''')

        
    

print('Here are', numBdays, 'birthdays:')
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthname = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthname, birthday.day)
    print(dateText, end='')
print('''
      ''')
match = getMatch(birthdays)
print('In this simulation, ', end = '')
if match !=None:
    monthname = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthname, match.day)
    print('''multiple people have a birthday on {}'''.format(dateText))
else:
    print("there are no matching birthdays")
    
print('Generating', numBdays, 'random birthdays 100,000 times: ')
input('Press Enter to begin: ')
print('Let\'s run another 100,000 simulations:')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i,'simulations run')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100,000 simulations run")

prob = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBdays,'people, there was a')
print('matching birthday in that group', simMatch, 'times. this means')
print('that', numBdays, 'people have a', prob, '% chance of having a matching birthday in their group.')