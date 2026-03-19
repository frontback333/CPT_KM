arr = list(map(int,input().split()))
ad = int(input())
for i in range(3) :
    arr[2-i]+=ad
    if(arr[2-i]>=60) :
        ad=arr[2-i]//60
        arr[2-i]%=60
    else : break
for i in arr : print(i, end=" ")