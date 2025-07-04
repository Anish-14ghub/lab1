a=[1,2,3,4,5]
b=[1,4]
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)