Algoritmo inicio_horas
	Escribir "escriba una cantidad de minutos"
	Leer m	
	h<- m/60
	ht=trunc(h)
	mf=(h-ht)*60
	mt=trunc(mf)
	Escribir "la cantidad de minutos en horas es= "  ht  "horas y "  mt   "minutos"
FinAlgoritmo
