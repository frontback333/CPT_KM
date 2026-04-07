#D[i]=점이 정렬된 순서로 i+1개까지 있을때 전체 거리 합
N=int(input())
L = list(map(int,input().split()))
D = [0]*N
L.sort()
sum=0
for i in range(1,N):
    D[i] = D[i-1] + (L[i]-L[i-1])*i
    sum+=D[i]
print(sum*2)