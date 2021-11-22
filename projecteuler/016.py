# i was worried that python couldn't handle 2 ** 1000 but apparently thats not a problem so this is really easy

a = str(2 ** 1000)

list = list(map(int, a))
print(sum(list))
