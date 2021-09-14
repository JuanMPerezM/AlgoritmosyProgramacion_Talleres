frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
def elimina_elemento_lista(lista:list, elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
"""
if __name__ == "__main__":
  lista_frutas_nueva=elimina_elemento_lista(lista_frutas,"\n")
  lista_frutas_sin_Kiwi=elimina_elemento_lista(lista_frutas_nueva,"Kiwi")
  print(lista_frutas_sin_Kiwi)
"""