mx=0
idx = 0
for i in range(9):
    ipt = int(input())
    if(ipt>mx):
        mx=ipt
        idx=i+1
print(mx,idx)