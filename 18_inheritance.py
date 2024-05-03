class Person:
    pass

class Student(Person):
  pass


# class student that inherit the class from person 

# to inherit the constructor from parent function 
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

