  
"""
entradas
nbilletes50-->int-->n1
nbilletes20-->int-->n2
nbilletes10-->int-->n3
nbilletes5-->int-->n4
nbilletes2-->int-->n5
nbilletes1-->int-->n6
nbilletes500-->int-->n7
nbilletes100-->int-->n8
salidas
total_dinero-->str-->td
"""
n1=(int(input("digite la cantidad de billetes de $50000 ")))
n2=(int(input("digite la cantidad de billetes de $20000 ")))
n3=(int(input("digite la cantidad de billetes de $10000 ")))
n4=(int(input("digite la cantidad de billetes de $5000 ")))
n5=(int(input("digite la cantidad de billetes de $2000 ")))
n6=(int(input("digite la cantidad de billetes de $1000 ")))
n7=(int(input("digite la cantidad de billetes de $500 ")))
n8=(int(input("digite la cantidad de billetes de $100 ")))
td=(n1*50000)+(n2*20000)+(n3*10000)+(n4*5000)+(n5*2000)+(n6*1000)+(n7*500)+(n8*100)
print("el total de dinero es $" + str (td))