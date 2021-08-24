"""
Entradas
Salario -> flotar -> s
Ventas_1 -> flotar -> v1
Ventas_2 -> flotar -> v2
Ventas_3 -> flotar -> v3
Salidas
Total_1 -> flotar -> t1
Total_2 -> flotar -> t2
Total_3 -> flotar -> t3
"""
s = float ( input ( "escriba su salario bruto:" ))
v1 = float ( input ( "escriba las ventas del departamento 1:" ))
v2 = float ( input ( "escriba las ventas del departamento 2:" ))
v3 = float ( input ( "escriba las ventas del departamento 3:" ))
vt = v1 + v2 + v3
p = vt * 0,33
si ( v1 > p ):
  t1 = ( s * 0,20 ) + s
otra cosa :
  t1 = s
si ( v2 > p ):
  t2 = ( s * 0,20 ) + s
otra cosa :
  t2 = s
si ( v3 > p ):
  t3 = ( s * 0,20 ) + s
otra cosa :
  t3 = s
print ( "El pago del departamento 1 es: $" , "{: .0f}" . formato ( t1 ))
print ( "El pago del departamento 2 es: $" , "{: .0f}" . formato ( t2 ))
print ( "EL pafo del departamento 3 es: $" , "{: .0f}" . formato ( t3 ))