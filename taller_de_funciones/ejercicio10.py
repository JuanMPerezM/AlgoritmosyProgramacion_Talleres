frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
def posicion_elmemento(l1:list,elm:str):
  for i in l1:
    if(i==elm):
     p=l1.index(i)
     print (p)