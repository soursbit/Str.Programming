s = str(input("Введите предложение: "))

s=s.strip()
st=[]

for i in range(len(s)):
    n=s.find(" ")
    if n==-1:
        st.append(s)
        break
    st.append(s[:n])
    s=s[n+1:]
    s=s.lstrip()
at=[]
max_l=0
for i in range(len(st)):
    if len(st[i])>max_l:
        at=[]
        at.append(st[i])
        max_l=len(st[i])
    elif len(st[i])==max_l:
        at.append(st[i])
        
if len(at)>1:
    print('В предложении есть несколько слов максимальной длины')
else:
    print(str(at[0]))
