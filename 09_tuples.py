mytuple = ("apple", "banana", "cherry")

print(mytuple)

# ordered and unchangable
# tuples are indexed

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# tuple length can be find using len keyword
print(len(thistuple))


#  tupple with one item should have , beside them so that 
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc",34,True,40,"Male")
print(tuple1)

# we can also use tupple constructor to make the tupple 
thistuple = tuple(("","",""))



# HOW TO ACCESS TUPLE ELEMENT

# by index
# by negative index -1 is the last element of the tuple
# range of the index [2:5]

# check if the element exist 
# like : if "apple" in thistuple

# update tuples 
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# we cannot change tuple values directly but we can covert it to list then change the value 

# another way of adding is 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# del thistuple this del key word will delete the whole tuple important
# unpack tuples

# nothing but destructoring
(green, yellow, red) = thistuple

# using asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

# assign rest of the variable in red like javascript spread

# what are loop in tuple
for x in thistuple:
    print(x)

# use range , while loop

# join tuples in python

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# tuple.count(5) tells number of time 5 occurs in the tuple
# index() returns a location where the element is founf

