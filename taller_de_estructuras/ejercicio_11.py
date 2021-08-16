"""
entrada
nombre-->str-->n
horas_trabajadas-->int-->ht
precio_hora_normal-->int-->phn
horas _extras-->int-->hx
#hijos-->int-->hi
salidas
asignaciones-->str-->asi
deducciones-->str-->dd
sueldo_neto-->str-->sn
"""
n=str(input("escriba el nombre del trabador "))
ht=int(input("digite la cantidad de horas trabajadas "))
phn=int(input("digite el precio de la hora normal de trabajo "))
hx = int(input("digite la cantidad de horas extra trabajadas "))
hi=int(input("digite cuantos hijos tiene "))
if (hi==0):
  ch=0
else: 
    ch=173000
ac=250000
ph=180000
asi=ac+ph+(ch*hi)
vhx = ht*0.25
hxt = vhx+ht
sb = (ht*phn)+hxt+asi
td = ((sb*0.05)+(sb*0.02)+(sb*0.07))
sn = sb-td
print(str(n), "tiene un total de " + str(asi), " en asignaciones")
print(str(n), "tiene un total de  " + str(td), " en deducciones")
print(str(n), "tiene un sueldo neto de " + str(sn))