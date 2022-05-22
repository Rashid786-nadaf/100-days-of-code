# To check wheather the year is leap year or not a leap year.
# This method can be solved by : using if-else method.

# Taking input from the user.
year = int(input("Enter the value for year: "))

# To check wheather the year is leap year or not
# The year value should be:
# 1. year should perfectly divisible by 400.
# 2. year should be divisible by only 4 and not by 100.
# this can br implemented by if-else method.

if ((year%400==0) or (year%4==0 and year%100!=0)):
    print("It is leap year.")
else:
    print("It is not a leap year.")