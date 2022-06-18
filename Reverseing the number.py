# reversing the number
#taking input string from user
num=int(input("enter the string : "))
reverse=0
while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10

print(reverse)
# using string slicing.
num2=int(input("enter the string : "))
print(str(num2)[::-1])

# recursion method.
# define recursum
def recurcum(num3,reverse1):
    if num3 >0:
        reminder1 = num3 % 10
        reverse1 = (reverse1*10)+reminder1
        num3 = num3//2
        return recurcum(int(num3/10),reverse)

num3 = int(input("Enter the number: "))
reverse1 = 0
print(recurcum(num3,reverse1))
