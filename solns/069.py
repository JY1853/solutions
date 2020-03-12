primes = [2]
v = 3
ans = 1

while ans < 250000:
    if any(v % p == 0 for p in primes):
        v += 2
    else:
        primes.append(v)
        ans = ans * v
        v += 2
print(ans * 2)

#We can do this without writing any code - simply observe that there cannot be any repeated factors in n.
