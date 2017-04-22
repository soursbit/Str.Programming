import math

x = int(input("Введите x:"))
k = int(input("Введите k:"))
U = 0
u1 = 0
u2 = 1
t = 2
i = 1


for t in range(t,k+1):
    if t != 3:
        for i in range(i,t+1):
            if i != 2 and i != 7:
                u1 = u1 + ((i - 2)/(i - 7))
        u2 = ((t*math.pow(x,t))/(t-3))*u1
print("Ответ: ",u2)
        
                
                
            
