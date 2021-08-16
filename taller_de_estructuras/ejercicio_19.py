"""
entrada
lote-->int-->x
venta-->int-->k
docenas-->int-->y
salida
descuento-->int-->d
"""
X = int(input("digite el numero de lotes "))
K= int(input("valor total de ventas"))
Y= int(input("cantidad de docenas "))
pp = (K*Y)-X
d = 100-((X/pp)*100)
print("La ganancia " + str(d), "%")