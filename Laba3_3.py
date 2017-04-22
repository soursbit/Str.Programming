import math

x = float(input("Введите x: "))
n = int(input("Введите сумму n членов: "))
p = 0
s = 1
i = 1

while i <=  n:
    if i % 2 == 0:
        p = p - math.pow(x,s)/s
        s = s + 2
        i = i + 1
    else:
        p = p + math.pow(x,s)/s
        s = s + 2
        i = i + 1
print("Ответ: ",p)
