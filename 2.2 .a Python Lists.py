"""#1)List Index

my_list = ['k','a','r','t','h','i','k']
# Output: k
print(my_list[0])
# Output: r
print(my_list[2])
# Output: h
print(my_list[4])
# Output: 1
print(my_list.index('a'))
# Output: 2
print(my_list.count('k'))
# Error! Only integer can be used for indexing:type error
print(my_list[4.0])
# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
# Output: a
print(n_list[0][1]) 
# Output: 5
print(n_list[1][3])"""


#2)Negative indexing

"""my_list = ['k','a','r','t','h','i','k']
# Output: k
print(my_list[-1])
# Output: r
print(my_list[-5])"""

#We can access a range of items in a list by using the slicing operator (colon).

"""my_list = ['k','a','r','t','h','i','k',]
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 5th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])"""

#We can use assignment operator (=) to change an item or a range of items.

"""# mistake values
even = [2, 4, 6, 8]
# change the 1st item 
even[0] = 1 
# Output: [1, 4, 6, 8]
print(even)
# change 2nd to 4th items
even[1:4] = [3, 5, 7] 
# Output: [1, 3, 5, 7]
print(even)"""

#We can add one item to a list using append() method or add several items using extend() method.

"""odd = [1, 3, 5]
odd.append(7)
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)"""

#We can also use + operator to combine two lists. This is also called concatenation.
#The * operator repeats a list for the given number of times.

""""odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
#Output: ["re", "re", "re"]
print(["re"] * 3)"""

#insert one item we use can insert() method

"""odd = [1, 9]
odd.insert(1,3)
# Output: [1, 3, 9] 
print(odd)
odd[2:2] = [5, 7]
# Output: [1, 3, 5, 7, 9]
print(odd)"""

#We can delete one or more items from a list using the keyword del.

"""my_list = ['p','r','o','b','l','e','m']
# delete one item
del my_list[2]
# Output: ['p', 'r', 'b', 'l', 'e', 'm'] 
print(my_list)
# delete multiple items
del my_list[1:5] 
# Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list 
# Error: List not defined
print(my_list)"""

#We can also use the clear() method to empty a list.

"""my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)"""

#We can test if an item exists in a list or not, using the keyword in.

"""my_list = ['p','r','o','b','l','e','m']
# Output: True
print('p' in my_list)
# Output: False
print('a' in my_list)
# Output: True
print('c' not in my_list)"""

#Using a for loop we can iterate though each item in a list.
"""for fruit in ['apple','banana','mango']:
    print("I like",fruit)"""








