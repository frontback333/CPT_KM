import random

def createmat(N):
    return [[random.randint(0,N*N*10) for _ in range(N)] for _ in range(N)]

def printmat(N,mt):
    for i in range(N):
        for j in range(N):
            print(f"{mt[i][j]:0{len(str(N*N*10))}d}",end=' ')
        print()

N=int(input())
A=createmat(N)
B=createmat(N)
C=createmat(N)
sum = createmat(N)

for i in range(N):
    for j in range(N):
        sum[i][j]=0
        for k in range(N):
            sum[i][j]+=A[i][k]*B[k][j]

for i in range(N):
    for j in range(N):
        sum[i][j]+=C[i][j]
printmat(N,A)
printmat(N,B)
printmat(N,C)
printmat(N,sum)