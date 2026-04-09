import sys
ck=[0]*10005
def sn():
    for i in range(1,10000):
        temp = i
        num = temp
        while(temp):
            num+=temp%10
            temp//=10
        if(num<10000):ck[num]=1

sn()
for i in range(1,10000):
    if not ck[i]:print(i)