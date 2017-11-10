#Mathematical Functions in Python | Set 1 (Numeric Functions)

# 1)ceil() and floor()
# importing "math" for mathematical operations

'''import math
a = 2.3
 
# returning the ceil of 2.3
print ("The ceil of 2.3 is : ", end="")
print (math.ceil(a))
 
# returning the floor of 2.3
print ("The floor of 2.3 is : ", end="")
print (math.floor(a))'''

# 2) Python code to demonstrate the working of
# fabs() and factorial()
 
# importing "math" for mathematical operations
'''import math
 
a = -10
b= 5
 
# returning the absolute value.
print ("The absolute value of -10 is : ", end="")
print (math.fabs(a))
 
# returning the factorial of 5
print ("The factorial of 5 is : ", end="")
print (math.factorial(b))'''

# Python code to demonstrate the working of
# copysign() and gcd()
 
# importing "math" for mathematical operations
'''import math
 
a = -10
b = 5.5
c = 15
d = 5
 
# returning the copysigned value.
print ("The copysigned value of -10 and 5.5 is : ", end="")
print (math.copysign(5.5, -10))
 
# returning the gcd of 15 and 5
print ("The gcd of 5 and 15 is : ", end="")
print (math.gcd(5,15))'''

# Python code to demonstrate the working of
# exp() and log()
  
# importing "math" for mathematical operations
'''import math
  
# returning the exp of 4
print ("The e**4 value is : ", end="")
print (math.exp(4))
  
# returning the log of 2,3
print ("The value of log 2 with base 3 is : ", end="")
print (math.log(2,3))'''

# Python code to demonstrate the working of
# log2() and log10()
  
# importing "math" for mathematical operations
'''import math
  
# returning the log2 of 16
print ("The value of log2 of 16 is : ", end="")
print (math.log2(16))
  
# returning the log10 of 10000
print ("The value of log10 of 10000 is : ", end="")
print (math.log10(10000))'''

# Python code to demonstrate the working of
# pow() and sqrt()
  
# importing "math" for mathematical operations
'''import math
  
# returning the value of 3**2
print ("The value of 3 to the power 2 is : ", end="")
print (math.pow(3,2))
  
# returning the square root of 25
print ("The value of square root of 25 : ", end="")
print (math.sqrt(25))'''

# Python code to demonstrate the working of
# sin() and cos()
  
# importing "math" for mathematical operations
'''import math
 
a = math.pi/6
  
# returning the value of sine of pi/6
print ("The value of sine of pi/6 is : ", end="")
print (math.sin(a))
  
# returning the value of cosine of pi/6
print ("The value of cosine of pi/6 is : ", end="")
print (math.cos(a))'''

# Python code to demonstrate the working of
# tan() and hypot()
  
# importing "math" for mathematical operations
'''import math
 
a = math.pi/6
b = 3
c = 4
  
# returning the value of tangent of pi/6
print ("The value of tangent of pi/6 is : ", end="")
print (math.tan(a))
  
# returning the value of hypotenuse of 3 and 4
print ("The value of hypotenuse of 3 and 4 is : ", end="")
print (math.hypot(b,c))'''

# Python code to demonstrate the working of
# degrees() and radians()
  
# importing "math" for mathematical operations
'''import math
  
a = math.pi/6
b = 30
 
# returning the converted value from radians to degrees
print ("The converted value from radians to degrees is : ", end="")
print (math.degrees(a))
  
# returning the converted value from degrees to radians
print ("The converted value from degrees to radians is : ", end="")
print (math.radians(b))'''

# Python code to demonstrate the working of
# gamma()
  
# importing "math" for mathematical operations
'''import math
 
a = 4
 
# returning the gamma() of 4
print ("The gamma() of 4 is : ", end="")
print (math.gamma(a))'''

# Python code to demonstrate the working of
# const. pi and e
  
# importing "math" for mathematical operations
'''import math
 
# returning the value of const. pi
print ("The value of const. pi is : ", end="")
print (math.pi)
 
# returning the value of const. e
print ("The value of const. e is : ", end="")
print (math.e)'''

# Python code to demonstrate the working of
# inf, nan, isinf(), isnan()
  
# importing "math" for mathematical operations
'''import math
 
# checking if number is nan
if (math.isnan(math.nan)):
       print ("The number is nan")
else : print ("The number is not nan")
 
# checking if number is positive infinity
if (math.isinf(math.inf)):
       print ("The number is positive infinity")
else : print ("The number is not positive infinity")'''



