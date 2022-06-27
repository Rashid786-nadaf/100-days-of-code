#You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.
#For Example:
#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2


s = input()
new_string = ""
for i in range(len(s)):
    if s[i].isupper():
        new_string += s[i].lower()
    else:
        new_string += s[i].upper()
print(new_string)