i = 1000
s = 0

while i <= 9999:
    a = i % 10
    b = i % 100 // 10
    c = i % 1000 // 100 
    d = i % 10000 // 1000
    if a != b and a!=c and a!=d and b!= c and b!=d and c!=d:
        print(i)
        s = s + 1
        i = i + 1
    else:
        i = i + 1
print("Кол - во таких чисел",s)  

