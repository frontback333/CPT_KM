pp,mx = 0,0
for _ in range(4):
    a,b = map(int,input().split())
    pp += b-a
    mx = max(pp,mx)
print(mx)