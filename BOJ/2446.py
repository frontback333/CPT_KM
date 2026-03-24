N=int(input())
lop = 1+2*(N-1)
for i in range(N):
    for __ in range(i):print(" ",end='')
    for __ in range(lop):print("*",end='')
    print()
    lop-=2
lop+=4
for i in range(N-1,0,-1):
    for __ in range(i-1):print(" ",end='')
    for __ in range(lop):print("*",end='')
    print()
    lop+=2