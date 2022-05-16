# This method can be solved in 3 ways:
# 1st if else statement.
# 2nd using ternary operator.
# 3rd using max() function

# 1st method:
# taking input from the user
number1 = int(input("Enter the value of number1: "))
number2 = int(input("Enter the value of number2: "))
if number1 > number2:
    print("number1 is greater.")
else:
    print("number2 is greater.")

# 2nd method.
# ternary opertor : This is used to find greater of two number
# we use if and else in print statement that returns boolean values as the result.

num1 = int(input("Enter the values of num1: "))
num2 = int(input("Enter the values of num2: "))
print(num1 if num1 > num2 else num2)

# 3rd method
# using max() function.
# max() function is inbuilt function that finds greatest of two numbers.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(max(a,b))