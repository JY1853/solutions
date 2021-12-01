def donald(a):
    c, d = 1, 0
    while c * c < a:
        if a % c == 0:
            d += c
            d += a / c
            c += 1
        else:
            c += 1
    return int(d - a)

counter = 1
ans = 0

while counter < 10000:
    dcounter = donald(counter)
    if donald(dcounter) == counter and not dcounter == counter:
        ans += counter
        ans += dcounter
        counter += 1
    else:
        counter += 1

print(int(ans / 2))
