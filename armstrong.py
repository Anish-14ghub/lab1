for i in range(100, 1000):
    a = str(i)
    s = int(a[0])**3 + int(a[1])**3 + int(a[2])**3
    if s == i:
        print(i)