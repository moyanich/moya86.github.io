# String Methods 2
#
# 1. Create a variable called the_string and assign it the string "North Dakota".
# 2. Call .rjust() on the_string with 17 as its argument and print() the result.
# 3. Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
# 4. Create a variable called center_plus and assign it the result of .center() being called on the_
# string with 16 and "+" as arguments.
# 5. Use print() to display the string assigned to center_plus.
# 6. Call .lstrip() on the_string to remove "North" then print() the result.
# 7. Call .rstrip() on the_string with "+" as its argument and print() the result.
# 8. Call .strip() on the_string with "+" as its argument and print() the result.
# 9. Call .replace() on the_string and replace "North" with "South". print() the result.

# 1. Create a variable called the_string and assign it the string "North Dakota".
the_string = "North Dakota"

# 2. Call .rjust() on the_string with 17 as its argument and print() the result.
print(the_string.rjust(17))

# 3. Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
print(the_string.ljust(17, "*"))

# 4. Create a variable called center_plus and assign it the result of .center() being called on the_string
# with 16 and "+" as arguments.
center_plus = the_string.center(16, "+")

# 5. Use print() to display the string assigned to center_plus.
print(center_plus)

# 6. Call .lstrip() on the_string to remove "North" then print() the result.
print(the_string.lstrip("North"))

# 7. Call .rstrip() on the_string with "+" as its argument and print() the result.
print(center_plus.rstrip("+"))

# 8. Call .strip() on the_string with "+" as its argument and print() the result.
print(center_plus.strip("+"))

# 9. Call .replace() on the_string and replace "North" with "South". print() the result.
print(the_string.replace("North", "South"))


