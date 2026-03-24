WD = input()
sum = 0
ck = 0
for i in WD:
    od = ord(i)
    if od<97:sum+=od-38
    else:sum+=od-96
for i in range(1,int(sum**0.5)):
    if not sum%(i+1):
        ck+=1
if ck:print("It is not a prime word.")
else:print("It is a prime word.")