n = int(input("Введите n: "))
s = 1
r = 2

while r <= n:
    s = s + 1/r
    r = r + 1

print("S = ",s)
