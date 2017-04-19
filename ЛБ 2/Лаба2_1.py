import math

kr = int(input("Введите площадь круга: "))
kv = int(input("Введите площадь квадрата: "))

if (2*math.sqrt(kr)) >= (math.sqrt(2*math.pow(math.sqrt(kv),2))):
    print("Квадрат в круге поместится")
else:
    print("Квадрат в круге не поместится")

if (math.sqrt(kv)) >= (2*math.sqrt(kr/math.pi)):
    print("Круг поместится в квадрате")
else:
    print("Круг не поместится в квадрате")
