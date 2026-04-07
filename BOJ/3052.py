L=[]
for _ in range(10):
    val = int(input())%42
    if not val in L:
        L.append(val)
print(len(L))