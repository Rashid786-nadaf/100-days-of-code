#To check whether the given string is palindrome:
string = input("Enter the string: ")
newstring = string[::-1]
if string == newstring:
    print("The string is palindrome\n")
else:
    print("The string is not palindrome\n")
