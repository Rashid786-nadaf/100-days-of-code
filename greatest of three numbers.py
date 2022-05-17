# This can be solved by three method:
# 1st method : using if-else statement.
# 2nd method : using nested if-else statement.
# 3rd method : using ternary operator.

# 1st method:
# taking all three inputs from the user.
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
if a > b and a > c:
    print(str(a)+ " is greater.")
elif b > a and b > c:
    print(str(b)+" is greater.")
else:
    print(str(c)+" is greater.")

# 2nd method:
#Taking input from user.
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
num3 = int(input("Enter the value of num3: "))
if num1>num2: # nested if-else.
    if num1>num2:
        print(str(num1)+" is greater.")
elif num2 > num1:
    if num2 >num3:
        print(str(num2)+" is greater")
else:
    print(str(num3)+ " is greater")

# 3rd method using ternary operator.
# taking input from the user.
first = int(input("Enter the value: "))
second = int(input("Enter the value: "))
third = int(input("Enter the value: "))
# ternary operator : checks greatest number of two and returns it.
max = first if first>second else second
max = third if third>max else max
print(max) # printing greatest number.