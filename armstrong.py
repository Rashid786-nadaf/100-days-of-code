# armstrong number:
# A given number is armstrong if the sum of the digits of the number raised to power of the length of number
# added together and then compared with the original number, if same then it's armstrong or else not.

# iteration method:
num = int(input("enter the number to check armstrong: \n"))
numbers = num
length = len(str(num))
sum = 0
digit = 0
for i in range(length):
    digit = int(num%10)
    num = num/10
    sum += pow(digit,length)
if numbers == sum:
    print("it is armstrong")
else:
    print("it is not a armstrong")