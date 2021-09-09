archivo = open('paises.txt', 'r')
c=0
lista=[]
for i in archivo:
  c=c+1
print("El total de países es de: ",c)
archivo.close()