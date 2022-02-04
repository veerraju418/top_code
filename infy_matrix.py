mat=[[0,1,6,8,8,9],[5,6,1,6,8,9],[6,5,6,1,1,9],[1,6,6,1,1,9],[6,3,3,3,3,9]]
#4 same elements in subsequent  row col diagonal
res=10000
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j],end=' ')
    print()

row=len(mat)
col=len(mat[0])

def check(i,j):
    if i<row and j<col:
        return True
    return False


for i in range(row):
    for j in range(col):
        start=mat[i][j]

        #check 4 element in row
        if check(i,j+3):
            if mat[i][j+1]==start and mat[i][j+2]==start and mat[i][j+3]==start:
                res=min(res,start)
        

        #col
        if check(i+3,j):
            if mat[i+1][j]==start and mat[i+2][j]==start and mat[i+3][j]==start:
                res=min(res,start)
        

        #diag
        if check(i+3,j+3):
            if mat[i+1][j+1]==start and mat[i+2][j+2]==start and mat[i+3][j+3]==start:
                res=min(res,start)
print(res)
