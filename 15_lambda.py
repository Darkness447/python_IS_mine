# lambda arguments : expression


# we can make our own lambda function important

x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))


z = lambda a, b, c : a + b + c
print(z(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# in function return lambda function to make it reuse by other

