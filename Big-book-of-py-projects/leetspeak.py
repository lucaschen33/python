import random, pyperclip

def main():
    print("Enter your leet message")
    english = input('> ')
    print()
    leetSpeak = englishToLeetSpeak(english)
    print(leetSpeak)
    
    try:
        pyperclip.copy(leetSpeak)
        print('Copied leetspeak to clipboard')
    except NameError:
        pass
    
def englishToLeetSpeak(message):
    charMapping = {
            'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message:
        if char.lower() in charMapping and random.random() <=0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            leetspeak = leetspeak + char
    return leetspeak

if __name__ == '__main__':
    main()