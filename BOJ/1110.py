a = int(input())
b = ((a%10)*10) + ((a%10) + (a//10))%10
cnt=1
while a!=b :
    b = ((b%10)*10) + ((b%10) + (b//10))%10
    cnt+=1
print(cnt)