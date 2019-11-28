# Source: https://www.tutorialspoint.com/python/python_modules.htm
# A module allows you to logically organize your Python code.
# Grouping related code into a module makes the code easier to understand and use.
# A module is a Python object with arbitrarily named attributes that you can bind and reference.
# Simply, a module is a file consisting of Python code.
# A module can define functions, classes and variables. A module can also include runnable code.
# Example:
# The Python code for a module named aname normally resides in a file named aname.py.
# Here's an example of a simple module, support.py
# def print_func( par ):
# print "Hello : ", par
# return

# The import Statement
# You can use any Python source file as a module by executing an import statement in some other Python source file.
# The import has the following syntax −
# import module1[, module2[,... moduleN]
# When the interpreter encounters an import statement,
# it imports the module if the module is present in the search path.
# A search path is a list of directories that the interpreter searches before importing a module.
# For example, to import the module support.py, you need to put the following command at the top of the script −
#
# #!/usr/bin/python
#
# # Import module support
# import support
#
# # Now you can call defined function that module as follows
# support.print_func("Zara")
# When the above code is executed, it produces the following result −
#
# Hello : Zara

import random
print(random.randint(1, 10))

# Note: need to learn more about modules

