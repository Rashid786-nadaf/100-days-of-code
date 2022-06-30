# Consider a list (list = []). You can perform the following commands:

# 1 insert i e: Insert integer e at position i .
# 2 print: Print the list.
# 3 remove e: Delete the first occurrence of integer .
# 4 append e: Insert integer  at the end of the list.
# 5 sort: Sort the list.
# 6 pop: Pop the last element from the list.
# 7 reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands,
# where each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

n = int(input())
list = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'insert':
        list.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == 'print':
        print(list)
    elif cmd[0] == 'remove':
        list.remove(int(cmd[1]))
    elif cmd[0] == 'append':
        list.append(int(cmd[1]))
    elif cmd[0] == 'sort':
        list.sort()
    elif cmd[0] == 'pop':
        list.pop()
    else:
        list.reverse()

#input example:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
