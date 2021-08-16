"""
entrada
valor_prestamo-->int-->vp
valor_intereses-->int-->vi
tiempo-->in-->t
salida
intereses-->str-->inter
"""
vp=int(input ("ingrese el valor del pestramo " ))
vi=int(input ("ingrese el valor de los intereses "))
inter=(vp*4*vi)/100
print("el interes en cuatro años es del " +str (inter))