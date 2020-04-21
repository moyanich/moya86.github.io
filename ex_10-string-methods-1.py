# String Methods 1

# 1. Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"
# 2. Use .isupper() to check if mixed_case is a string of all upper case letters. print() the result.
# 3. Use .islower() to check if mixed_case is a string of all lower case letters. print() the result.
# 4. Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.
# 5. Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.
# 6. Use the .istitle() method to check if mixed_case is title case and print the result.
# 7. Create a variable called title_case and assign it the result of .title() being called on mixed_case.
# 8. print() title_case
# 9. Call startswith() on mixed_case with the letter mixed_case starts with as its argument. print() the result.
# 10. Call endswith() on mixed_case with the letter mixed_case ends with as its argument. print() the result.
# 11. Create a variable called words and assign it the result of split() being used on mixed_case.
# 12. print the variable "words"
# 13. Use the .join() method to join together all of the items in the list assigned to words
# as a single string.  Use .isalpha() to check if the string is made up entirely of letters.
# Finally, use print() to display the result.


mixed_case = "A Song of Ice and Fire"

# 2. Use .isupper() to check if mixed_case is a string of all upper case letters. print() the result.
print(mixed_case.isupper())

# 3. Use .islower() to check if mixed_case is a string of all lower case letters. print() the result.
print(mixed_case.islower())

# 4. Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.
print(mixed_case.upper())

# 5. Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.
print(mixed_case.lower())

# 6. Use the .istitle() method to check if mixed_case is title case and print the result.
print(mixed_case.istitle())  # Returns True if the string follows the rules of a title i.e.
# The first letters have to be title case

# 7. Create a variable called title_case and assign it the result of .title() being called on mixed_case.
title_case = mixed_case.title()

# 8. print() title_case
print(title_case)

# 9. Call startswith() on mixed_case with the letter mixed_case starts with as its argument. print() the result.
print(mixed_case.startswith("A"))

# 10. Call endswith() on mixed_case with the letter mixed_case ends with as its argument. print() the result.
print(mixed_case.endswith("Fire"))

# 11. Create a variable called words and assign it the result of split() being used on mixed_case.
words = mixed_case.split()
# 12. print the variable "words"
print(words)

# 13. Use the .join() method to join together all of the items in the list assigned to words as
# a single string. Use .isalpha() to check if the string is made up entirely of letters.
# Finally, use print() to display the result.
# join - Joins the elements of an iterable to the end of the string
# isalpha - Returns True if all characters in the string are in the alphabet
print("".join(words).isalpha())
