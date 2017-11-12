# Tuples
#1) A tuple is a group of one or more values that are treated as a whole.

#1.1 Using Tuples

t1 = ("apple", "orange")
print(type(t1))
t2 = "banana", "cherry"
print(type(t2))

#1.2 You can mix data types within tuples. You can even put tuples in tuples.

t1 = ("apple", 3, 1.4)
t2 = ("apple", 3, 1.4, ("banana", 5))

#1.3 To find out how many elements a tuple contains, you can use the len() function.
t1 = ("apple", "orange")
t2 = ("apple", 3, 1.4)
t3 = ("apple", 3, 1.4, ("banana", 5))
print(len(t1))
print(len(t2))
print(len(t3))

#1.4 You can use a for loop to access individualelements of a tuple in sequence.
t1 = ("apple", 3, 1.4, ("banana", 5))
for element in t1:
    print (element)

#1.5 You can also use the max() and min()& sum() functions
t1 = (234, 456,78, 409)
print(max(t1))
print(min(t1))
print(sum(t1))

#1.6 You can test whether an element is part of a tuple by using the in operator.
t1 = ("apple", "orange", "cherry")
print("banana" in t1)
print("orange" in t1)

#2)TUPLE ASSIGMENTS
t1 = ("apple")
print(type(t1))

#len
t1 = ("apple")
print(type(t1))
print(len(t1))

#left, right
t1, t2 = "apple", "banana"
print(t1)
print(t2)

t1, t2 = ("apple", "banana"), "cherry"
print(t1)
print(t2)

#3) Tuple indices

# 3.1 individual elements
t1 = ("apple", "banana", "cherry", "durian")
print(t1[2])

#3.2 slices
t1 = ("apple", "banana", "cherry", "durian" , "orange")
print(t1[1.4])

#3.3 while loop use
t1 = ("apple", "banana", "cherry", "durian" , "orange")
i = 0
while i < len(t1)
    print(t1[i])
    i+= 1

#4 TUPLE COMPARISONS:

t1 = ("apple", "banana")
t2 = ("apple", "banana")
t3 = ("apple", "cherry")
t4 = ("apple", "banana", "cherry")
print (t1==t2)
print(t1<t3)
print(t1>t4)
print(t3>t4)

#5 TULPLE are IMMUTABLE:
t1 = ("apple", "banana", "cherry")
t1[0] = "orange"

#6 APPLICATIONS OF TUPLES

from math import sqrt

#Distance between two point in N-dimensional space.
#The points should have the same dimension. i.e. they are tuples
#of numeric values, and they should have the same length.

def distance (p1, p2):
    total = 0
    for i in range (len(p1)):
        total += (p1[i] - p2[i]**2
    return sqrt(total)

# 1- dimensional space
point1 = (1,)
point2 = (5,)
print("1D: Distance between", point1, "and", point2, "is", distance(point1, point2))

#2- dimensional space
point1 = (1,2)
point2 = (5,5)
print("1D: Distance between", point1, "and", point2, "is", distance(point1, point2))

#3 - dimensional space
point1 = (1,2,4)
point2 = (5,5,8)
print("1D: Distance between", point1, "and", point2, "is", distance(point1, point2))



























                  






