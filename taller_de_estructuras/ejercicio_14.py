"""
entrada
lectura_anterior-->int-->lan
lectura_actual-->int-->lac
costo_kilovati-->int-->k
salida
monto_pago-->str-->mp
"""
lan=int(input("inglese el valor de la lectura anterior "))
lac=int(input("inglese el valor de la lectura actual "))
k=int(input("inglese el costo por kilovatio "))
lt=lan-lac
mp=k*lt
print("al valor a pagar de $"+ str (mp))