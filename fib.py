n=int(input("Enter the number of Terms"))
x=0
y=1
z=0
if(n==0):
    print("There is no zero term")
elif(n==1):
    print(f"{x}")
else:
    for i in range(0,n):
        print(f"{x}")
        z=x+y
        x=y
        y=z