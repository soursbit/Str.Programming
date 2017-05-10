n = int(input("Введите N: "))
m = int(input("Введите M: "))
i = 1
j = 1
s = 0
arr = [[int(input()) for i in range(n)] for j in range(m)]
a = []

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (arr[i][j]>=1) and (arr[i][j]<=10):
            a.append(arr[i][j])
print(a)
    
