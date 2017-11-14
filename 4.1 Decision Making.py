#Python 3 - Decision Making

#3.1 Python If Statements
'''if test expression:
    statement(s)'''

'''a = 10
if a == 10:
    print("hello Python")

# If the number is positive, we print an appropriate message
num = 3
if num > 0:
    print(num, "is a positive number.")
    print("This is always printed.")
num = -1
if num > 0:
    print(num, "is a positive number.")
    print("This is also always printed.")'''

#3.2 Python if...else Statement

'''# Program checks if the number is positive or negative
# And displays an appropriate message
num = 3
# Try these two variations as well. 
# num = -5
# num = 0
if num >= 0:
    print("Positive or Zero")
else: print("Negative number")'''


#3.3 Python if...elif...else

'''# In this program, 
# we check if the number is positive or
# negative or zero and 
# display an appropriate message
num = 3.4
# Try these two variations as well:
# num = 0
# num = -4.5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")'''

#3.4 Python Nested if statements

# In this program, we input a number# check if the number is positive or# negative or zero and display# an appropriate message# This time we use nested if

''' num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")'''


'''num = int(input("enter number"))
if num%2 == 0:
   if num%3 == 0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
    if num%3 == 0:
      print ("divisible by 3 not divisible by 2")
    else:
      print  ("not Divisible by 2 not divisible by 3")'''



























