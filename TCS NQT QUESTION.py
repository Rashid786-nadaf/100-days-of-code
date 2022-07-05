# Problem statement
# A doctor has a clinic where he serves his patients.
# The doctor's consultation fees are different for different groups of patients depending on their age.
# If the patient's age is below 17. The fee is 200 INR. If the patient's age is between 17 and 40, fees are 400 INR.
# If the patient's age is above 40, fees are 300 INR.
# Write a code to calculate earnings in a day for which one array/List of values representing the age of patients visited on that day is passed as input.
# Note:
# 1. Age should not be zero or less than zero or above 120.
# patients a day.
# 2. Doctors consult a maximum of 20 3. Enter age value (press ENTER without value to stop):
# Input
# 20
# 30
# 40
# 50
# 2
# 3
# 14
# Output
# Total income 2100 INR

patient = int(input("Enter the number of patient's to be consulted: "))
income = 0
if patient > 20:
    print("Maximum patient's limit is 20")
else:
    while patient != 0:
        age = int(input())
        if age == 0 or age > 120:
            print("Invalid age re-enter.")
            continue
        if age <= 17:
            income += 200
        elif age <= 40:
            income += 400
        else:
            income += 300
        patient -= 1
print(f"Total income {income} INR")
