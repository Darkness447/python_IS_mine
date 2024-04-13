# multiline string


str1 = """
Darkness is future
That's what i can tell you right now 
"""


# there is no char data type in python very important


# for loop in string
# len in string is len(s)

# for x in str1:
#     print(x)

# print(str1)

# in keyword 

print("is" in str1)

# use this with if statement 

if "is" in str1:
    print("you are dumb ash")

    # similary there is not in

# return a range by using this []

b = "Hi John Doe"
print(b[5:])

# use slice end,start and negatives to play with the string


# built in methods that can be used in a string
# a.upper()
# a.lower()
# remove white space before and after the string like trim() , strip()
# replace a string with other string string means not whole string but the part of string that is specified
# a.replace("d","Z")

# split method will return the list .split(specify the crateria)
# concat two string by just a+b

# to print the number under string use f
x = 76
print(f"asdka;slkd;lad {x}")
# we can also format the value here like x:.2f upto two decimal places 


# \" illegal character can be inserted in string

print("Hello \"Darkness\" Bro ")

"""

shit~~~~~~

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""