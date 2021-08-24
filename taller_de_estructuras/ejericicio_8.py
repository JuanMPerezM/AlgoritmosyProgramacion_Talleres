inp=input().split(" ")
a,b,c=inp
a=int(a)
b=int(b)
c=int(c)
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("El area del triangulo es "+str(d))