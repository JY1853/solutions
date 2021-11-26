a, b = 0, 0
nums = []

while a < 100:
    while b < 100:
        nums.append(a ** b)
        b += 1
    b = 0
    a += 1

ans = []

for i in nums:
    ans.append(sum(int(digit) for digit in str(i)))

print(max(ans))
