n=int(input())
for i in range(n):
    n1=int(input())
    fact = 1
    for num in range(2, n1 + 1):
        fact *= num
    print(fact)
    