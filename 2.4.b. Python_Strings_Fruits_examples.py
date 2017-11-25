#Strings Fruit Examples:

#1.Basic string Example:
'''s1 = "apple"
s2 = "banana"
print(s1)
print(s2)
print(s1 + s2)
print(3*s1)
print(s2 * 3)
print(2*s1+2*s2)'''

#Also use format() function to format strings. It also explained how you can
#get the length of a string using the len() function.
'''s1 = "orange"
s2 = "banana"
for letter in s2:
    if letter in s2:
        print(s1, "and", s2, "share the letter", letter)'''

#2. Multi-line Strings:

"""long = "I'm fed up with being treated like sheep. What's the \ point of going abroad if you're just another tourist carted\around in buses surrounded by sweaty mindless oafs from\
Kettering and Conventry in their Cloth caps and their cardigans\and their transistor radios and their Sunday"
print(long)"""

#3. Escape sequences.
#"\n" is a so-called "escape sequence."
#An escape sequence is a string character written as a backslash followed by
#code, which can be one or multiple characters.

#4. String indices
"""fruit = "orange"
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[-2])
print(fruit[-6])
print(fruit[0])
print(fruit[-3])"""

#4.1 You can also use variables as indices, and even calculations or function calls:

"""from math import sqrt

fruit = "orange"
x = 3

print(fruit[3-2])
print(fruit[int(sqrt(4))])
print(fruit[2**2])
print(fruit[int((x-len(fruit))/3)])"""

#4.2 Outside the bounds of the string:

"""fruit = "orange"
print(fruit[:])
print(fruit[0:])
print(fruit[:6])
print(fruit[:100])
print(fruit[:len(fruit)])
print(fruit[1:-1])
print(fruit[2], fruit[1:6])"""

#4.3 Traversing Strings

#I already explained how you can traverse the characters of a string using a for loop:

'''fruit = 'apple'
for char in fruit:
    print(char, '-', end = '')'''

#4.3.1 use indices Traverse string

'''fruit = 'apple'

for i in range(0, len(fruit)):
    print(fruit[1], "-", end="")
print()

i = 0
while i< len(fruit):
    print(fruit[i], "-", end="")
    i+=1'''

#4.4 Extended slices

"""fruit = "banana"
print(fruit[::2])
print(fruit[1::2])
print(fruit[::-1])
print(fruit[::-2])"""

#Reversing a string :

'''fruit = "banana"
print(fruit[::-1])
for i in range(5, -1, -1):
    print(fruit[i])'''

#5 Strings are immutable

'''fruit = "orange"
fruit[2] = "a" #Runtime error!
print(fruit)'''

#for instance:

'''fruit = "orange"
fruit = fruit[:2] + "a" + fruit[3:]
print(fruit)'''

#6 string methods
#6.1 strip()
'''s = "   I have many Fruits  \n         "
print("["+s+"]")
s = s.strip()
print("["+s+"]")'''

#6.2  upper() and lower()
'''s = "The Meaning of Life"
print(s)
print(s.upper())
print(s.lower())'''

#6.3 find()
'''s = "We can decorate our garden by growing fruits "
print(s.find("can"))
print(s.find("t"))
print(s.find("t", 12))
print(s.find("g"))'''

#6.4 replace()
'''a = 'We can decorate our garden by growing fruits'
print(s.replace('fruits', 'Trees'))'''

#6.5 split()
"""s = 'We can decorate our garden by growing fruits'
wordlist = s.split()
for word in wordlist:
    print(word)"""

#6.6 join()
#join() is the opposite of split():
'''s = 'We can; decorate our; garden by ; growing fruits'
wordlist = s.split( ';' )
s = "".join(wordlist)
print(s)'''







































