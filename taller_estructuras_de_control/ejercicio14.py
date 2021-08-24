"""
entrada
diferencia de la lectura anterior -> flotar -> difl
diferencia de la lecura actual -> flotar -> da
salida
total de factura -> flotar -> total
"""
difl = float ( input ( "Digite el valor de la lectura anterior:" ))
da = float ( input ( "Digite el valor de la lectura actual:" ))
co = difl - da
si ( co <= 100 ):
    total = ( co * 4600 )
elif ( co > = 101  y  co <= 300 ):
    total = ( co * 80000 )
elif ( co > = 301  y  co <= 500 ):
    total = ( co * 100000 )
elif ( co > = 501 ):
    total = ( co * 120000 )
print ( "El monto a pagar es:" + str ( total ))