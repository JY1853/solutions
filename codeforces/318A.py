import math

a = input()

n = int(a.split(' ')[0])
k = int(a.split(' ')[1])


if k == math.ceil(n/2) and k % 2 == 1:
    print(n)
elif k > (n/2):
    print(int(2*(k-(math.ceil(n/2)))))
else:
    print(int((2*k)-1))
