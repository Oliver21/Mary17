# -*- coding: utf-8 -*
from analizadorSintactico import *
from turtle import *
import turtle
import os

#esta funcion nos regresa el valor que contiene cierta posicion de memoria,
#primero ingresamos a esa posicion, extraemos el valor y dependiendo de su contenido regresamos ese valor
def damevalor(valor):
	revisado=str(valor)
	if revisado[0:4]=="mem-":
		revisado=revisado[4:]
		if revisado[0:4]=="mem-":
			revisado=damevalor(revisado)
		revisado=UnivMemManager.find(int(revisado))
		revisado=str(revisado)
		if revisado=="None":
			print "La variable a la que intentas acceder no tiene un valor asignado"
			sys.exit()
		if revisado[0]=="\"":
			revisado=revisado[1:len(revisado)-1]
			while revisado[0]=="\"":
				revisado=revisado[1:len(revisado)-1]
			return str(revisado)
		elif revisado[0]=="T":
			return True
		elif revisado[0]=="F":
			return False
		elif revisado.find(".")==-1:
			return int (revisado)
		else:
			return float(revisado)
	else:
		return int(revisado)
			
def dameposicion(valor):
	revisado=str(valor)
	revisado=revisado[4:]
	if revisado[0:4]=="mem-":
		#revisado=revisado[4:]
		revisado=damevalor(revisado)
	return int(revisado)


dibujo=False
#esta funcion se activa en caso de que el usuario use alguna de las funciones especiales para dibujar
def tablero():
	if dibujo==False:
		tess = turtle.Turtle()
		setup(940, 680, 0, 0)
		title("MARY17")
		speed(1)

