#Containers:
#list
#set
#dict
#tuple - unmuttable

#types:
#1 counter
#2 deque
#3 namedTuple()
#4 orderdDict
#5 defaultdict

from collections import Counter

c = Counter('gallad')
print(c)
c = Counter(['a', 'a','b','c','c'])
print(c)
c = Counter({'a':1, "b" :2})
print(c)
c = Counter(cats=4, dogs=7)
print(c['cats'])

#print(c['pet'])
#if put diffferent key, instead of return error; will return a 0

#Methods:

print (list(c.elements()))

print(c.most_common(1))



#Subtract
c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']
c.subtract(d)
print(c)
c.update(d)
print(c)

#Operations:
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

print(c+d)
print(c-d)
print()

#Union and intersection

#Intersection:
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

print(c & d)

#Union
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

print(c | d)