s1=['Riwaj','Aman','Akrit','Riwaj','Aman']
dict={}
for i in s1:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)S