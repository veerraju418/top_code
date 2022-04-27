d=dict()
for order in orders:
    d[order[1]]=[]
for order in orders:
    d[order[1]].append(order[2])
dish=[]
l=[]
for order in orders:
    l.append(order[2])
l=list(set(l))
l.sort()
dish.append('Table')
for i in l:
    dish.append(i)

fin=[]
#fin.append(dish)
for table,data in sorted(d.items(),key=lambda x:x[0]):
    li=[]
    li.append(int(table))
    for dk in l:
        try:
            li.append(str(d[table].count(dk)))
        except:
            li.append(0)
    fin.append(li)


res=sorted(fin,key=lambda item:item[0])
for i in range(len(res)):
    res[i][0]=str(res[i][0])
db=[]
db.append(dish)
for don in res:
    db.append(don)
return db
