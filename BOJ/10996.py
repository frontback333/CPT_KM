N=int(input())
bt = N//2
tp = N-bt
for _ in range(N):
    for __ in range(tp):print("* ",end='')
    print()
    for __ in range(bt):print(" *",end='')
    print()