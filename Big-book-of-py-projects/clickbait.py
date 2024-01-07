import random

OBJECT_PRONOUS = ['Her', 'Him,', 'Them']

POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']

PERSONAL_PRONOUNS = ['She', 'He', 'They']

PROVINCES = ['Ontario', 'Alberta', 'British Coulumbia', 'Saskatchewan', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Prince Edward Island', 'Quebec', 
             'Yukon', 'Nunavut', 'Northwest Territories']

NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def millennial():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killing the {} Industry?'.format(noun)

def dontKnow():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without this {}, {} could kill you {}'.format(noun, pluralNoun, when)

def bigcompanieshate():
    pronoun = random.choice(OBJECT_PRONOUS)
    province = random.choice(PROVINCES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big companies  hate {}! See how this {} {} invented a cheaper {}'.format(pronoun, province, noun1, noun2)

def youwontbelieve():
    pronoun = random.choice(OBJECT_PRONOUS)
    province = random.choice(PROVINCES)
    noun = random.choice(NOUNS)
    place = random.choice(PLACES)
    return 'You won\'t believe what this {} {} found in {} {}'.format(province, noun, pronoun, place)

def dontwantyouknow():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} don\'t want you to know about {}'.format(pluralNoun1, pluralNoun2)

def giftidea():
    number = random.randint(7,15)
    noun = random.choice(NOUNS)
    province = random.choice(PROVINCES)
    return '{} gift ideas to give your {} from {}'.format(number, noun, province)

def reasonswhy():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return '{} reasons why {} are more interesting than you think (number {} will surprise you!)'.format(number1, pluralNoun, number2)

def jobAuto():
    province = random.choice(PROVINCES)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(province, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(province, noun, pronoun1, pronoun2)
    
    
def main():
    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break 
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)
        if clickbaitType == 1:
            headline = millennial()
        elif clickbaitType == 2:
            headline = dontKnow()
        elif clickbaitType == 3:
            headline = bigcompanieshate()
        elif clickbaitType == 4:
            headline = youwontbelieve()
        elif clickbaitType == 5:
            headline = dontwantyouknow()
        elif clickbaitType == 6:
            headline = giftidea()
        elif clickbaitType == 7:
            headline = reasonswhy()
        elif clickbaitType == 8:
            headline = jobAuto()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')
    
    
    
if __name__ == '__main__':
    main()