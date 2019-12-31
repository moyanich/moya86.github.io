# Python If-Else
# Source: Hackerrank
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, n.


n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")



n = int(input("Enter a number: "))

if (n in range (6, 21) or n % 2 != 0):
    print("Weird")
else:
    print("Not Weird")
