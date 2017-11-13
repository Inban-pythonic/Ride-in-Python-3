          #SETS

#1. Basics of sets
'''fruitset = { "apple", "banana", "cherry"}
print(fruitset)
#1.1 create a set consisting of the different characters in a string:
helloset = set("helloworld")# next use space ex: hello world
print(helloset)
#1.2 for loop use
fruitset = { "apple", "banana", "cherry", "durian", "mango"}
for element in fruitset:
    print(element)
print()

fruitlist = list(fruitset)
fruitlist.sort()
for element in fruitlist:
    print(element)'''

#2. SET METHODS:
#2.1 add() and Update()
'''fruitset = { "apple", "banana", "cherry", "durian", "mango"}
print(fruitset)
fruitset.add("apple")
fruitset.add("elderberry")
print(fruitset)
fruitset.update(["apple", "apple", "apple", "strawberry",
                 "strawberry", "apple", "mango"])
print(fruitset)'''

#2.2 remove(), Discard(), and clear()
'''fruitset = { "apple", "banana", "cherry", "durian", "mango"}
print(fruitset)
fruitset.remove("apple")
print(fruitset)'''
#clear() removes all elements of the set at once.

#2.3 pop()
'''fruitset = { "apple", "banana", "cherry", "durian", "mango"}
while len(fruitset)>0:
    print(fruitset.pop())'''

#2.4 copy()
'''fruitset = { "apple", "banana", "cherry", "durian", "mango"}
fruitlist = list(fruitset)
print(fruitlist.copy())'''

#2.5 union()
'''fruitset1= { "apple", "banana", "cherry",}
fruitset2= { "banana", "cherry", "druian"}
fruitunion = fruitset1.union(fruitset2)
print(fruitunion)

fruitunion = fruitset1 | fruitset2
print(fruitunion)'''

#2.6 intersection()
'''fruitset1= { "apple", "banana", "cherry",}
fruitset2= { "banana", "cherry", "druian"}
fruitintersection = fruitset1.intersection(fruitset2)
print(fruitunion)

fruitunion = fruitset1 & fruitset2
print(fruitintersection)'''

#2.7 difference()
'''fruitset1= { "apple", "banana", "cherry",}
fruitset2= { "banana", "cherry", "druian"}
fruitdifference = fruitset1.difference(fruitset2)
print(fruitdifference)

fruitdifference = fruitset1 & fruitset2
print(fruitdifference)'''

#2.8 isdisjoint(), issubset(), and issuperset()
'''fruitset1= { "apple", "banana", "cherry",}
fruitset2= { "banana", "cherry", "druian"}
print(fruitset1.isdisjoint(fruitset2))
print(fruitset1.issubset(fruitset2))
print(fruitset2.issubset(fruitset1))
print(fruitset1.issubset(fruitset1))
print(fruitset1.issuperset(fruitset2))
print(fruitset2.issuperset(fruitset1))
print(fruitset1.issuperset(fruitset1))'''

#2.9 Frozensets

#Python supports a variant on the set type, namely the frozent. create frozenset()
'''fruitset1= { "apple", "banana", "cherry",}
fruitset2= { "banana", "cherry", "druian"}
print(fruitset1.union(fruitset2))'''






































































