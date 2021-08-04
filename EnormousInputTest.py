n,k = map(int,input().split())
C=0
for i in range(n):
    n1=int(input())
    if(n1%k==0):
        C=C+1
print(C)