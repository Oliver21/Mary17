#!/usr/bin/python
from analizadorSintactico import *


def damevalor(valor):
	revisado=str(valor)
	if revisado[0:4]=="mem-":
		revisado=revisado[4:]
		revisado=UnivMemManager.find(int(revisado))
		return revisado
	elif revisado[0]=="\"":
		return str(revisado[1:len(revisado)-1])
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
for i in cuadru:
	valor1=i.pos1
	valor2=i.pos2
	valor3=i.pos3
	valor4=i.pos4
	
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
	elif valor1=="Goto":
		pass
		#print "Aqui hay una !="
	elif valor1=="Goto":
		pass
		#print "Aqui hay una goto"
	elif valor1=="GoToT":
		pass
		#print "Aqui hay una gotot"
	elif valor1=="GoToF":
		pass
		#print "Aqui hay una gotof"
	elif valor1=="GoTo":
		pass
		#print "Aqui hay una goto"
	elif valor1=="PRINT":
		#print "Aqui hay una print"
		print damevalor(valor4)
	elif valor1=="READ":
		entrada= raw_input()
		print (entrada)
		#print "Aqui hay una read"
		
