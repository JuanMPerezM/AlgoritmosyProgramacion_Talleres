"""
Entradas
Dato 1-->int-->x
Dato 2-->int-->m
Salidas
"""
while True:
    inp=input().split()
    x,m=inp
    x=int(x)
    m=int(m) 
    if (x==0 and m==0):
        break
    else:
         n=x*m
         print(n)