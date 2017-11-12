#1) How to create a string?
# all of the following are equivalent
"""my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
"""

#2) How to access characters in a string?
"""str = 'inbanyogi'
print('str = ', str)

#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

#3 How to change or delete a string?
>>> my_string = 'programiz'
>>> my_string[5] = 'a'
...
TypeError: 'str' object does not support item assignment
>>> my_string = 'Python'
>>> my_string
'Python'
>>> del my_string[1]
...
TypeError: 'str' object doesn't support item deletion
>>> del my_string
>>> my_string
...
NameError: name 'my_string' is not defined"""

#3 Python String Operations
#3.1 Concatenation of Two or More Strings
#Joining of two or more strings into a single one is called concatenation.
#The + operator does this in Python. Simply writing two string literals together also concatenates them.
#The * operator can be used to repeat the string for a given number of times.

str1 = 'Hello'
str2 ='World!'
# 3.1.1. using +
print('str1 + str2 = ', str1 + str2)
# 3.1.2. using *
print('str1 * 3 =', str1 * 3)

#Writing two string literals together also concatenates them like + operator.
#If we want to concatenate strings in different lines, we can use parentheses.

>>> # 3.1.3. two string literals together
>>> 'Hello ''World!'
'Hello World!'

>>> # 3.1.4. using parentheses
>>> s = ('Hello '
...      'World')
>>> s
'Hello World'
#4) Iterating Through String
#Using for loop we can iterate through a string. Here is an example to count the number of 'l' in a string.

"""count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')"""

#5)String Membership Test
#We can test if a sub string exists within a string or not, using the keyword in.

'''>>> 'a' in 'program'
True
>>> 'at' not in 'battle'
False'''

#6) Built-in functions to Work with Python
#Various built-in functions that work with sequence, works with string as well.
#Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
#Similarly, len() returns the length (number of characters) of the string.

'''str = 'cold'
# 6.1 enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#character count
print('len(str) = ', len(str))'''

#7) Python String Formatting
#Escape Sequence
#If we want to print a text like -He said, "What's there?"- we can neither use single quote or double quotes. This will result into SyntaxError as the text itself contains both single and double quotes.

""">>> print("He said, "What's there?"")
...
SyntaxError: invalid syntax
>>> print('He said, "What's there?"')
...
SyntaxError: invalid syntax
One way to get around this problem is to use triple quotes. Alternatively, we can use escape sequences.

An escape sequence starts with a backslash and is interpreted differently. If we use single quote to represent a string, all the single quotes inside the string must be escaped. Similar is the case with double quotes. Here is how it can be done to represent the above text."""

# 8) using triple quotes
"""print('''He said, "What's there?"''')
# escaping single quotes
print('He said, "What\'s there?"')
# escaping double quotes
print("He said, \"What's there?\"")"""


#9) The format() Method for Formatting Strings
#The format() method that is available with the string object is very versatile and powerful in formatting strings. Format strings contains curly braces {} as placeholders or replacement fields which gets replaced.

#We can use positional arguments or keyword arguments to specify the order.
"""# 9.1.default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)
# 9.2. order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)
# 9.3. order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)
The format() method can have optional format specifications. They are separated from field name using colon. For example, we can left-justify <, right-justify > or center ^ a string in the given space. We can also format integers as binary, hexadecimal etc. and floats can be rounded or displayed in the exponent format. There are a ton of formatting you can use. Visit here for all the string formatting available with the format() method.

>>> # 9.4formatting integers
>>> "Binary representation of {0} is {0:b}".format(12)
'Binary representation of 12 is 1100'

>>> #9.5 formatting floats
>>> "Exponent representation: {0:e}".format(1566.345)
'Exponent representation: 1.566345e+03'

>>> #9.6 round off
>>> "One third is: {0:.3f}".format(1/3)
'One third is: 0.333'

>>> #9.7 string alignment
>>> "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')
'|butter    |  bread   |       ham|'
#9.8 Old style formatting
#We can even format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this.

>>> x = 12.3456789
>>> print('The value of x is %3.2f' %x)
The value of x is 12.35
>>> print('The value of x is %3.4f' %x)
The value of x is 12.3457"""

#Common Python String Methods
#There are numerous methods available with the string object. The format() method that we mentioned above is one of them. Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc. Here is a complete list of all the built-in methods to work with strings in Python.

""">>> "iNBan".lower()
'inban'
>>> "inbAn".upper()
'INBAN'
>>> "This will split all words into a list".split()
['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
>>> ' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'This will join all words into a string'
>>> 'Happy New Year'.find('ew')
>>> 'Happy New Year'.replace('Happy','Brilliant')
'Brilliant New Year'"""



           
