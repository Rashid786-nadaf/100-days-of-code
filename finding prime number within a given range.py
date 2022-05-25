# finding prime numbers within a given range
# prime number : The number which is divided by 1 or by it-self.
# Taking two user input as low and high limits.
num1 = int(input("Enter the lower limit: "))
num2 = int(input("Enter the higher limit: "))
# we will append all the primes in the list primes.
primes = []
# 1st for loop will iterate through the number.
for i in range(num1, num2 + 1):
    flag = 0
    if i < 2:
        continue
# This for loop will iterate through the number and
    # check wheather the number is prime or not.
    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(i)
print(primes)