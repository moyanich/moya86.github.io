# For Loop
# Source: https://www.pythonforbeginners.com/control-flow-2/python-for-and-while-loops
# The for statement is used to iterate over the elements of a sequence.
# It's traditionally used when you have a piece of code which you want to repeat n number of time.
#
# The for loop is often distinguished by an explicit loop counter or loop variable.

for counter in range(1, 6):
    print(counter)

#can also be written like this:

numbers = range(1, 6)

for count in numbers:
    print(count)


