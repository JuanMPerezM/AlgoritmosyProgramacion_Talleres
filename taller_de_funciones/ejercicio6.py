frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
def palabras_por_letra (l1,elm):
  aux=[]
  for i in l1:
     if(i[0]==elm):
      aux.append(i)
  return aux
  