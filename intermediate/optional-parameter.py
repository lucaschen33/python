#Optional parameter:
def func(x=4):
    return x *2
call = func(6)
print(call)
# if you put a number in "call = func(HERE)" then it will overwrite the other one



#Multiple Optional Paramters:
def func(word, freq=1):
    print(word*freq)
    
call = func("lucas", 4)


#default freq:
def func(word, freq=10):
    print (word*freq)

call = func("lucas", 3)


def func(word, add =5, freq=10):
    print (word(freq+add))

call = func("jolie", 3, 5)








