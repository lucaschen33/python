#Named Tuples assign meaning to each position in a tuble and allow for
#more readable, self-documenting code. They can be used wherever regular tupeles
#are used and they add the ability to access fields by name instead of position index,


from collections import namedtuple

Point = namedtuple('Point', 'x y z')
#Also works with lists.
newP = Point(3,4,5)
print(newP)
print(newP.x, newP.y, newP.z)
print(newP[0])
print(newP._asdict())
print(newP._fields)

#Replace method

newP = newP._replace(x=6)
print(newP)

#new point

p2 = Point._make(['a', 'b', 'c'])
print(p2)