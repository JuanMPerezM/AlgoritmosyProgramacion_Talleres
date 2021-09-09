archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print(a)
archivo.close()