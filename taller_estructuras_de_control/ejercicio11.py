"""
Entradas
Temperatura -> flotar -> t
Salidas
Deporte -> str -> d
"""
t = float ( input ( "Ingrese la temperatura:" ))
si ( t > 85 ):
  d = "Natación"
elif ( t > 70  y  t <= 85 ):
  d = "Tenis"
elif ( t > 32  y  t <= 70 ):
  d = "Golf"
elif ( t > 10  y  t <= 32 ):
  d = "Esqui"
elif ( t <= 10 ):
  d = "Marcha"
print ( "El deporte que puede practicar es:" + str ( d ))