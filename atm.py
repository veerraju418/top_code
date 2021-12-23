d=dict()
l1=[3,1,3,10]
l2=[2000,500,100,20]
goal=4300
j=0
for i in l2:
    d[i]=l1[j]
    j+=1
res=0
f=[]
for k,v in d.items():
    c=0
    fl=1
    while res+k<=goal:
        if v!=0:
            res+=k
            c+=1
            v-=1
        else:
            f.append(0)
            fl=0
            break
    if fl==1:
        f.append(c)
if res!=goal:
    print(0)
else:
    for i in f:
        print(i,end=' ')
