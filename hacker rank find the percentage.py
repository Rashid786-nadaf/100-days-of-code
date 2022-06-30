# finding the percentage of the specified student.
# taking input for number of students
n = int(input())
student_marks = {} # stores the student data in dictionary in key:value pair.
for i in range(n):
    name, *line = input().split() # *line allows user to enter multiple values for single variable.
    scores = list(map(float, line)) # values that has been entered for single variable is then converted to list.
    student_marks[name] = scores # name:scores[] is appended to student_marks.
query_name = input() # user input for query_name that is present in student_marks dict.
count = 0
if query_name in student_marks:
    a = student_marks.get(query_name,"not_found") # get() method is used to access values from the student_marks dict.
    for i in range(len(a)):
        count += a[i]
avg = count/3
print("%.2f"%avg) # "%.2f" allows to print the value upto 2 decimal places.
#input example:
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60