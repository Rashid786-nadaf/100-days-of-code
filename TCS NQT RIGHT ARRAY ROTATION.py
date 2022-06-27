#Given an array[] of N intergers and a positive integer K.
# The task is to rotate the array clockwise by K.

# PERFORMING RIGHT ARRAY ROTATION.

#N value taking from the user input
N = int(input())
# forming list of array from users input.
arr = [int(i) for i in input().split(" ",N-1)]
#K value taking from the user.
K = int(input())
# right rotation of list of array.
for i in range(K):
    temp = arr[len(arr)-1]
    for j in range(len(arr)-1,0,-1):
        arr[j] = arr[j-1]
    arr[0]=temp

#printing list of array.
for i in range(len(arr)):
    print(arr[i], end=' ')