x = int(input("Введите x: "))

for i in range(1,x):
	if (x%i == 0):
		print(i)

stop = int(input())  # чтобы не закрывалось окно