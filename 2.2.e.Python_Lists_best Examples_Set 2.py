
#List Methods in Python | Set 2 (del, remove(), sort(), insert(), pop(), extend()…)

#Some of the list methods are mentioned in set 1 below
#List Methods in Python | Set 1 (in, not in, len(), min(), max()…)
#More methods are discussed in this article.

#1. del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
#2. pop() :- This method deletes the element at the position mentioned in its arguments.

# Python code to demonstrate the working of
# del and pop()
 
'''# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8]
 
# using del to delete elements from pos. 2 to 5
# deletes 3,5,4
del lis[2 : 5]
 
# displaying list after deleting 
print ("List elements after deleting are : ",end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using pop() to delete element at pos 2
# deletes 3
lis.pop(2)
 
# displaying list after popping  
print ("List elements after popping are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")'''

#3. insert(a, x) :- This function inserts an element at the position mentioned in its arguments. It takes 2 arguments, position and element to be added at respective position.
#4. remove() :- This function is used to delete the first occurrence of number mentioned in its arguments.

# Python code to demonstrate the working of
# insert() and remove()
 
'''# initializing list 
lis = [2, 1, 3, 5, 3, 8]
 
# using insert() to insert 4 at 3rd pos
lis.insert(3, 4)
 
# displaying list after inserting
print("List elements after inserting 4 are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using remove() to remove first occurrence of 3
# removes 3 at pos 2
lis.remove(3)
 
# displaying list after removing 
print ("List elements after removing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")'''

#5. sort() :- This function sorts the list in increasing order.
#6. reverse() :- This function reverses the elements of list.

# Python code to demonstrate the working of
# sort() and reverse()
 
'''# initializing list 
lis = [2, 1, 3, 5, 3, 8]
 
# using sort() to sort the list
lis.sort()
 
# displaying list after sorting
print ("List elements after sorting are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
     
print("\r")
 
# using reverse() to reverse the list
lis.reverse()
 
# displaying list after reversing
print ("List elements after reversing are : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")''' 

#7. extend(b) :- This function is used to extend the list with the elements present in another list. This function takes another list as its argument.
#8. clear() :- This function is used to erase all the elements of list. After this operation, list becomes empty.

# Python code to demonstrate the working of
# extend() and clear()
 
'''# initializing list 1
lis1 = [2, 1, 3, 5]
 
# initializing list 1
lis2 = [6, 4, 3]
 
# using extend() to add elements of lis2 in lis1
lis1.extend(lis2)
 
# displaying list after sorting
print ("List elements after extending are : ", end="")
for i in range(0, len(lis1)):
    print(lis1[i], end=" ")
     
print ("\r")
 
# using clear() to delete all lis1 contents
lis1.clear()
 
# displaying list after clearing
print ("List elements after clearing are : ", end="")
for i in range(0, len(lis1)):
    print(lis1[i], end=" ")'''

