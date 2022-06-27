# To check whether the charater is vowel or consonants:

char = input("Enter the sting ")
# to check whether the character is alphabet or not
if not char.isalpha():
    print("Not a  character\n")
elif char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'i' or char == 'o' or char == 'u':
    print(char,"is a vowel\n")
else:
    print(char,"is a consonants\n")

# To find the ASCII value of the given character.
a = input("Enter the character the for a:")
val = ord(a)
print("The ASCII value for the character is \n",val)

# length of the string without using strlen() function
string = input("Enter the string:")
count = 0
for i in string:
    count += 1
print(count)

# toggle each character in a string.
c  =  input("Enter the string for c: ")
if not c.isalnum():
    print("not a character string:\n")
elif c.islower():
    print(c.upper())
else:
    print(c.lower())

# count the number of vowels in a string:
d = input("Enter the string for d: ")
count1 = 0
for i in d:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'u':
        count1 += 1
print(count1,'\n')

# to remove vowels from the given string:
d =  input("Enter the string for d: ")
f = str()
for i in d:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        pass
    else:
        f += i
if i == 0:
    print("No vowels found\n")
else:
    print("New string is \n",f)

#using replace method:
vowels = ['A','E','I','O','U','a','e','i','o','u']
for i in range(len(d)):
    if d in vowels:
        f = f.replace(i,"")
print("String after replacing:\n",f)
