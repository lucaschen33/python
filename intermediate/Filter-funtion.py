def add7(x):
    return x+7

def isOdd(x) :
    #return False
    #return True
    #return x%2 != 0
    return 1

a = [1,2,3,4,5,6,7,8,9,10]

#b = list(filter(isOdd,a))

c = list(map(add7,filter(isOdd,a)))

print(a)
#print(b)
print(c)