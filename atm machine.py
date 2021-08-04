
withamount,intamount=map(float,input().split())
amount=withamount+0.50
if withamount%5==0 and amount<=intamount:
    tran=intamount-amount
    print(tran)
else:
    print(intamount)
