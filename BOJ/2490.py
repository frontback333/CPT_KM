for _ in range(3) :
    arr = list(map(int,input().split()))
    cnt = 0
    for i in arr :
        if i : cnt+=1
    if cnt==4 : print("E")
    elif cnt==3 : print("A")
    elif cnt==2 : print("B")
    elif cnt==1 : print("C")
    else : print("D")