N =int(input())
dit = {}
for _ in range(N):
    book = str(input())
    if book in dit : dit[book]+=1
    else : dit[book]=1
ans,mx=0,0
for i,v in dit.items():
    if v>mx:
        mx=v
        ans=i
    elif v==mx: ans = min(ans,i)
print(ans)