archivo = open('paises.txt', 'r')
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print("La posición de la Capital de Colombia es "+str(c))
archivo.close()