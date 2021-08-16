"""
entrada
horas_trabajadas-->int-->ht
precio_hora-->int-->ph
salidas
sueldo_neto-->str-->sn
"""
ht=int(input ("ingrese el numero de horas trabajadas ") )
ph=int(input("ingrese el valor de la hora de trabajo "))
s=ht*ph
sn=(s*0.2)
snt=s-sn
print("el sueldo neto es de " +str (snt))