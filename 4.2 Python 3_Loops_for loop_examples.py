#1. for loop with strings

'''for letter in "banana":
    print(letter)
print("done")'''

#1.1 for loop using a variable as collection:

'''fruit = "banana"
for letter in fruit:
    print(letter)
print( "Done" )'''

#1.2 use if condition:

'''fruit = "banana"
for letter in fruit:
    print(letter)
    if letter == "n":
        fruit = "orange"
        print(fruit)
print("Done")'''
            

#1.3 for loop using a range of numbers:

'''for x in range(10):
    print(x)'''

'''for x in range (1, 11, 2):
    print(x)'''

#1.4 The range() function:

'''for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)
print ("Good bye!")'''

#1.5 for loop with manual collections:

'''for x in ( 10, 100, 1000, 10000 ):
    print(x)

for x in ("apple", "pear", "orange", "banana", "mango", "cherry"):
    print(x)'''

# 2. Nested loops:
'''import sys
for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print (k, end=' ')
   print()'''

