def ispal(a):
    b = str(a)
    reverse = b[::-1]
    if b == reverse:
        return a
    else:
        return 0

a, b = 100, 100
list = []

while a < 1000:
    while b < 1000:
        list.append(ispal(a * b))
        b += 1
    b = 100
    a += 1

print(max(list))
