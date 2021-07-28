x=int(input())
y=int(input())
z=int(input())
N=int(input())
ans=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=N:
                ans.append([i,j,k])
print(ans)
