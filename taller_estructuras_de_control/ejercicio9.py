"""
Entradas
a -> int -> Monto de la compra
Salidas
b -> int -> Valor final de la compra
"""
a = int ( entrada ())
si ( a < 50000 ):
    b = "El valor de la compra es" + str ( a )
elif ( a > 50000  y  a < 100000 ):
    b = "El valor de la compra es" + str ( a - ( a * 0.05 ))
elif ( a > = 100000  y  a < 700000 ):
    b = "El valor de la compra es" + str ( a - ( a * 0.11 ))
elif ( a > = 700000  y  a < 1500000 ):
    b = "EL valor de la compra es" + str ( a - ( a * 0.18 ))
elif ( a > = 1500000 ):
    b = "El valor de la compra es" + str ( a - ( a * 0.25 ))
imprimir ( b )