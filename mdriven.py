print("Select an Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("1-4"))
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if(ch==1):
    result=n1+n2
elif(ch==2):
    result=n1-n2
elif(ch==3):
    result=n1*n2
else:
    result=n1/n2
print(result)    

