t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    k = list(map(int,input().split()))
    tmp=b%a
    res=k[a-tmp:]+k[:a-tmp]
    print(*res)
