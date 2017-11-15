#Python 3 - Loops

#1. while loop : Repeats a statement
#2. for loop   : Executes a sequence of statements
#3. nested loop: use one or more loop inside 

#1. while loop:
'''while test_expression:
    Body of while'''

#1.1 example while loop:
'''a = 0
while a < 10:
    print(" value is a :" ,a)
    a = a - 2'''
#1.2 Example: Python while Loop
# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n
# To take input from the user,
# n = int(input("Enter n: "))
'''n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1 # update counter
# print the sum
print("The sum is", sum)'''

#1.3 Example to illustrate
# the use of else statement
# with the while loop
'''counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")'''

#1.3.2 with the else statement
'''count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")'''

#1.4 Example while loop:
'''count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
print ("Good bye!")'''

#1.5 The Infinite Loop:
'''var = 1
while var == 1 :  # This constructs an infinite loop
   num = int(input("Enter a number  :"))
   print ("You entered: ", num)
   print ("Good bye!")'''

#1.6 example of a one-line while:
'''flag = 1
while (flag): print ('Given flag is really true!')
print ("Good bye!")'''










