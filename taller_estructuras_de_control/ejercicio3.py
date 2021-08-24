"""
Entradas
a -> int -> dato
b -> int -> dato
c -> int -> dato
d -> int -> dato
"""
inp = entrada (). dividir ()
a , b , c , d = inp
a = int ( a )
b = int ( b )
c = int ( c )
d = int ( d )
si ( d == 0 ):
    imprimir ((( a - c ) ** 2 ))
otra cosa :
    imprimir ((( a - b ) ** 3 ))