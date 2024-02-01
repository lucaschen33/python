import sys

try:
    import bext
except ImportError:
    print('install bext if you read this msg')
    sys.exit()

HEART = chr(9829)  # Character 9829 is '♥'.
bext.fg('red')
print(HEART, end='')
bext.fg('reset')

