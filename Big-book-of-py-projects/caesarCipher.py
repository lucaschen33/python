import pyperclip

SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    print('Encrypt meaning to conceal a message, decrypt meaning to uncover a message.')
    response = input('')
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')
    
    
while True: 
    maxKey = len(SYMBOL) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOL):
        key = int(response)
        break
    
print('Enter the message to {}.'.format(mode))
message = input('> ')

message = message.upper()
translated = ''


for symbol in message:
    if symbol in SYMBOL:
        num = SYMBOL.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key



        if num >= len(SYMBOL):
            num = num - len(SYMBOL)
        elif num < 0:
            num = num + len(SYMBOL)

        translated = translated + SYMBOL[num]
    else:
        translated = translated + symbol
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass
