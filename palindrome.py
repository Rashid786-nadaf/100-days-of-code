# to check wheather the number is palindrome:
# using simple itreation:

#taking number as input from user
numbers = int(input("Enter the number to check for palindrome: "))
reverse = 0
temp = numbers
while numbers > 0:
    reminder = numbers % 10
    reverse = (reverse*10)+reminder
    numbers = numbers//10
if temp == reverse:
    print("Number is palindrome\n")
else:
    print("Number is not palindrome\n")

