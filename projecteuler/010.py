# this took me like a solid 40 minutes to run, so it's not very efficient. will come back and think about it again!

primes = [2]
v = 3

while v < 2000000:
    if any(v % p == 0 for p in primes):
        v += 2
    else:
        primes.append(v)
        v += 2
print(sum(primes))
