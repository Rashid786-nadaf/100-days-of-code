#Given an array[] of N intergers and a positive integer K.
# The task is to rotate the array clockwise by K.

# performing left rotation.

# N value taking input from the user.
N = int(input())
# forming list of array from users input.
arr = [int(i) for i in input().split(" ",N-1)]
# K value for rotating array clockwise
K = int(input())
for i in range(0,K):
    temp = arr[0]
    for j in range(0,len(arr)-1):
        arr[j] = arr[j+1]
    arr[len(arr)-1] = temp

for i in range(0,len(arr)):
    print(arr[i],end=' ')