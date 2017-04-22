import math

n = float(input("Введите число n: "))
b = 1.6
y = 0
a = 0
x = 0

a = math.sin(math.pow(x,2) + math.pow(b,2))
y = math.log(a,math.e)/math.log10(math.pow(b,3))
x = math.pow(n,b) + math.pow(b,2)

print("a = ",a)
print("y = ",y)
print("x = ",x)
