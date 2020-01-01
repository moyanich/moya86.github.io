# Roman Numeral Equivalent
# For this exercise, start by creating a variable and assigning it a randomly generated
# integer between and inclusive of both 1 and 10.
#
# Then, using your knowledge of if, elif, and else statements, create a program which prints
# the roman numeral equivalent of the randomly generated number.
#
# For example, if the randomly generated integer was 9, then the program would say that the
# roman numeral equivalent of 9 is IX in the output.

# This example uses the following python functions
#  random library
# for loop
#  Dictionary - A dictionary is a collection which is unordered, changeable and indexed.
#       In Python dictionaries are written with curly brackets, and they have keys and values.

import random

# generates random integer between and inclusive of 1 and 10
random_number = random.randint(1, 10)

# Used a dictionary to complete example.
# Create the dictionary
roman_numerals = {"i": 1, "ii": 2, "iii": 3, "iv":  4, "v": 5, "vi": 6, "vii": 7, "viii": 8,  "ix": 9, "x": 10}

for numerals, num in roman_numerals.items():   # numerals - key, num - value
    if num == random_number:
        print("The roman numeral equivalent of " + str(random_number) + " is " + numerals + ".")



