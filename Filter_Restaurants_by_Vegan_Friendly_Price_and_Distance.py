d=dict()
if veganFriendly==1:
    for data in restaurants:
        if data[3]<=maxPrice and data[4]<=maxDistance and data[2]==1:
            d[data[0]]=data[1]
else:
    for data in restaurants:
        if data[3]<=maxPrice and data[4]<=maxDistance:
            d[data[0]]=data[1]
don=dict()
for k,v in sorted(d.items(),key=lambda item:item[1],reverse=True):
    if don.get(v,0)!=0:
        don[v].append(k)
    else:
        don[v]=[k]
res=[]
for k,v in sorted(don.items(),reverse=True):
    r=sorted(v,reverse=True)
    for i in r:
        res.append(i)
return res
