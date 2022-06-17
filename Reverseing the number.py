# reversing the number
#taking input string from user
num=int(input("enter the string : "))
reverse=0
while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10

print(reverse)

