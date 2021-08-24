"""
entradas
edad -> int -> edad
hemoglobina -> int -> hemo
salidas
resultado -> str - r
"""
edad  =  int ( input ( "Su edad en meses" ))
hemo  =  float ( input ( "Su nivel de hemoglobina en%" ))
si ( edad  > =  0  y  edad  <=  1 ):
  si ( hemo  > =  12  y  hemo  <=  26 ):
    print ( "negatipo para Anemia" )
  otra cosa :
    print ( "positivo para anemia" )
elif ( edad  >  1  y  edad  <=  6 ):
  si ( hemo  > =  10  y  hemo  <=  18 ):
    print ( "negatipo para Anemia" )
  otra cosa :
    print ( "positivo para anemia" )
elif ( edad  >  6  y  edad  <=  12 ):
  si ( hemo  > =  11  y  hemo  <=  15 ):
    print ( "negatipo para Anemia" )
  otra cosa :
    print ( "positivo para anemia" )
elif ( edad  >  12  y  edad  <=  60 ):
  si ( hemo  > =  11,5  y  hemo  <=  15 ):
    print ( "negatipo para Anemia" )
  otra cosa :
    print ( "positivo para anemia" )
elif ( edad  >  60  y  edad  <=  120 ):
  si ( hemo  > =  12,6  y  hemo  <=  15,5 ):
    print ( "negatipo para Anemia" )
  otra cosa :
    print ( "positivo para anemia" )
elif ( edad  >  120  y  edad  <=  180 ):
  si ( hemo  > =  13  y  hemo  <=  15,5 ):
    print ( "negatipo para Anemia" )
  otra cosa :
    print ( "positivo para anemia" )