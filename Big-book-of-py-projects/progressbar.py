import random, time
from colorama import init, Fore, Back, Style


def getRedColor():
    return random.choice('red')


def main():
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0, 100)
        barStr = getProgressBar(bytesDownloaded, downloadSize)
        print(barStr, end='', flush=True)
        time.sleep(0.1)
        print('\b' * len(barStr), end='', flush=True)
    print(barStr)
    
        
def getProgressBar(progress, total, barWidth=40):
    BAR = Fore.BLUE+"█"
    progressBar = ''
    progressBar += '['
    if progress > total:
        progress = total
        BAR = Fore.GREEN+"█"
    if progress > 1024:
        BAR = Fore.LIGHTRED_EX+"█"
    if progress > 2048:
        BAR = Fore.LIGHTWHITE_EX+"█"
    if progress > 3072:
        BAR = Fore.LIGHTYELLOW_EX+"█"
    if progress < 0:
        progress = 0
        
    numberOfBars = int((progress/ total)*barWidth)   
    progressBar += BAR*numberOfBars
    progressBar += ' ' *(barWidth - numberOfBars) 
    progressBar += ']' 
    percentComplete = round(progress / total*100, 1)
    progressBar +=' ' + str(percentComplete) + '%'
    progressBar += ' ' + str(progress) + '/' + str(total)
    return progressBar

if __name__ == '__main__':
    main()