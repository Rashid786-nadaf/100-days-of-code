# Nested list hackerrank problem.
records = []
grade = []
no_of_items = int(input())
for i in range(no_of_items):
    name = str(input())
    score  = float(input())
    records.append([name,score])
    grade.append(score) # this will append only score.
print(records)
print(grade)
grade = sorted(set(grade)) # this will sort and have only unique values.
print(grade)
m = grade[1]
print(m)
name = []
for val in records:  # itrating scores through-out records.
    if m == val[1]:  # checking wheather value of sceond highest grade is equal or not.
        name.append(val[0]) #and finally appending name it to name list.
print(name) #printing name which is un-soreted.
name.sort()
print(name) # printing sorted name list.
for a in name:
    print(a)
"""
inputs to be taken.
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""