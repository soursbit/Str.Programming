import math

x = float(input("Введите x: "))
y = 0

y = ((math.exp(x) - math.exp(-x))/2)*math.tan(x+1) - math.pow(math.tan(2+((math.exp(x) - math.exp(-x))/2)-1),2)

print("y = ",y)
