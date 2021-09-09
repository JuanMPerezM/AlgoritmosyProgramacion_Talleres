archivo = open('paises.txt', 'r')
lista=[]
ciudad=[]
c=0
for i in archivo:
  if (i[0]=="E"):
    lista.append(i)
    a="".join(lista)
    lista=[]
    a=i.index(":")
    for r in range (a+2,len(i)):
      ciudad.append(i[r])
    a="".join(ciudad)
    c=c+1
    print(a)
    print(c)
    ciudad=[]
archivo.close()