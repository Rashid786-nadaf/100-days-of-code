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

# using recurion method:
num1 = int(input("Enter the number for num1: "))
length1 = len(str(num1)) # specify lenght of num1
numbers1 = num1
sum1 = 0 # stores the armstrong addition.
# defineing armstrong having parameters
# 1.num1:having original user number initially
# 2.length1: having lenght of the inital number1.
# 3.sum1: storing 0 at first and later on for storing armstrong addition.
def armstrong(num1,length1, sum1):# armstrong(371,3,0)
    if num1 == 0:   # not applicable
        return sum1
    if num1 != 0:  # appicable
        sum1 += pow(int(num1%10),length1)#sum1 = 0 + (371%10)^3 --> 0 + 1^3 --> sum1 = 1 this will happen untill the num1 is 0
        # then later it return updated num1,length1,sum1 to def
        return armstrong(num1/10,length1,sum1) # i.e , armstrong(37,2,1) it will repeat untill the condition fails.
if armstrong(num1,length1,sum1) == numbers1:
    print("armstrong\n")
else:
    print("not a armstrong\n")

# armstrong numbers in a given range:
low = int(input("Enter the lower limit: "))
high = int(input("Enter the higher limit: "))
for i in range(low,high-1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digits = temp%10
        sum += digits ** order
        temp //= 10
    if i ==sum:
        print(i,end= '\n')

