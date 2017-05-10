n = int(input("Введите кол-во чисел в массиве: "))
i = 1
s = 0
t = 0
arr = [int(input()) for i in range(n)]
for i in range(n-1):
    if arr[i]> arr[i+1]:
        print('Индекс элеммента: ',i+1)
        s = s + 1
            
if arr[n-1]>arr[0]:
    print('Индекс элеммента: ',n)
    s = s + 1
