from num2words import num2words #num2words package required

iterator = 1
spaces = 0
counter = 0
while iterator < 1001:
    x = num2words(iterator)
    if any(n == "-" for n in x):
        spaces += int(x.count("-"))
        if any(n == " " for n in x):
            spaces += int(x.count(" "))
        else:
            spaces += 0
    elif any(n == " " for n in x):
        spaces += int(x.count(" "))
    else:
        spaces += 0
    counter += len(x)
    iterator += 1
print(counter - spaces)
