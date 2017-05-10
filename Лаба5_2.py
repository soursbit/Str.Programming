n=int(input())
massiv=[x for x in input().split()]
spisok=[]
for i in range(n-1):
    if massiv[i] in massiv[i+1::] and massiv[i] not in spisok:
        spisok.append(massiv[i])
print(' '.join(spisok))


