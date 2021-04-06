a = input() #first line is number of test cases

counter = 0
testcases = []
ans = []

while counter < int(a):  #collecting all the test cases
    counter += 1
    testcases.append(input())

for i in testcases: #the calculations
    n = int(i.split()[0])
    m = int(i.split()[1])
    x = int(i.split()[2])
    if x%n == 0:
        a = n
    else:
        a = x%n
    b = (x-a)/n
    y = int((a-1)*m+b+1)
    ans.append(y)

for j in ans:
    print(j)
