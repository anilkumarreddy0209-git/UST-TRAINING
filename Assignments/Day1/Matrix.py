m=[[1,2,3,4],
   [5,6,7,8],
   [3,6,2,7]]
r=[]
rows=len(m)
cols=len(m[0])
for i in range(cols):
    temp=[]
    for j in range(rows):
        temp.append(m[j][i])
    r.append(temp)
for k in r:
    print(k)