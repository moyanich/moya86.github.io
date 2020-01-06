import math

# Exmaple
# Source: Hackerrank
#
# link: https://www.hackerrank.com/challenges/python-loops/problem
# Read an integer N . For all non-negative integers i < N, print i2.
# Constraints
# 1 <= N <= 20


n = int(input("Enter a number"))

i = 0

for i in range(n):
    print(pow(i, 2))
