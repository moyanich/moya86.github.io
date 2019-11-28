# A function is a block of organized, reusable code that is used to perform a single, related action.
# Functions provide better modularity for your application and a high degree of code reusing.
#  Source: https://www.tutorialspoint.com/python/python_functions.htm
# # Defining a Function
# You can define functions to provide the required functionality. Here are simple rules to define a function in Python.
# Function blocks begin with the keyword 'def' followed by the function name and parentheses '( )'.
# Any input parameters or arguments should be placed within these parentheses.
# You can also define parameters inside these parentheses.
# The first statement of a function can be an optional statement -
# the documentation string of the function or docstring.
# The code block within every function starts with a colon (:) and is indented.
# The statement return [expression] exits a function, optionally passing back an expression to the caller.
# A return statement with no arguments is the same as return None.
# # Syntax
# def function_name( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]


def function_name():
    print(2+2)
    return


function_name()


def function_parameter(parameter):
    print(parameter+2)
    return


function_parameter(16)

first_string = "Munchie"


def function_multiple_parameters(p1, p2, p3):
    print(p1, str(p2), p3)


function_multiple_parameters(first_string, 5, "Tuddles" )
