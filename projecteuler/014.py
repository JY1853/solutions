def collatz(a):
    counter = 1
    while not a == 1:
        if a % 2 == 0:
            counter += 1
            a = a/ 2
        else:
            counter += 1
            a = (3 * a) + 1
    return counter

c = 1
list = []
while c < 1000000:
    list.append(collatz(c))
    c += 1

print(list.index(max(list)))
