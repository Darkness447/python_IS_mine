# thisList=["how","are","you"]

# newList=[x for x in thisList if "are" in x]


# newList = ['hello' for x in thisList]

# .sort() method can be used to sort the list in python


# print(newList)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)

# customize your own sort function thisList.sort(key = myFunc)

# print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# .reverse method is also great to learn

# .copy can be used to copy a list 

# Make a copy of a list with the list() method:

# join the list important

l = [1,2,3,5]
l1 = [6,4,23,2]

print(l+l1)

# use can use .extend() method 