x = float(input("Введите x пробег в первый день: "))
y = float(input("Введите y пробег, который должен быть: "))
i = 1
if x != y:
	while x<y:
		x = x + (x*0.1)
		i += 1
	print("№ Дня = ",i)
else:
	print("Пробег равен первому дню")
stop = int(input())  # чтобы не закрывалось окно