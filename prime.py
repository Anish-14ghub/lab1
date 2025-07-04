a = int(input("Enter a number: "))
if a > 1:
    s = True
    for i in range(2, a):
        if a % i == 0:
            s = False
            break
    if s:
        print("Prime")
    else:
        print("Not Prime")

