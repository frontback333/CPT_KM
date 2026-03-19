arr = list(map(int,input().split()))
ad = int(input())
for i in range(3) :
    arr[2-i]+=ad
    if(i!=2 and arr[2-i]>=60) :
        ad=arr[2-i]//60
        arr[2-i]%=60
    else : 
        ad=0
arr[0]%=24
for i in arr : print(i, end=" ")