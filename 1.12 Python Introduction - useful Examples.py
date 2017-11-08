# 1)This program prints Hello, world!
#print('Hello, world!')


#2) This program adds two numbers
num1 = 1.5
num2 = 6.3
# Add two numbers
sum = float(num1) + float(num2)
# Display the sum
#print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


"""# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
# Add two numbers
sum = float(num1) + float(num2)
# Display the sum 
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))"""

#print('The sum is %.1f' %(float(input('Enter first number: '))+float(input('Enter second number: '))))


# 3)Python Program to calculate the square root
# Note: change this value for a different result
num = 8 
# uncomment to take the input from the user
#num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
#print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))



# Find square root of real or complex numbers
# Import the complex math module
import cmath
# change this value for a different result
num = 1+2j
# uncommment to take input from the user
#num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
#print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))


#4) Python Program to find the area of triangle
a = 5
b = 6
c = 7
# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#print('The area of the triangle is %0.2f' %area)


# 5)Solve the quadratic equation ax**2 + bx + c = 0
# import complex math module
import cmath
a = 1
b = 5
c = 6
# To take coefficient input from the users
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
#print('The solution are {0} and {1}'.format(sol1,sol2))




#6) Python program to swap two variables
# To take input from the user
# x = input('Enter value of x: ')
# y = input('Enter value of y: ')
x = 5
y = 10
# create a temporary variable and swap the values
temp = x
x = y
y = temp
#print('The value of x after swapping: {}'.format(x))
#print('The value of y after swapping: {}'.format(y))

#7) Program to generate a random number between 0 and 9
# import the random module
import random
#print(random.randint(0,9))

#8) Python Program to Convert Kilometers to Miles

kilometers = 5.5
# To take kilometers from the user, uncomment the code below
#kilometers = input("Enter value in kilometers")
# conversion factor
conv_fac = 0.621371
# calculate miles
miles = kilometers * conv_fac
#print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))

#9) Python Program to convert temperature in celsius to fahrenheit
# change this value for a different result
celsius = 37.5
# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
#print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))







