print("Последнее полнолуние было 27 августа")
a = 27
b = 0

while b != 28:
    if a == 31:
        a = 0
    b = b + 1
    a = a + 1
print("Следующее полнолуние: ",a," числа следующего месяца")
