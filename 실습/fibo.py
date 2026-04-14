import time
D=[0]*10000
D[1]=1
Dcount=0
count=0
def Dfibo(N):
    global Dcount
    Dcount+=1
    if D[N] or not N:return D[N]
    D[N]=Dfibo(N-1)+Dfibo(N-2)
    return D[N]
def fibo(N):
    global count
    count+=1
    if not N: return 0
    elif N==1:return 1
    else : return(fibo(N-1)+fibo(N-2))
n = int(input())
start = time.time()
print("DP 재귀 값:",Dfibo(n))
print("DP 재귀횟수:",Dcount,", DP 재귀시간:",time.time()-start)
start = time.time()
print("일반 재귀 값:",fibo(n))
print("일반 재귀횟수:",count,", 일반 재귀시간:",time.time()-start)