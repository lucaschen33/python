import math, sys

while True:
    response = input('Enter a positive whole number to factor(or QUIT)')
    if response.upper() == 'QUIT':
        sys.exit()
        
    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)
    
    factors = []
    
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
            
    factors = list(set(factors))
    factors.sort()
        
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))