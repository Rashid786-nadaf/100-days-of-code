# stock exchange problem.

num = int(input()) # taking input from the user.
stock_records = []
for i in range(num):
    name , value = input().split()
    stock_records.append([name,int(value)])
#print(stock_records)
list1 = []
list2 = []
list3 = []
for i in range(len(stock_records)): #
    for j in range(len(stock_records[i])):#stock_records[i] = stock_records[0] eg: ['CSE',23]
        if stock_records[i][j] == 'CSE' or stock_records[i][j] == 'cse': #stock_records[i][j] = stock_records[0][0] i.e 'CSE'
            list1.append(stock_records[i])
        elif stock_records[i][j] == 'SSE' or stock_records[i][j] == 'sse':
            list2.append(stock_records[i])
        elif stock_records[i][j] == 'NSE' or stock_records[i][j] == 'nse':
            list3.append(stock_records[i])

list1.sort(key=lambda x:x[1])  # X:X[1] is pointing to second index of the list1 eg: [['CSE',15],['CSE',40]] the x:x[1] means x[1]=15 storing in x
#key is a argument that take a function as input. i.e lamdba is a function.
list1.reverse()
list2.sort(key=lambda x:x[1])
list2.reverse()
list3.sort(key=lambda x:x[1])
list3.reverse()

#print(list1)
#print(list2)
#print(list3)
list4 = list1+list2+list3
list5 = sum(list4,[])
#print(list5)
l5 = list(map(str,list5))
#print(l5)
l = l5[-1]
#print(l)
def f(list5):
    for i in range(len(l5)):
        if i % 2 == 0:
            print(l5[i],end=' ')
        if i % 2 != 0 and i<len(l5)-1:
            print(l5[i],end=',')

res = str(f(l5))
print(res.replace("None",l))