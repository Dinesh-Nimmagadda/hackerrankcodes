t = int(input())
for _ in range(t):
    n= int(input())
    m = []
    for i in range(n):
        a = list(map(int,input().split()))
        m.append(a)
    count=0
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j<=q:
                        if m[i][j]>m[p][q]:
                            count+=1
    print(count)
