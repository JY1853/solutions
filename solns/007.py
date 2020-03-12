primes = [2]
v = 3

while len(primes) < 10001:
    if any(v % p == 0 for p in primes):
        v += 2
    else:
        primes.append(v)
        v += 2
print(max(primes))
