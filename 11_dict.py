thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":["red", "white", "blue"]
}

# dictonary are used to store data in key value format important
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(thisdict["brand"])

# duplicate keys are not allowed but we can change , remove , add ,data here
type(thisdict)
len(thisdict)

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
key = thisdict.keys() 
# return all the keys

x = thisdict.values()
# give all the values

x = thisdict.items() 
# return all item as a tuple in list

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# .update() will update the item

# remove item by .pop() .popitem() del .clear()

# for x, y in thisdict.items():
#   print(x, y)
# return a pair of key and value that is destructured in x,y

# dict1 = dict2 this doesn't copy the whole directory it gives this as a reference

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
 
 