"""
entrada
precio_pc-->int-->pc
precio_cuotas-->int-->cuo
salidas
recargo-->str-->r
"""
pc=int(input("digite el precio del producto con pago al contado "))
cuo = int(input("digite el precio del producto con pago a cuotas "))
rn=(cuo-pc)
r=(rn/cuo)*100
print("el recargo es de "+ str (r),"%")