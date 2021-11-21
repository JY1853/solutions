a = 2
b = 2

terms = []

while 100 >= a:
    while 100 >= b:
        terms.append(a ** b)
        b += 1
    b = 2
    a += 1

norepeats = list(dict.fromkeys(terms))

print(len(norepeats))
