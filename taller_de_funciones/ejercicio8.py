frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
def informacion_lista(lista:list)->list:
  auxiliar=[]
  for i in lista:
    print(len(lista))
  return auxiliar
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_fruta_nueva)
  lista_fruta_dos=tamano_lista(lista_fruta_nueva)
  print(lista_fruta_dos)
  lista_fruta_dos=informacion_lista
  print(type(lista_fruta_nueva))
"""
  