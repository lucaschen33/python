import time, sys, bext

print('Press Ctrl-C to stop')
time.sleep(3)
indent= 0
indentIncreasing = True

try:
    while True:
        print(' '*indent, end ='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('purple')
        print('##', end='')
        bext.fg('cyan')
        print('##')
        
        if indentIncreasing:
            indent = indent + 1
            if indent == 60:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
        
        time.sleep(0.02)
except KeyboardInterrupt:
    sys.exit()