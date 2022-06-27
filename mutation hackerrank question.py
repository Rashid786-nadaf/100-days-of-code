# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# Let's try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.
# Example
# >>> string = "abracadabra"
# You can access an index by:
# >>> print string[5]
# a

# Task
# Read a given string, change the character at a given index and then print the modified string.
# Function Description
# Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:
# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert
# Returns

# string: the altered string
# Input Format
#
# The first line contains a string, .
# The next line contains an integer , the index location and a string , separated by a space.
#
# Sample Input
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output
# abrackdabra
"""
def mutable_string(string,position,character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ =="__main__":
    s = input()
    i , c = input().split()
    string = mutable_string(s,int(i),c)
    print(string)
"""
string = input()
p,c = input().split()
l = list(string)
#print(c)
#print(p)
for i in range(len(l)):
    if i == int(p):
        l[i] = c
    string = ''.join(l)
print(string)
