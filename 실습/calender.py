date_quantity = [31,28,31,30,31,30,31,31,30,31,30,31]
month = int(input())
startdate = 1
for i in range(month-1):
    startdate += date_quantity[i]
startdate %= 7
print(f"        {month}월")
print("일 월 화 수 목 금 토")
for i in range(startdate):
    print("   ",end='')
for i in range(date_quantity[month+1]):
    if (startdate + i)%7==0 and startdate+i>=7:
        print()
    print(f"{i+1:2d}",'',end='')