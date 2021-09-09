archivo = open('paises.txt', 'r')
lista=[]
lista.append("Messismo: Messirve \n")
for i in archivo: 
  lista.append(i)
  a=" ".join(lista)
  print(a)
  a=[]
  lista=[]
archivo.close()