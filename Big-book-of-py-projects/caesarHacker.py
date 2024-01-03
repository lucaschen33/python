message = input('''What is the message you would like to decrypt(Please only input messages from Caesar Cipher).''')

SYMBOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOL)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOL:
            num = SYMBOL.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(SYMBOL)

            translated = translated + SYMBOL[num]
        else:
            translated = translated + symbol
    print('Key #{}: {}'.format(key, translated))
        