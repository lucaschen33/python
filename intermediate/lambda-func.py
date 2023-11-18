def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85
 #   return x+5

#func2 = lambda x: x+5

#print(func2(9))
print(func(2))


#Multiple parameters:

def func(x):
    func2 = lambda x: x+5
    return func2(x) + 85

func3 = lambda x,y:x+y
print(func3(5,5))


print(func(2))


#lambda with map:
#using lambda, you dont need to use func or define a variable



a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x: x+5, a))
print(newList)



#lambda with filter func:

a = [1,2,3,4,5,6,7,8,9,10]

newList = list(filter(lambda x: x%2==0, a))
print(newList)