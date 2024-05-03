# format string to specfy the part f we have to do txt = f"The Price is 50 dollar"
# f{} contain dynamic variable
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:



def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# Before Python 3.6 we used the format() method to format strings.