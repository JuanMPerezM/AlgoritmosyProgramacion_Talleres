archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
lista2=[]
for i in archivo:
  a=i.index(":")
for i in range(0,len(i)):
  lista2.remove("rey julien")
  lista2.insert("Madagascar: Antananarivo")
  print(lista2)
archivo.close()