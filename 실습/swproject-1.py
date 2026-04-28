balance = 1000
year = 0
while balance<2000:
    year+=1
    interest = balance*0.05
    balance +=interest
print("%d 년" %year)
print("%d 원" %balance)