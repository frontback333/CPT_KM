K = int(input())
L=[]
for _ in range(K):
    ipt=int(input())
    if not ipt:
        L.pop()
    else:
        L.append(ipt)
sum=0
for i in L: sum+=i
print(sum)