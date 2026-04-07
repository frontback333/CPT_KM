n = int(input())
ar = list(map(int,input().split()))
for i in range(n):
    for j in range(i,n):
        if(ar[j]<ar[i]):
            ar[i],ar[j]=ar[j],ar[i]
print(ar)