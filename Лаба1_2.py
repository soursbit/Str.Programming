import math 
q = float
d = int(input("Введите d = "))
k = int(input("Введите k = "))
p = int(input("Введите p = "))
x = int(input("Введите x = "))
q = (math.sqrt(k+2.6*p*math.sin(k)))/(x - math.pow(d,3))
print(q)
