import math

input = input()
list = input.split(' ')
a = int(list[2])
b = math.ceil(int(list[0]) / a)
c = math.ceil(int(list[1]) / a)
print(int(b * c))
