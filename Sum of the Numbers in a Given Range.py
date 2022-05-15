# sum of the numbers in a given range, this can be solved in 2 ways.
#  1: Using Brute Force.
#  2: Using the Formula.

# 1st method.
# Taking input from the user num1 and num2
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
sum = 0 # for storing the added numbers.
# using for loop for iteration purpose.
for i in range(num1,num2+1): # range has 3 parameters range(start,stop,step).
    sum+=i
print(sum)

# 2nd method.
# In this we will minus the larger number (b) with lower number (a) and add the final number with lower number (a).
# using formula : ((b *(b+1))/2 - (a*(a+1))/2) + a

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
sum = int(((b *(b+1))/2 - (a*(a+1))/2) + a)
print(sum)