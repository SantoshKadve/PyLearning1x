#String
#Bunch of char
name = "pramod"
print(name)
#String Functions
#Python string are Immutable in nature, once created, they cant be changed

#eg
# name[0] = "h" #TypeError: 'str' object does not support item assignment
# print(name)

#capitalize()
cap_name=name.capitalize()
print(cap_name) #o/p  - Pramod

#upper() case function
print(name.upper()) # o/p - PRAMOD

# lower() case
print(name.lower())

# id() function returns the identity of object-
# it shows Python strings are immutable and every result of name' is creating new strg

result1=name.lower()
print(id(result1))
print(id(name))
print(id(cap_name))

#swap case
# it returns swapping of case - lower to upper and upper to lower case
name2 = "pRaMoD"
print(name2.swapcase()) # o/p - PrAmOd

#Title function - returns Title case version of string, where 1st letter become Capital and remaining will be lower
name3= "HELLO WORLD"
print(name3.title()) #o/p - Hello World

name3= "hello world"
print(name3.title()) #o/p - Hello World

#find() - Returns the lowest index of a substring in the string
# it Returns -1 if string not found
index=name3.find("world") #o/p - 6
index=name3.find("sworld") #o/p- -1 if word not found
print(index)

# len() - Length function returns the umber of char in a string
print(len(name3)) # o/p - 11 it include blank space as well



