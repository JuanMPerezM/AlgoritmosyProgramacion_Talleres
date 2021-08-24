  
"""
Entradas
cantidad invertida -> int -> invertida
Tasa de interes -> flotar -> tasa
Salida
Saldo -> flotar -> saldo
"""
invertida = float ( input ( "Cantidad a invertir:" ))
tasa = float ( input ( "Tasa de interes:" ))

x = invertida * tasa
si  x > 100_000 :
    print ( "la cantidad generada por concepto de interes es:" , x , "supera los 100000" )
otra cosa :
    print ( "la cantidad generada por concepto de interes es de:" , x , "no supera los 100000" )
print ( "Saldo de la cuenta:" , invertida + x )