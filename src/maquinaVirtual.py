# -*- coding: utf-8 -*
from analizadorSintactico import *
from turtle import *
import turtle
import os


def damevalor(valor):
	revisado=str(valor)
	if revisado[0:4]=="mem-":
		revisado=revisado[4:]
		if revisado[0:4]=="mem-":
			revisado=damevalor(revisado)
		#return revisado
		revisado=UnivMemManager.find(int(revisado))
		revisado=str(revisado)
		if revisado[0]=="\"":
			revisado=revisado[1:len(revisado)-1]
			while revisado[0]=="\"":
				revisado=revisado[1:len(revisado)-1]
			#print revisado
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





def damevalor2(valor):
	revisado=str(valor)
	if revisado[0:4]=="mem-":
		revisado=revisado[4:]
		if revisado[0:4]=="mem-":
			revisado=damevalor(revisado)
		revisado=UnivMemManager.find(int(revisado))
		return revisado
	elif revisado[0]=="\"":
		return str(revisado[1:len(revisado)-1])
	elif revisado[0]=="T":
		return True
	elif revisado[0]=="F":
		return False
	else:
		revisado=revisado
		if revisado.find(".")==-1:
			return int(revisado)
		else:
			return float(revisado)
			
def dameposicion(valor):
	revisado=str(valor)
	revisado=revisado[4:]
	if revisado[0:4]=="mem-":
		#revisado=revisado[4:]
		revisado=damevalor(revisado)
	return int(revisado)


dibujo=False
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
	
	if valor1=="+":
		#print "Aqui hay una suma"
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
	elif valor1=="-":
		#print "Aqui hay una resta"
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 - valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	elif valor1=="*":
		#print "Aqui hay una multiplicacion"
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 * valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	elif valor1=="/":
		#print "Aqui hay una division"
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 / valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
	elif valor1=="=":
		#print "Aqui hay una ="
		valor2=damevalor(valor2)
		if type(valor2) == str:
			valor2 = "\"" + valor2 + "\""
		lugar=dameposicion(valor4)
		#print "Asigna el valor " + str(valor2) + " a la posicion " + str(lugar) 
		UnivMemManager.asigna(lugar, valor2)
	elif valor1=="<":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 < valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
		#print "Aqui hay una <"
	elif valor1==">":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 > valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
		#print "Aqui hay una >"
	elif valor1=="<=":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 <= valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
		#print "Aqui hay una <="
	elif valor1==">=":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 >= valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
		#print "Aqui hay una >="
	elif valor1=="==":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 == valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
		#print "Aqui hay una =="
	elif valor1=="!=":
		valor2=damevalor(valor2)
		valor3=damevalor(valor3)
		resultado = valor2 != valor3
		UnivMemManager.asigna(dameposicion(valor4),resultado)
		#print "Aqui hay una !="
	elif valor1=="GoToT":
		if damevalor(valor2):
			i = damevalor(valor4) - 1
		#print "Aqui hay una gotot"
	elif valor1=="GoToF":
		if damevalor(valor2):
			pass
		else:
			i = damevalor(valor4) - 1
		#print "Aqui hay una gotof"
	elif valor1=="GoTo":
		i = damevalor(valor4) - 1
		#print "Aqui hay una goto"
	elif valor1=="PRINT":
		print damevalor(valor4)
	elif valor1=="READ":
		lectura=raw_input()
		lectura="\"" + lectura + "\""
		UnivMemManager.asigna(dameposicion(valor4),lectura)
		#print (entrada)
		#print "Aqui hay una read"		

	elif valor1=="READINT":
		lectura=int(raw_input())
		UnivMemManager.asigna(dameposicion(valor4),lectura)

	elif valor1=="||":
		if damevalor(valor2) or damevalor(valor3):
			UnivMemManager.asigna(dameposicion(valor4),True)
		else:
			UnivMemManager.asigna(dameposicion(valor4),False)
	elif valor1=="&&":
		if damevalor(valor2) and damevalor(valor3):
			UnivMemManager.asigna(dameposicion(valor4),True)
		else:
			UnivMemManager.asigna(dameposicion(valor4),False)
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
		i=0
		while i<5:
			forward(50)
			right(144)
			i=i+1
		penup()
		dibujo=True

	elif valor1=="ERA":
		nombrefuncion
		#print nombrefuncion
		if nombrefuncion!=None:
			conta=0
			while TablaFunciones.get(nombrefuncion).getVarMemory(conta)!=None:
				posicion = TablaFunciones.get(nombrefuncion).getVarMemory(conta)
				PValores.push(UnivMemManager.find(int(posicion)))
				conta=conta+1
			PNombres.push(nombrefuncion)

		nombrefuncion=valor2
		#PNombres.push(nombrefuncion)

	elif valor1 =="gosub":
		nombrefuncion=valor2
		PFunciones.push(i)
		i = TablaFunciones.get(nombrefuncion).Cont - 1
		
	elif valor1=="ENDPROC":
		nombrefuncion
		#borramos todo el contenido de la memoria de funciones
		TablaFunciones.get(nombrefuncion).LocalTable.release()
		i=PFunciones.pop()
		nombrefuncion=None
		if PNombres.size()>0:
			nombrefuncion=PNombres.pop()
			conta=0
			while TablaFunciones.get(nombrefuncion).getVarMemory(conta)!=None:
				conta=conta+1
			#print "El nombrefuncion en la pila es " + nombrefuncion
			while (conta > 0):
				posicion = TablaFunciones.get(nombrefuncion).getVarMemory(conta-1)
				UnivMemManager.asigna(int(posicion), PValores.pop())
				conta=conta-1

	elif valor1 =="param":
		#decFunciones=True
		parametro=int(valor4[5:])
		valorpara=damevalor(valor2)
		posicion = TablaFunciones.get(nombrefuncion).getVarMemory(parametro-1)
		UnivMemManager.asigna(int(posicion), valorpara)
		#PValores.push(valorpara)
		#print "Se pasara el valor " + str(valorpara) + " a la posicion numero " + str(posicion)
		#print posicion
		#print UnivMemManager.find(posicion)
		#print UnivMemManager.find(10000)
		#print UnivMemManager.find(posicion)
	elif valor1=="Return":
		valor=damevalor(valor2)
		memoria=TablaFunciones.get (nombrefuncion).ReturnValue.memory
		UnivMemManager.asigna (int(memoria), valor)

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
		
