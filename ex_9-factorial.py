# Create a function which takes one positive integer as its input and returns its factorial.
#
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and
# print what is returned by those calls.  For those inputs, you should get 6, 24, and 120, respectively.

num = int(input("Enter a positive number: "))
def function_fac(n) :
    if n == 1:
        return n
    elif n < 1:
        return("N/A")
    else:
        return n*function_fac(n-1)
print(function_fac(int(num)))