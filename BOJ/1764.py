N,M=map(int,input().split())
lis={}
for _ in range(N):
    pp = input()
    lis[pp]=1
cnt=0
ans=set()
for _ in range(M):
    pp=input()
    if pp in lis:
        cnt+=1
        ans.add(pp)
print(cnt)
ans=list(ans)
ans=sorted(ans)
for i in ans: print(i)