import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if math.fabs(c - a) > math.fabs(b - a):
    print("b находится ближе к a")
elif math.fabs(c - a) == math.fabs(b - a):
    print("находятся на одинаковом растоянии")
else:
    print("c находится ближе к a")

