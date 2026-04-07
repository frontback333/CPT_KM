T=int(input())
for _ in range(T):
    st = str(input())
    ck=0
    for i in st:
        if i == '(': ck+=1
        else : ck -= 1
        if ck<0 : break
    if ck == 0 : print("YES")
    else : print("NO")