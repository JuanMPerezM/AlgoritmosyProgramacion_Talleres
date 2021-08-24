"""
Entradas
Dia -> int -> d
Mes -> int -> m
Año -> int -> a
Salidas
Signo -> str -> s
Edad -> int -> e
"""
d = int ( input ( "Ingrese el dia de nacimiento:" ))
m = int ( input ( "Ingrese el mes de nacimiento en numero:" ))
a = int ( input ( "Ingrese su año de nacimiento:" ))
si (( m == 11 ) y ( d > = 22 )) o (( m == 12 ) y ( d <= 21 )):
  s = "Sagitario"
elif (( m == 12 ) y ( d > = 22 )) o (( m == 1 ) y ( d <= 20 )):
  s = "Capricornio"
elif (( m == 1 ) y ( d > = 21 )) o (( m == 2 ) y ( d <= 19 )):
  s = "Acuario"
elif (( m == 2 ) y ( d > = 20 )) o (( m == 3 ) y ( d <= 19 )):
  s = "Piscis"
elif (( m == 3 ) y ( d > = 21 )) o (( m == 5 ) y ( d <= 21 )):
  s = "Tauro"
elif (( m == 5 ) y ( d > = 22 )) o (( m == 6 ) y ( d <= 21 )):
  s = "Géminis"
elif (( m == 6 ) y ( d > = 22 )) o (( m == 7 ) y ( d <= 22 )):
  s = "Cáncer"
elif (( m == 7 ) y ( d > = 23 )) o (( m == 8 ) y ( d <= 23 )):
  s = "Leo"
elif (( m == 8 ) y ( d > = 24 )) o (( m == 9 ) y ( d <= 22 )):
  s = "Virgo"
elif (( m == 9 ) y ( d > = 23 )) o (( m == 10 ) y ( d <= 22 )):
  s = "Libra"
elif (( m == 10 ) y ( d > = 23 )) o (( m == 11 ) y ( d <= 21 )):
  s = "Escorpión"
si (( m == 8 ) y ( d > = 24 )) o (( m == 9 ) y ( d <= 22 )):
  e = 2021 - a - 1
elif (( m == 9 ) y ( d > = 23 )) o (( m == 10 ) y ( d <= 22 )):
  e = 2021 - a - 1
elif (( m == 10 ) y ( d > = 23 )) o (( m == 11 ) y ( d <= 21 )):
  e = 2021 - a - 1
elif (( m == 11 ) y ( d > = 22 )) o (( m == 12 ) y ( d <= 21 )):
  e = 2021 - a - 1
elif (( m == 12 ) y ( d > = 22 )) o (( m == 1 ) y ( d <= 20 )):
  e = 2021 - a - 1
otra cosa :
  e = 2021 - a
print ( "Su signo es:" + str ( s ))
print ( "Su edad es:" , "{: .0f}" . formato ( e ))