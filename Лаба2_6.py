import math

x = float(input("Введите точку по оси x: "))
y = float(input("Введите точку по оси y: "))

b = -(math.pow(x,2))+2

if  math.fabs(y) == b:
    print("Входит")
else:
    print("Не входит ")
