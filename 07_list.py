#  change the item value 
#  change the range of value also important


# insert method will insert the item at specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# append will add the item in the end of the list
# extend method we can append list,dir,set

thislist1 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist1.extend(tropical)
print(thislist1)

# remove method removes the first occurence of item .remove("banana
# ")
# remove the specified index pop(index)
# del keyword also remove the specified index del thisList[0]
# .clear() will clear all the list 

# loop in list

for x in thislist:
  print(x)

# range and len will create suitable iterable
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

