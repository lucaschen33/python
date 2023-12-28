import collections
from collections import deque



# #  create a deque
# d = deque("hello")
# print(d)
# #  add to front and back of a deque
# d.append('4')
# d.append(5)   
# d.append("Lucas")
# d.appendleft("Jolie")
# print(d)
# #  remove from deque from front and back
# d.pop()
# d.popleft()
# print(d)
# #  clear a deque
# d.clear()
# print(d)
# # add more to a deque without multiple lines of code
# d.extend('456')
# d.extend("hello")
# d.extend([1,2,4])
# d.extendleft("tfel")
# print(d)
# #  rotate elememt= move deque over
# #  you have to rotate with a integer that is negetive or positive

# #  positive = to the right
# d.rotate(1)
# print(d)
# #  negetive = to the left
# #  after rotate to the right I rotate it back with -1
# d.rotate(-1)
# print(d)
# d.clear()
# print(d)

# #  to make a max amount of things use maxlen=(integer)

d=deque("hello", maxlen=(5))
print(d)
#  If I add to the deque, depending how many things I add in, that is how many will be removed to keep the max amount of things I put in 5
d.append(1)
print(d)