N=int(input())
L = list(map(int,input().split()))
L.sort()
print(L[0],L[N-1])