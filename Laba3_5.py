import math

n = int(input("Введите n: "))
z = 1
i = 1

while n*2 >=i:
    if i % 2!=0:
        z = z/math.pow(i,3)
        i = i + 1
    else:
        i = i + 1
print("Разность кубов = ",z)
