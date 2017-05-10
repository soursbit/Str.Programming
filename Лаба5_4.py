n = int(input("Введите N: "))
m = int(input("Введите M: "))
i = 1
j = 1
s = 0
arr = [[int(input()) for i in range(n)] for j in range(m)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()
    
for j in range(len(arr[i])):
    for i in range(len(arr)):
        s = s + arr[i][j]
    print("Сумма",j+1,"столбца",s)
    s = 0
 
