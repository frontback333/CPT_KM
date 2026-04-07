N=int(input())
D=list(map(int,input().split()))
M=int(input())
Q=list(map(int,input().split()))
dit = {}
for i in D:
    if i in dit : dit[i]+=1
    else : dit[i]=1
for i in Q:
    if i in dit: print(dit[i],end=' ')
    else : print(0,end=' ')