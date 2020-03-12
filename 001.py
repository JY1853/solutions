ans = 0
i = 0
j = 0
k = 0

while i < 999:
    i+=1
    if i % 3 == 0:
        ans += i

while j < 999:
    j += 1
    if j % 5 == 0:
        ans += j

while k < 999:
    k += 1
    if k % 15 == 0:
        ans = ans - k

print(ans)
