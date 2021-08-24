"""
entradad
nota_tarea1_mates-->int-->num
nota_tarea2_mates-->int-->ndm
nota_tarea3_mates-->int-->ntm
examen_mates-->float-->xm
nota_tarea1_fisik-->int-->nuf
nota_tarea2_fisik-->int-->ndf
examen_f-->float-->xf
nota_tarea1_q-->int-->nuq
nota_tarea2_q-->int-->ndq
nota_tarea3_q-->int-->ntq
examen_q-->float-->xq
salidas
promedio_mates-->str-->pm
promedio_fisik-->str-->pf
promedio_quimik-->str-->pq
promedio_total-->str-->pg
"""
num=int(input("digite la nota #1 de su tareas de matematicas ")) 
ndm=int(input("digite la nota #2 de su tareas de matematicas "))
ntm=int(input("digite la nota #3 de su tareas de matematicas "))
xm=int(input("digite la nota del examen de matematicas "))
nuf = int(input("digite la nota #1 de su tareas de fisica "))
ndf = int(input("digite la nota #2 de su tareas de fisica "))
xf = int(input("digite la nota del examen de fisica "))
nuq = int(input("digite la nota #1 de su tareas de quimica "))
ndq = int(input("digite la nota #2 de su tareas de quimica "))
ntq = int(input("digite la nota #3 de su tareas de quimica  "))
xq = int(input("digite la nota del examen de quimica  "))
pm=(((num+ndm+ntm)/3)*0.1)+(xm*0.9)
pf = (((nuf+ndf)/2)*0.2)+(xf*0.8)
pq = (((nuq+ndq+ntq)/3)*0.15)+(xq*0.85)
pg=(pm+pf+pq)/3
print("su promedio en matematicas es de "+str (pm))
print("su promedio en fisica es de "+str(pf))
print("su promedio en quimica es de "+str(pq))
print("su promedio en general en estas tres materias es de "+str(pg))