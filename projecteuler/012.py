def eul(a):
    c = 1
    ans = 0
    while c * c < a:
        if a % c == 0:
            ans += 2
            c += 1
        else:
            c += 1
    return ans

tnums = [0]
euls = [0]
counter = 1

while max(euls) < 500:
    a = max(tnums)
    tnums.append(a+counter)
    euls.append(eul(a+counter))
    counter += 1    

print(max(tnums))
