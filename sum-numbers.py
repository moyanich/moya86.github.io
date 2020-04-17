# Programming Challenge: Sum of Numbers From A Positive Integer
# Write a program which gets a positive integer from a user using input() and assigns it to a variable.
#
# The program should then use a while loop to get the sum of all of the integers from the integer that
# was entered by the user down to 1.  For example, if the integer entered by the user was 6, the
# while loop would find the sum of 6, 5, 4, 3, 2, and 1, which is 21.
#
# At the bottom of your program create two print statements.  One will display the user entered
# integer and the other will display the sum found by the while loop.

# num is a variable which holds a user entered integer.
num = int(input("Enter a number to add: "))

#  This is a variable which will be used to hold the sum of all the integers from num.
sum = 0

while num > 0:
    sum += num

    # This will decrement num so that num will eventually equal 0 and the while
    # loop will stop running its code.
    num -= 1


print(sum)

