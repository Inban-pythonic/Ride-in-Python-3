#Creating a Tuple
'''# empty tuple
# Output: ()
my_tuple = ()
print(my_tuple)

# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)
'''


#2)Creating a tuple with one element is a bit tricky.
'''#Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.
# only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")
print(type(my_tuple))

# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello",)  
print(type(my_tuple))

# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",
print(type(my_tuple))''''

#3) Accessing Elements in a Tuple
#3.1. Indexing
"""my_tuple = ('p','e','r','m','i','t')

# Output: 'p'
print(my_tuple[0])

# Output: 't'
print(my_tuple[5])

# index must be in range
# If you uncomment line 14,
# you will get an error.
# IndexError: list index out of range

#print(my_tuple[6])

# index must be an integer
# If you uncomment line 21,
# you will get an error.

# TypeError: list indices must be integers, not float

#my_tuple

# 3.1.2.nested index
# Output: 's'
print(n_tuple[0][3])

# nested index
Output: 4
print(n_tuple[1][1])"""

#3.2. Negative Indexing
'''my_tuple = ('p','e','r','m','i','t')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])'''

#3.3 Slicing
#We can access a range of items in a tuple by using the slicing operator - colon ":".
'''my_tuple = ('i','n','b','a','n','y','o','g','i')

# elements 2nd to 4th
# Output: ('r', 'o', 'g')
print(my_tuple[1:4])

# elements beginning to 2nd
# Output: ('p', 'r')
print(my_tuple[:-7])

# elements 8th to end
# Output: ('i', 'z')
print(my_tuple[7:])

# elements beginning to end
# Output: ('i','n','b','a','n','y','o','g','i')
print(my_tuple[:])'''

#3.4 Changing a Tuple Unlike lists, tuples are immutable

'''my_tuple = (4, 2, 3, [6, 5])

# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# 3.4.1.but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)

# tuples can be reassigned
# Output: ('i','n','b','a','n','y','o','g','i')
my_tuple = ('i','n','b','a','n','y','o','g','i')
print(my_tuple)

#3.4.2.Both + and * operations result into a new tuple.
# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# 3.4.3Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)''''

#3.5 Python Tuple Methods
#Method	Description
#count(x)	Return the number of items that is equal to x
#index(x)	Return index of first item that is equal to x
'''my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('p'))

# Index
# Output: 3
print(my_tuple.index('l'))'''

#3.6 Other Tuple Operations
#3.6.1. Tuple Membership Test
#We can test if an item exists in a tuple or not, using the keyword in.

'''my_tuple = ('a','p','p','l','e',)
# In operation
# Output: True
print('a' in my_tuple)
# Output: False
print('b' in my_tuple)
# Not in operation
# Output: True
print('g' not in my_tuple)'''

#3.6.2. Iterating Through a Tuple
"""#Using a for loop we can iterate though each item in a tuple.

# Output: 
# Hello John
# Hello Kate
for name in ('John','Kate'):
     print("Hello",name)"""




