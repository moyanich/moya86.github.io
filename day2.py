fact = 1
print("enter a number to find factorial:")
num = int(input())
for i in range(num,1,-1):
    fact = fact*i
print("factorial is "+ str(fact))
