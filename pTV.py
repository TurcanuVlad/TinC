a=int(input('Numarul de linii:'))
b=[]
sp=0
ss=0
sps=0
spj=0
sss=0
ssj=0
for i in range(0, a):
    c=[]
    for j in range(0,a):
        c.append(int(input('>')))
    b.append(c)
for i in range(0,a):
    for j in range(0,a):
        print(b[i][j], end=" ")
    print()
for i in range(0,a):
    sp+=b[i][i]
print('Suma elem. de pe diag. prnc.=', sp)
h=0
for i in b[::-1]:
    ss+=i[h]
    h+=1
print("Suma elem. de pe diag. sec.=", ss)
for i in range(0,a):
    for j in range(0,a):
        if i<j:
            sps+=b[i][j]
        if i>j:
            spj+=b[i][j]
print("Suma elem. aflate mai jos de diag. princip.=", spj)
print("Suma elem. aflate mai sus de diag. princip.=", sps)
for i in range(0,a):
     if(i+j)<(a-1):
         sss+=b[i][j]
     if (i+j)>(a-1):
        ssj+=b[i][j]
print("Suma elem. aflate mai jos de diag. sec.=", ssj)
print("Suma elem. aflate mai sus de diag. sec.=", sss)    