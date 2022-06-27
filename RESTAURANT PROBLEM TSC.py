# 'N' number of customers are waiting at a restaurant that is recently opened.
# After every 'M' minutes , a new customer arrives at the restaurant.
# Only one customer is allowed at a time. The manager at the reception desk asks each customers to wait for 'X' minutes to get their table.
# The task is to calculate the duration (in minutes) the last customer arrived needs to wait.
#  input format :
# First line : 3 input space-separated non -negative integers N,M,X as described in the problem.
# Output format :
# First line: A non negative integer as described in the problem statement.


# Taking input from user.
# N : number of customers.
# M : Time duration between two customer
# X : Time duration manager told to wait

#long approach
N,M,X  = map(int,input().split())
list1 = []
list2 = []
for i in range(N):
        if i == 0:
                list1.append(0)
        else:
                for j in range(N-1):
                        list1.append(list1[j]+M)
                if len(list1)==N:
                        break
print(list1)
for i in range(N):
        if i == 0:
                list2.append(0)
        else:
                for j in range(N-1):
                        list2.append(list2[j]+X)
                if len(list2)==N:
                        break
print(list2)
print(abs(list2.pop()-list1.pop())) # .pop() function by default it points to last index of the list


# best approach
# N,M,X  = map(int,input().split())
# list1 = [i*M for i in range(N)]
# print(list1)
# list2 = [i*X for i in range(N)]
# print(list2)
# print(abs(list1[-1]-list2[-1]))   #abs() converts negative number to positive