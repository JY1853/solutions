import math

num = math.factorial(100)
ans = 0
for digit in str(num):
    ans += int(digit)

print(ans)
