n=int(input())
for i in range(n):
    n1=input()
    sum=0
    digits = [int(x) for x in str(n1)]
    for z in range(len(digits)):
        sum=digits[0]+digits[z]
    print(sum)