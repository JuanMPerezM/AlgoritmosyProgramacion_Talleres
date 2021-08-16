"""
entradas
chelines_auztriacos-->int-->ca
dracmas_griegos-->int-->dg
pesetas-->int-->p
salidas
pesetas_r-->str-->pr
francos_franceses-->str-->ff
dolares-->str-->d
liras_italianas-->str-->li
"""
ca=int(input("digite su cantidad en chelines austriacos "))
dg= int(input("digite su cantidad en dracmas griegos "))
p = int(input("digite su cantidad en pesetas "))
pr = ca*9568.71
ff=(dg*886.07)/20110
d=p*122499
li=p*92.89
print(str(ca),"chelines austriacos son equivalentes a " + str (pr)," pesetas")
print(str(dg),"dracmas griegos son equivalente  " + str (ff)," francos franceses")
print(str(p) ,"pesetas son eqivalente a " + str (d)," dolares")
print(str(p), "pesetas son eqivalente a " + str(li)," liras italianas")