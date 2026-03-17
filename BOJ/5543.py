a = list(int(input()) for _ in range (5))
print(min(min(a[0],a[1]),a[2])+min(a[3],a[4])-50)