n = input()
a = 0
mylist = []
while a < int(n):
    a += 1
    temp = input()
    if len(temp) > 10:
        length = len(temp) - 2
        mylist.append(temp[0] + str(length) + temp[-1])
    else:
        mylist.append(temp)

for i in mylist:
    print(i)
