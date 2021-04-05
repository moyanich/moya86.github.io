# Programming Challenge: Word Counter

# For this programming challenge, write a program in a .py file which takes a string
# (you can assign the string to a variable or use input() to get a string from a user) and uses
# two print() statements to display a list of all of the words that the string contains as well
# as the number of words in the string.
#
# For example, if the program was used on the string "This is a string.", then the
# first print statement would display ['This', 'is', 'a', 'string'] and the second
# print statement would display 4.  Remember, to break up a string into that kind of a list,
# you would use the .split() method.
#
# Also, notice that there is no "." after "string" in the list displayed by the first print()
# statement:  For this program, you should get rid of everything from the list except numbers,
# letters, and spaces before using .split().  That will remove all punctuation and odd characters
# from the string, including periods from acronyms and floats as well as escape sequences and
# apostrophes used in contractions.
#
# Since numbers are being kept, they will count as words.  So, if the string the program
# was being used on was "James Bond is 007.", then the number "007" would count as a word
# and the string would have 4 words total.
#
# You should test your program with many different strings.  However, the string that the
# solution code is being used on is the string below, which is a quote from the movie Forrest Gump.
# This string has been assigned to a variable called str_1, so if you copy the code into your .py file,
# make sure to change the variable name to whatever you have been using.

str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."