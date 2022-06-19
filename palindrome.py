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

# using slicing:
numbers = int(input("Enter the number: "))
reverse1 = str(numbers)[::-1]
if reverse1==numbers:
    print("palindrome\n")
else:
    print("not a palindrome\n")

#recursion method for checking string:
def palindrome(string):
#base case
    if len(string) <= 1:
        return True
    if string[0]==string[len(string)-1]:
        return palindrome(string[1:len(string)-1])
    else:
        return False
str = input("Enter the string: ")
if palindrome(str):
    print("it's palindrome")
else:
    print("it's not a palindrome")