
def getSevSegStr(number, numDigits=2):
    # Define the representation of each digit in a seven-segment display
    SEVENSEG = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ', '  |', '  |'],
        '2': [' _ ', ' _|', '|_ '],
        '3': [' _ ', ' _|', ' _|'],
        '4': ['   ', '|_|', '  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ', '|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ', '|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|']
    }

    # Pad the number with leading zeros to the desired number of digits
    number = str(number).zfill(numDigits)

    # Initialize the lines of the seven-segment display
    topRow, middleRow, bottomRow = '', '', ''

    # For each digit in the number
    for digit in number:
        # Get the seven-segment representation of the digit
        seg = SEVENSEG[digit]

        # Add the representation to each line
        topRow += seg[0] + '  '
        middleRow += seg[1] + '  '
        bottomRow += seg[2] + '  '

    # Combine the lines into a single string
    sevSegStr = '\n'.join([topRow, middleRow, bottomRow])

    return sevSegStr
