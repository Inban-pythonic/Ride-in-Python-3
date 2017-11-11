#1.1 List Basic Examples:
'''fruitlist = ["apple", "banana", "cherry"]
print(len(fruitlist))
for element in fruitlist:
    print(element)
print(fruitlist[2])

numlist = [312, 465, 765, 897]
print(max(numlist))
print(min(numlist))
print(len(numlist))
print(sum(numlist))
print(312 in numlist)
print(999 in numlist)'''

#1.2 Lists are mutable:

#Because you can change the contents of a list.
#overwrite
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist[2] = "strawberry"
print(fruitlist)

fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist[1:3] = ["raspberry", "strawberry", "blueberry"]
print(fruitlist)
#insert
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist[1:1] = ["raspberry", "strawberry", "blueberry"]
print(fruitlist)
#delete
fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist[1:3] = []
print(fruitlist)'''


#1.3.lists and operators

# operator +
'''fruitlist = ["apple", "banana", "cherry",]+["durian", "orange"]
print(fruitlist)
numlist = 10 * [0]
print(numlist)

fruitlist = ["apple", "banana", ]
fruitlist += "cherry"
print(fruitlist)

fruitlist = ["apple", "banana", ]
fruitlist += ["cherry"]
print(fruitlist)'''

#1.4 List methods
#1.4.1 append()

'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist.append("orange")
print(fruitlist)'''

#1.4.2 extend()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist.extend( ["raspberry", "strawberry", "blueberry"])
print(fruitlist)'''

#1.4.3 insert()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist.insert(2,"blueberry")
print(fruitlist)'''

#1.4.4 remove()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
fruitlist.remove("banana")
print(fruitlist)'''


#1.4.5 pop()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist)
print(fruitlist.pop(0))
print(fruitlist)'''

#1.4.6 del
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
del fruitlist[3]
print(fruitlist)'''

#1.4.7 index()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist.index("banana"))'''

#1.4.8 count()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
print(fruitlist.count("banana"))'''

#1.4.9 sort()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
fruitlist.sort()
print(fruitlist)'''

#1.4.10 reverse()
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
fruitlist.reverse()
print(fruitlist)'''

#2.5 ALIASING
'''fruitlist = ["apple", "banana", "cherry", "durian", "orange"]
newfruitlist = fruitlist
print(fruitlist)
print(newfruitlist)
newfruitlist[2] = "orange"
print(fruitlist)
print(newfruitlist)'''

#2.6 NSTED LISTS
'''fruitlist = ["apple", "banana", ["cherry", "durian", "orange"]]
print(fruitlist[0][1])
print(fruitlist[1][2])'''

#2.7 list Comprehension

#make it try: flowerlist or birdlist like fruitlist 






































































