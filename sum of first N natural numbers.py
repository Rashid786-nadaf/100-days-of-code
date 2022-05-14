# This problem statement can be solved in 3 ways
# 1. looping.
# 2. using formula for the sum of N terms.
# 3. using recursion.

# 1st method.

# taking input from the user.
num = int(input("Enter the value: "))
sum = 0 # for storing added number.
for i in range(num+1):
# we use num+1 because in range function the number will start from 0(default) and stops before the specified number.
    sum+=i
print(sum)

# 2nd method.
# formula for finding sum of N terms:
# sum = (num*(num+1))/2.

num1 = int(input("Enter the value for num1: "))
sum = int((num*(num+1))/2)
print(sum)

# 3rd method.
# recursion : function calling it-self repeatedly know as recursion.
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1) # values get added recursively, if the value is not 1.

num2 = int(input("Enter the value for num2: "))
print(getSum(num))