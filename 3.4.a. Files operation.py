"""

'''poem = '''\
Programming is fun when the work is done
if you wanna make your work also fun:
    use Python:


#Open for 'w'riting
f = open('poem.txt', 'w')
#Write text to file
f.write(poem)
#Close the file
f.close()

#If no mode is specified,
#'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    #Zero length indicates EOF
    if len(line) == 0:
        break
    #The line already has newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')

#close the file
f.close()"""


#PICKLE

#Python provides a standard module called pickle which you can use to store any plain Python object in a file and then get it back later.
#This is called storing object persistently.

'''import pickle

#The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

#Write to the file
f = open(shoplistfile, 'wb')
#Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)'''









































