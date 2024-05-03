# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes
# print(len(x))

# python scope very important

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
# we can think it as a closure in python


# global scope

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

# if we have to create global scope variable in local scope 
def myName():
   global  x
   x = 100
   
# The nonlocal keyword is used to work with variables inside nested functions.

# The nonlocal keyword makes the variable belong to the outer function.