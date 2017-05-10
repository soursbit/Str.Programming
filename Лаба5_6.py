n = int(input("Введите N: "))
i = 1
j = 1
s = 0

arr = [[int(input()) for i in range(n)] for j in range(n)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()

arr = [arr[i][i] for i in range(len(arr))]
arr.sort()
print(arr)


        

