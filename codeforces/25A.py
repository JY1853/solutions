a = input()
b = input()
mylist = b.split(' ')

oddcounter = 0
oddlist = []
evencounter = 0
evenlist = []

for i in mylist:
    if int(i) % 2 == 0:
        evencounter += 1
        evenlist.append(evencounter+oddcounter)
    else:
        oddcounter += 1
        oddlist.append(evencounter+oddcounter)

if evencounter == 1:
    print(evenlist[0])
else:
    print(oddlist[0])
