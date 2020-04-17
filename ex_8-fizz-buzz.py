# Write a program that prints the integers 1 through 50 using a loop.
#
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
# For numbers which are multiples of 3 but not 5 print “Fizz” instead of the number and
# for the numbers that are multiples of 5 but not 3 print “Buzz” instead of the number.

num = 0

for num in range(1, 51):
    # for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # For numbers which are multiples of 3 but not 5 print “Fizz” instead of the number
    elif num % 3 == 0:
        print("Fizz")
    # for the numbers that are multiples of 5 but not 3 print “Buzz” instead of the number
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
