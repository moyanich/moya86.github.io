# str() METHOD
# @link https://www.geeksforgeeks.org/str-vs-repr-in-python/
# str() and repr() both are used to get a string representation of object.
# str() is used for creating output for end user while repr() is mainly used for debugging and development.
# repr’s goal is to be unambiguous and str’s is to be readable.
# For example, if we suspect a float has a small rounding error, repr will show us while str may not.


ex_1 = "Hello, I am new here"
ex_2 = str(29)
ex_3 = str(94.13532)
ex_4 = str(True)
print(str(ex_1))
print(repr(ex_1))
print(ex_3)
print(ex_4)
print(str(2.0/22.0))
print(repr(2.0/22.0))


# Output 
# Hello, I am new here
# 'Hello, I am new here'
# 94.13532
# True
# 0.09090909090909091
# 0.09090909090909091