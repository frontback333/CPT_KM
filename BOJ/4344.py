T=int(input())
for i in range(T):
    K = list(map(int,input().split()))
    sum=0
    for i in range(len(K)-1): sum+=K[i+1]
    avg = sum/K[0]
    cnt=0
    for i in range(len(K)-1):
        if K[i+1]>avg:cnt+=1
    print(f"{cnt/K[0]*100:.03f}%")