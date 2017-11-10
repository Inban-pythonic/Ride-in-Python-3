#List Operations:

#Adding Lists:
#Lists can be added by using the concatenation operator(+) to join two lists.
"""list1=[10,20]  
list2=[30,40]  
list3=list1+list2  
print (list3)"""

#Note: '+'operator implies that both the operands passed must be list else error will be shown.
"""list1=[10,20]
list1+30  
print (list1)  """

#Replicating lists
#'*' operator by a specific number of time.
"""list1=[10,20]  
print (list1*1) """

#List slicing:
"""list1=[1,2,4,5,7]  
print (list1[0:2])  
print (list1[4])  
list1[1]=9  
print (list1)"""

#min(list):
"""list1=[101,981,'abcd','xyz','m']  
list2=['aman','shekhar',100.45,98.2]  
print ("Minimum value in List1: ",min(list1))  
print ("Minimum value in List2: ",min(list2))"""

#max(list):
"""list1=[101,981,'abcd','xyz','m']  
list2=['aman','shekhar',100.45,98.2]  
print "Maximum value in List : ",max(list1)  
print "Maximum value in List : ",max(list2)"""

#len(list):
"""list1=[101,981,'abcd','xyz','m']  
list2=['aman','shekhar',100.45,98.2]  
print ("No. of elements in List1: ",len(list1))  
print ("No. of elements in List2: ",len(list2))"""

#cmp(list1,list2):

#Explanation: If elements are of the same type, perform the comparison and return the result. If elements are different types, check whether they are numbers.

'''If numbers, perform comparison.
If either element is a number, then the other element is returned.
Otherwise, types are sorted alphabetically .
If we reached the end of one of the lists, the longer list is "larger." If both list are same it returns'''

"""list1=[101,981,'abcd','xyz','m']  
list2=['aman','shekhar',100.45,98.2]  
list3=[101,981,'abcd','xyz','m']  
print (cmp(list1,list2))  
print (cmp(list2,list1))  
print (cmp(list3,list1))""" 

#list(sequence):
"""seq=(145,"abcd",'a')  
data=list(seq)  
print ("List formed is : ",data)"""  
 
#There are following built-in methods of List:

#Methods	Description
#index(object)	Returns the index value of the object.
#count(object)	It returns the number of times an object is repeated in list.
#pop()/pop(index) Returns the last object or the specified indexed object. It removes the popped object.
#insert(index,object) Insert an object at the given index.
#extend(sequence) It adds the sequence to existing list.
#remove(object)	It removes the object from the given List.
#reverse()   Reverse the position of all the elements of a list.
#sort()	It is used to sort the elements of the List.

#index(object):

'''data = [786,'abc','a',123.5]  
print ("Index of 123.5:", data.index(123.5))  
print ("Index of a is", data.index('a'))'''

#count(object):
'''data = [786,'abc','a',123.5,786,'rahul','b',786]  
print ("Number of times 123.5 occured is", data.count(123.5)) 
print ("Number of times 786 occured is", data.count(786))'''

#pop()/pop(int):
'''data = [786,'abc','a',123.5,786]  
print ("Last element is", data.pop()) 
print ("2nd position element:", data.pop(1))  
print (data)'''

#insert(index,object):
'''data=['abc',123,10.5,'a']  
data.insert(2,'hello')  
print (data)'''  

#extend(sequence):
'''data1=['abc',123,10.5,'a']  
data2=['ram',541]  
data1.extend(data2)  
print (data1)  
print (data2) ''' 

#remove(object):
'''data1=['abc',123,10.5,'a','xyz']  
data2=['ram',541]  
print (data1)  
data1.remove('xyz')  
print (data1 ) 
print (data2)  
data2.remove('ram')  
print (data2) ''' 
 
#reverse():
'''list1=[10,20,30,40,50]  
list1.reverse()  
print(list1)'''

#sort():
'''list1=[10,50,13,'rahul','aakash']  
list1.sort()  
print (list1)  ''' 