#servira para saber si tenemos llamadas anidadas			
memoriaFuncion=10000
memoriaInicialFuncion=10000
PFunciones=Stack()
PValores=Stack()
PNombres=Stack()
nombrefuncion = None
#print "---------------------------------------------------------------------"
#print "-----------------MAQUINA VIRTUAL-------------------------------"
i = 0
while i < len(cuadru):
	valor1=cuadru[i].pos1
	valor2=cuadru[i].pos2
	valor3=cuadru[i].pos3
	valor4=cuadru[i].pos4
	#cuadruplo que realiza operacion de suma
	if valor1=="+":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		if type(valor2) == str or type(valor3) == str:
			valor2 = str(valor2)
			valor3 = str(valor3)
			resultado = valor2 + valor3
			resultado = "\"" + str(resultado) + "\""
		else:
			resultado = valor2 + valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de resta
	elif valor1=="-":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 - valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de multiplicacion
	elif valor1=="*":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 * valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de division
	elif valor1=="/":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 / valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de asignacion (=)
	elif valor1=="=":
		valor2=damevalor(valor2)
		if type(valor2) == str:
			valor2 = "\"" + valor2 + "\""
		lugar=dameposicion(valor4)
		UnivMemManager.asigna(lugar, valor2)
	#cuadruplo que realiza operacion de comparacion (<)
	elif valor1=="<":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 < valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de comparacion (>)
	elif valor1==">":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 > valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de comparacion (<=)
	elif valor1=="<=":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 <= valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de comparacion (>=)
	elif valor1==">=":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 >= valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de comparacion (==)
	elif valor1=="==":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 == valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo que realiza operacion de comparacion (!=)
	elif valor1=="!=":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 != valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	#cuadruplo para cambiar de posicion en caso de que la evalucacion sea verdadera
	elif valor1=="GoToT":
		if damevalor(valor2):
			i = damevalor(valor4) - 1
	#cuadruplo para cambiar de posicion en caso de que la evalucacion sea falsa
	elif valor1=="GoToF":
		if damevalor(valor2):
			pass
		else:
			i = damevalor(valor4) - 1
	#cuadruplo para cambiar de posicion
	elif valor1=="GoTo":
		i = damevalor(valor4) - 1
	#cuadruplo para imprimir en pantalla
	elif valor1=="PRINT":
		print damevalor(valor4)
	#cuadruplo para leer del teclado
	elif valor1=="READ":
		lectura=raw_input()
		lectura="\"" + lectura + "\""
		UnivMemManager.asigna(dameposicion(valor4),lectura)	
	#cuadruplo para leer un valor numerico del teclado
	elif valor1=="READINT":
		lectura=int(raw_input())
		UnivMemManager.asigna(dameposicion(valor4),lectura)
	#cuadruplo que realiza operacion booleana (||)
	elif valor1=="||":
		if damevalor(valor2) or damevalor(valor3):
			UnivMemManager.asigna(dameposicion(valor4),True)
		else:
			UnivMemManager.asigna(dameposicion(valor4),False)
	#cuadruplo que realiza operacion booleana (&&)
	elif valor1=="&&":
		if damevalor(valor2) and damevalor(valor3):
			UnivMemManager.asigna(dameposicion(valor4),True)
		else:
			UnivMemManager.asigna(dameposicion(valor4),False)
	#FUNCIONES ESPECIALES
	#Dibuja un cuadrado en pantalla recibiendo como parametros , pos en x, pos en y y tamaño
	elif valor1=="CUADRADO":
		tablero()
		penup()
		inicioy=damevalor(valor3)
		iniciox=damevalor(valor4)
		tamano=damevalor(valor2)
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox+tamano, inicioy) #inferior derecha
		goto(iniciox+tamano, inicioy+tamano) #superior derecha
		goto(iniciox, inicioy+tamano) #superior izquierda
		goto(iniciox, inicioy) #inferior izquierda
		penup()
		dibujo=True
	#Dibuja un cubo en pantalla recibiendo como parametros , pos en x, pos en y y tamaño	
	elif valor1=="CUBO":
		tablero()
		penup()
		inicioy=damevalor(valor3)
		iniciox=damevalor(valor4)
		tamano=damevalor(valor2)
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox+tamano, inicioy) #inferior derecha
		goto(iniciox+tamano, inicioy+tamano) #superior derecha
		goto(iniciox, inicioy+tamano) #superior izquierda
		goto(iniciox, inicioy) #inferior izquierda
		penup()
		iniciox2=iniciox+(tamano/2)
		inicioy2=inicioy+(tamano/2)
		goto(iniciox2, inicioy2)
		pendown()
		goto(iniciox2+tamano, inicioy2) #inferior derecha
		goto(iniciox2+tamano, inicioy2+tamano) #superior derecha
		goto(iniciox2, inicioy2+tamano) #superior izquierda
		goto(iniciox2, inicioy2) #inferior izquierda
		penup()
		##############dibujamos diagonales##################
		goto(iniciox2+tamano, inicioy2) #inferior derecha
		pendown()
		goto(iniciox+tamano, inicioy) #inferior derecha
		penup()
		goto(iniciox2+tamano, inicioy2+tamano) #superior derecha
		pendown()
		goto(iniciox+tamano, inicioy+tamano) #superior derecha
		penup()
		goto(iniciox2, inicioy2+tamano) #superior izquierda
		pendown()
		goto(iniciox, inicioy+tamano) #superior izquierda
		penup()
		goto(iniciox2, inicioy2) #inferior izquierda
		pendown()
		goto(iniciox, inicioy) #inferior izquierda
		#############################################################
		penup()
		dibujo=True
	#Dibuja un triangulo en pantalla recibiendo como parametros , pos en x, pos en y y tamaño	 		
	elif valor1=="TRIANGULO":
		tablero()
		penup()
		inicioy=damevalor(valor3)
		iniciox=damevalor(valor4)
		tamano=damevalor(valor2)
		goto(iniciox, inicioy)
		pendown()
		goto(tamano+iniciox, inicioy)
		goto(iniciox+(tamano/2), tamano+inicioy)
		goto(iniciox, inicioy)
		penup()
		dibujo=True
		
	elif valor1=="MUEVE":
		tablero()
		muevey=damevalor(valor2)
		muevex=damevalor(valor3)
		goto(muevex, muevey)
		dibujo=True
		
	elif valor1=="APOYA":
		tablero()
		pendown()
		dibujo=True
		
	elif valor1=="LEVANTA":
		tablero()
		penup()
		dibujo=True
		
	elif valor1=="ESTRELLA":
		tablero()
		penup()
		inicioy=damevalor(valor3)
		iniciox=damevalor(valor4)
		tamano=damevalor(valor2)
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox+(tamano/2), inicioy+tamano)
		goto(iniciox+tamano, inicioy)
		goto(iniciox-(tamano*.2), inicioy+(tamano*(.6)))
		goto(iniciox+tamano+(tamano*.2), inicioy+(tamano*(.6)) )
		goto(iniciox, inicioy)
		penup()
		dibujo=True
	#Dibuja la fimra de nuestro lenguaje de programacion MARY 17
	elif valor1=="FIRMA":
		tablero()
		penup()
		iniciox=0
		inicioy=0
		goto(iniciox,inicioy)
		pendown()
		goto(iniciox,inicioy+30)
		goto(iniciox+15,inicioy+15)
		goto(iniciox+30, inicioy+30)
		goto(iniciox+30,inicioy)
		penup()
		iniciox=iniciox+40
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox, inicioy+30)
		goto(iniciox+30, inicioy+30)
		goto(iniciox+30, inicioy)
		goto(iniciox+30, inicioy+15)
		goto(iniciox, inicioy+15)
		penup()
		iniciox=iniciox+40
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox, inicioy+30)
		goto(iniciox+30, inicioy+30)
		goto(iniciox+30, inicioy+15)
		goto(iniciox, inicioy+15)
		goto(iniciox+15, inicioy+15)
		goto(iniciox+30, inicioy)
		penup()
		iniciox=iniciox+40
		goto(iniciox, inicioy)
		goto(iniciox+15, inicioy)
		pendown()
		goto(iniciox+15, inicioy+15)
		goto(iniciox, inicioy+30)
		goto(iniciox+15, inicioy+15)
		goto(iniciox+30, inicioy+30)
		penup()
		iniciox=iniciox+50
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox, inicioy+30)
		penup()
		iniciox=iniciox+10
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox+30, inicioy+30)
		goto(iniciox, inicioy+30)
		iniciox=iniciox-120
		inicioy=inicioy+40
		penup()
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox+30, inicioy+30)
		goto(iniciox+40, inicioy+15)
		goto(iniciox+50,inicioy+25)
		goto(iniciox+80, inicioy)
		dibujo=True
		penup()
		goto(0,0)

	#esta funcion es para separar espacios de memoria en donde se alamacenaran los datos de una funcion
	elif valor1=="ERA":
		nombrefuncion
		if nombrefuncion!=None:
			conta=0
			while TablaFunciones.get(nombrefuncion).getVarMemory(conta)!=None:
				posicion = TablaFunciones.get(nombrefuncion).getVarMemory(conta)
				PValores.push(UnivMemManager.find(int(posicion)))
				conta=conta+1
			PNombres.push(nombrefuncion)
		nombrefuncion=valor2
	#sirve para regresar a ejecutar una funcion al hacerse su llamada
	elif valor1 =="gosub":
		nombrefuncion=valor2
		PFunciones.push(i)
		i = TablaFunciones.get(nombrefuncion).Cont - 1
	#ENDPROC sirve para saber que se termino de ejecutar una funcion, por lo tanto regresamos a nuestra ejecucion normal
	elif valor1=="ENDPROC":
		nombrefuncion
		TablaFunciones.get(nombrefuncion).LocalTable.release()
		i=PFunciones.pop()
		nombrefuncion=None
		if PNombres.size()>0:
			nombrefuncion=PNombres.pop()
			conta=0
			while TablaFunciones.get(nombrefuncion).getVarMemory(conta)!=None:
				conta=conta+1
			while (conta > 0):
				posicion = TablaFunciones.get(nombrefuncion).getVarMemory(conta-1)
				UnivMemManager.asigna(int(posicion), PValores.pop())
				conta=conta-1
	#se pasan los parametros pertenecientes a una funcion
	elif valor1 =="param":
		parametro=int(valor4[5:])
		valorpara=damevalor(valor2)
		posicion = TablaFunciones.get(nombrefuncion).getVarMemory(parametro-1)
		UnivMemManager.asigna(int(posicion), valorpara)

	#regresa el resultado de una funcion
	elif valor1=="Return":
		valor=damevalor(valor2)
		memoria=TablaFunciones.get (nombrefuncion).ReturnValue.memory
		UnivMemManager.asigna (int(memoria), valor)
	# verifica que un valor se encuentre entre los limites de una variable dimensionada
	elif valor1=="Verifica":
		indice=damevalor(valor2)
		limiteInferior=damevalor(valor3)
		limiteSuperior=damevalor(valor4)
		if indice < limiteInferior or indice>limiteSuperior:
			print "Estas intentando acceder a valores fuera de la dimension de la variable"
			sys.exit()
		else:
			pass
		
	i = i+1

if (dibujo):
	raw_input("Press enter to continue")
		
