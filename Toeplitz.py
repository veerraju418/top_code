https://leetcode.com/problems/toeplitz-matrix/
r=len(matrix)
c=len(matrix[0])
fl=0
for i in range(c):
    don=0
    f=matrix[don][i]
    
    co=don+1
    d=i+1
    
    while co<r and d<c:
        if matrix[co][d]!=f:
            fl=1
            break
        co+=1
        d+=1
    if fl==1:
        break

for i in range(1,r):
    king=0
    f=matrix[i][king]
    y=i+1
    z=king+1
    while y<r and z<c:
        if matrix[y][z]!=f:
            fl=2
            break
        y+=1
        z+=1
    if fl==2:
        break
    
if fl!=1 and fl!=2:
    return True
return False
