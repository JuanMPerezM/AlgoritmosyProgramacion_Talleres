frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
def eliminar_un_caracter_de_toda_la_lista(lista:list, elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar