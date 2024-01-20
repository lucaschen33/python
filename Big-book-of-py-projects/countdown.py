import sys, time
import sevseg

secondsLeft = 30

try:
    while True:
        print('\n' * 60)
        hours = str(secondsLeft // 3600)
        minutes = str((secondsLeft % 3600)// 60)
        seconds = str(secondsLeft % 60)
        
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        
        hDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = hDigits.splitlines()
        
        hDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = hDigits.splitlines()
        
        print(hTopRow    + '     ' + mTopRow    + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)
        
        if secondsLeft == 0:
            print()
            print('Timer over')
            break
        
        print()
        print('Press Ctrl-C to quit countdown')
        time.sleep(1)
        secondsLeft -=1
except KeyboardInterrupt:
        sys.exit()