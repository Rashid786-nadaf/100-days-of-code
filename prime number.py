# To check number is prime or not.
# In order to do so the number should be only divisible by itself and 1.
# taking input from the user
number = int(input("Enter the value: "))
# we are taking range(2,number) because by 1 all numbers are divisible,
# so instead of 1 we start from 2 and
# number because the range function will stop before the specified number.
for i in range(2,number):
    if number % i ==0:
        print("Number is not prime")
        break
else:
    print("Number is prime.")
# end.