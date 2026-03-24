a = int(input())
cnt=0
for _ in range((a*2)-1):
    if _<a: cnt+=1
    else : cnt-=1
    for i in range(cnt):print("*",end='')
    print()