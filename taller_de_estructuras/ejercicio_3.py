print("Digite las ventas concretadas: ")
v1, v2, v3 =map(int, input().split())
sb=float(input("Digite su sueldo base: "))
c=float((v1+v2+v3)*0.10)
total=float(sb+c)
print("Obtendrá por concepto de comisiones por las 3 ventas: ", c)
print("Su pago total es de: ",total)