i = 2
a = 1
b = 1

while len(str(a)) < 1000:
    a += b
    if len(str(a)) < 1000:
        i += 1
    b += a
    if len(str(b)) < 1000:
        i += 1

print(i + 1)
