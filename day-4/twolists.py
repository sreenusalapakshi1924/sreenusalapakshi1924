a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
c=[]
for i in range(0,len(a)):
    if(a[i] in b and a[i] not in c):
        c.append(a[i])
print(c)