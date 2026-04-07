C = int(input())
for _ in range(C):
    st=str(input())
    score=0
    ad=0
    for i in st:
        if i == 'O':
            ad+=1
            score+=ad
        else:
            ad=0
    print(score)