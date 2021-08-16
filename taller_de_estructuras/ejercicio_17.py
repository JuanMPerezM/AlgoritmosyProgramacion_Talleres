"""
entrada
presupuesto-->int-->p
salidas
pre_gineco-->str-->pn
pre_trauma-->str-->pt
pre_pedria-->str-->pp
"""
p=int(input("ingrese el presupuesto "))
pn=(p*0.4)
pt=(p*0.3)
pp=(p*0.3)
print("el presupuesto para ginecologia es de $" +str (pn))
print("el presupuesto para traumatologia es de $" + str(pt))
print("el presupuesto para pediatria es de $" + str(pp))