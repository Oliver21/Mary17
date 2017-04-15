#!/usr/bin/python
from analizadorSintactico import *
from turtle import *
import turtle


tess = turtle.Turtle()
setup(640, 480, 0, 0)
title("Ejemplo de ventana")
speed(1)

def damevalor(valor):
	revisado=str(valor)
	if revisado[0:4]=="mem-":
		revisado=revisado[4:]
		revisado=UnivMemManager.find(int(revisado))
		return revisado
	elif revisado[0]=="\"":
		return str(revisado[1:len(revisado)-1])
	elif revisado[0]=="T" or revisado[0]=="F":
		return bool(revisado)
	else:
		revisado=revisado
		if revisado.find(".")==-1:
			return int(revisado)
		else:
			return float(revisado)
			
def dameposicion(valor):
	revisado=str(valor)
	revisado=revisado[4:]
	return int(revisado)
	
	

print "-----------------MAQUINA VIRTUAL-------------------------------"
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
		lugar=dameposicion(valor4)
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
		#print "Aqui hay una print"
		print damevalor(valor4)
	elif valor1=="READ":
		entrada= raw_input()
		print (entrada)
		#print "Aqui hay una read"		
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
		penup()
		inicioy=damevalor(valor3)
		iniciox=damevalor(valor4)
		tamano=damevalor(valor2)
		goto(iniciox, inicioy)
		pendown()
		goto(iniciox+tamano, inicioy)
		goto(iniciox+tamano, inicioy+tamano)
		goto(iniciox, inicioy+tamano)
		goto(iniciox, inicioy)
		
	elif valor1=="TRIANGULO":
		penup()
		inicioy=damevalor(valor3)
		iniciox=damevalor(valor4)
		tamano=damevalor(valor2)
		goto(iniciox, inicioy)
		pendown()
		goto(tamano+iniciox, inicioy)
		goto(iniciox+(tamano/2), tamano+inicioy)
		goto(iniciox, inicioy)
		
	elif valor1=="MUEVE":
		muevey=damevalor(valor2)
		muevex=damevalor(valor3)
		goto(muevex, muevey)
		
		
		
	i = i+1
		
