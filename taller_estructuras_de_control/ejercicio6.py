"""
Entradas
a -> int -> Digito
b -> int -> Digito
c -> int -> Digito
d -> int -> Digito
"""
a = int ( input ( "Ingrese un solo dígito:" ))
b = int ( input ( "Ingrese un solo dígito:" ))
c = int ( input ( "Ingrese un solo dígito:" ))
d = int ( input ( "Ingrese un solo dígito:" ))
e = cadena ( c ) + cadena ( d )
f = int ( e )
si ( f <= 50 ):
    g = ( cadena ( a ) + cadena ( b ) + "00" )
otra cosa :
    g = ( cadena ( a ) + cadena ( b + 1 ) + "00" )
imprimir ( g )