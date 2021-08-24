"""
entrada
precio_final-->int-->pf
precio_publico-->int-->pvp
salida
descuento-->int-->d
"""
pf=int(input("ingrese el precio final pagado "))
pvp=int(input("ingrese el precio de venta al publico "))
pp=pvp-pf
d=(pp/pvp)*100
print("el descuento es del " +str (d),"%")