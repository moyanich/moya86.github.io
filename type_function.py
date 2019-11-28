# type() FUNCTION
# @link https://www.geeksforgeeks.org/python-type-function/
# type() method returns class type of the argument(object) passed as parameter.
# type() function is mostly used for debugging purposes.
# Two different types of arguments can be passed to type() function, single and three argument.
# If single argument type(obj) is passed, it returns the type of given object.
# If three arguments type(name, bases, dict) is passed, it returns a new type object.

# E.G.
# type(object)
# type(name, bases, dict)
# Parameters :
# name : name of class, which later corresponds to the __name__ attribute of the class.
# bases : tuple of classes from which the current class derives. Later corresponds to the __bases__ attribute.
# dict : a dictionary that holds the namespaces for the class. Later corresponds to the __dict__ attribute.

ex_1 = False
ex_2 = 29
ex_3 = 4.13532
ex_4 = "Hello, I am new here"
print(type(ex_1))
print(type(ex_2))
print(type(ex_3))
print(type(ex_4))
print(type([]) is list)  # This is an array ???!!
print(type([]) is not list)  # This is an array, therefore this evaluation is false
print(type(()) is tuple)   # Note: Learn what is a tuple
print(type({}) is dict)  # Note: Learn what is a dict
print(type({}) is not list)


# Output 
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# True
# False
# True
# True
# True