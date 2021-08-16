print("Escriba las calificaciones de los 3 parciales:")
c1, c2, c3 = map(float, input().split())
ef=float(input("Escriba la calificacion del examen final: " ))* 0.30
tf=float(input("Digite la calificacion del trabajo final: "))* 0.15
promedio=(c1+c2+c3)/3*0.55
cf=promedio+ef+tf
print("La calificacion final de la clase es de: ",cf)