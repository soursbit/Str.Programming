s = str(input("Введите строку: "))
i = 0
r = len(s)
z = 0
l = int

while i<= r-1:
    if s[i] == 'я' or s[i] == 'Я':
        print(" ")
        i = i + 1
    else:
        l = ord(s[i])
        print(chr(l+1))
        i = i + 1
        
