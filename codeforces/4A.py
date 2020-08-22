val = input()

if val.isdigit():
    if int(val) == 2:
        print("NO")
    elif int(val) < 101 and int(val) % 2 == 0:
        print("YES")
    else:
        print("NO")
