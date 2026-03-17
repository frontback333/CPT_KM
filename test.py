lt = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
d = input("요일: ")
ad = int(input("일수: "))
tmp = 0
for i in range(7) :
    if(lt[i]==d) : tmp = i
print("요일 = ",lt[tmp+ad%7])