# sets in python
# A set is a collection which is unordered, unchangeable*, and unindexed.
# unchangable but we can add and remove new values important

myApple = {"apple","cat","banana"}

# set are unordered every time 
# once set has been created you cannot change the item but you can add and remove the item
# duplicates are not allowed in set

print({1,True})
# what is the output
# len(myApple) get length of the set


myset = {"apple", "banana", "cherry"}
print(type(myset))

thisSet = set(("apple","banana","cherry"))
print(thisSet)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#  add method set.add("any item")
# To add items from another set into the current set, use the update() method. currentSet.update(newSet)
# newSet can be anything apart from set ------- tuple,list

# another method is remove or discard method 
# thisset.clear()

for x in thisSet:
  print(x)

# joins in set
# union() and update()
# intersection()
# difference()
# symmetric_difference()


# set3 = set1 | set2  union operation
# set1.union(set2,set3,set4)
# upadate
# intersacton method and &
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.


# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# we can also use - operator here


# The symmetric_difference() method will keep only the elements that are NOT present in both sets.




