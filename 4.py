a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
i = a
if a<b:
	for i in range(a,b):
		if (i%d == c):
			print(i)
elif a>b:
	for i in range(b,a) :
		if (i%d == c):
			print(i)
else:
	print("Чисел нет")

stop = int(input())  # чтобы не закрывалось окно