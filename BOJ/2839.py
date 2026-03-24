N = int(input())
ans = -1
for i in range(N//5,-1,-1):
    if not (N-(i*5))%3 :
        ans = i + (N-(i*5))//3
        break
print(ans)