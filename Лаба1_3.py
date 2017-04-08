import math 
n = float
z = int(input("Введите z = "))
x = int(input("Введите x = "))
a = int(input("Введите a = "))
n = (math.pow(z+math.sqrt(z*x),1/5))/(math.exp(x)+math.pow(a,5)*math.atan(x))
print(n)
