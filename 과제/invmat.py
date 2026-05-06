import random

def createmat(N):
    return [[random.randint(0,N*N*10) for _ in range(N)] for _ in range(N)]

def printmat(N,mt):
    for i in range(N):
        for j in range(N):
            print(f"{mt[i][j]:0{len(str(N*N*10))}d}",end=' ')
        print()

N=int(input())
mt=createmat(N)
printmat(N,mt)
print()
for i in range(N):
    for j in range(i,N):
        tmp=mt[i][j]
        mt[i][j]=mt[j][i]
        mt[j][i]=tmp
printmat(N,mt)