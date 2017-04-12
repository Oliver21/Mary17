# -*- coding: utf-8 -*-
#MARY17
#Oliver Alejandro Martinez Quiroz A01280416
#Diego Alejandro Mayorga Morales A00813211
import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
from collections import Iterable
from Cuadruplo import *
from Cubo import *
import sys

precedence = (
	('right', 'IGUAL'),
	('left', 'AND', 'OR'),
	('left', 'LT', 'GT', 'LE', 'GE', 'SAME', 'DIF'),
	('left', 'SUMA', 'RESTA'),	
	('left', 'MULT', 'DIV'),
	('left', 'LBRACKET', 'RBRACKET'),
	('left', 'LPARENT', 'RPARENT'),
	('left', 'LKEY', 'RKEY')	
)

#definimos una estructura de datos tipo pila que nos servira para manejar los tipos y los identificadores de las variables
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
     def imprime(self):
	 for i, val in enumerate(self.items):
	 	print val,


#La clase Funcion funciona como template para la entrada de variables
class Funcion:
	def __init__(self, type, identifier):
		self.type = type
		self.numParam = None
		self.numLocal = None
		self.identifier = identifier
		self.Cont = None
		self.FunctionTable = None
		self.LocalTable = None

#La clase Variable funciona como template para la entrada de variables
class Variable:
	def __init__(self, type, identifier, memory, size):
		self.type = type
		self.memory = memory
		self.identifier = identifier
		self.size = size

#definimos la clase para la tabla por enviroment
#Nos servira para simular el creado de tablas por scope
class Env:
	#Este atributo es un objeto de la misma clase Env
	#Representa el scope anterior 
	prev = None
	def __init__(self,ant):
		self.prev = ant
		self.dict = {}

#funcion que nos sirve para insertar un nuevo simbolo a la tabla
	def put(self, identifier, content):
			self.dict[identifier] = content

#funcion que itera por las tablas para encontrar un simbolo
#empieza por el scope actual y regresa una tabla o None si no encuentra la variable

	def get(self, identifier):
		e = self
		while e != None:
			for k in e.dict:
				if identifier == k:
	  				return e.dict[k]
	  				break
			e = e.prev
		return None

#definicion de la tabla de funciones
global_functions_table = {}
class FunctionTable:
	def __init__(self):
		self.dict = {}

#funcion que nos sirve para insertar una nueva entrada a la tabla
	def put(self, identifier, content):
			self.dict[identifier] = content

#funcion que itera por las tablas para encontrar un simbolo
#regresa una funcion o None si no encuentra la funcion
	def get(self, identifier):
		for k in self.dict:
			if identifier == k:
  				return self.dict[k]
  				break
		return None

#definicion de funciones globales que necesitamos acceder en cualquier momento de la ejecuccion
top = None
saved = None
decFunciones = False
TablaFunciones = FunctionTable()
FuncToBuild = None
EnvParam = None


class MemManager:
	def __init__(self):
		self.memory = {"INT":{}, "FLOAT": {}, "STRING":{}, "CHAR":{}, "BOOL":{}}

	def save(self,type,value):
		cont = 0
		for key, val in self.memory[type].iteritems():
			if not key == cont:
				break
			cont = cont + 1
		self.memory[type][cont] = value
		return cont

	def find(self,type,position):
		if position in self.memory[type]:
			return self.memory[type][position]
		else:
			return None

MemManagerPrueba = MemManager()	
print MemManagerPrueba.save("INT",1)
print MemManagerPrueba.save("INT",1)
print MemManagerPrueba.save("INT",2)
print MemManagerPrueba.save("INT",3)

print MemManagerPrueba.memory




#Inicializamos muestros administradores de memoria
MemManagerGlobal = MemManager()
MemManagerLocal = MemManager()

#########DEFINIMOS UNA LISTA VACIA PARA CUADRUPLOS#########################
cuadru=[]
POper=Stack()
PilaO=Stack()
PTypes=Stack()
temporal = 1
#Prueba de cuadruplos
#x = Cuadruplo (1,3,2,5)
#print x.pos1, x.pos2, x.pos3, x.pos4

####################CONTENIDO DE UN PROGRAMA###################################
def p_program(p):
	'''program : PROGRAM  cuadrupro ID initTop DOSPUNTOS p2'''
	#p[0] = program(p[4], "program")
	#print "programa"

def p_initTop(p):
	'''initTop : empty'''
	#top es la tabla de variables del scope actual
	global top
	top = Env(None)


def p_p2(p):
	'''p2 : p3
	| p4
	| p5'''
	
def p_p3(p):
	'''p3 : declaracion p3
	|  p4'''
	
def p_p4(p):
	'''p4 : function p4
	| p5'''
	
def p_p5(p):
	'''p5 : cuadrupro2 bloque'''	
	
def p_cuadrupro(p):
	'''cuadrupro : empty'''
	x = Cuadruplo(pos1 = "GoTo")
	cuadru.append(x)
	#print x.pos1, x.pos2, x.pos3, x.pos4
	
def p_cuadrupro2(p):
	'''cuadrupro2 : empty'''
	cuadru[0].pos4 = len(cuadru)

########################CONTENIDO DE UN BLOQUE######################################
def p_bloque(p):

	'''bloque : LKEY  iniEnv b3 b4 b5'''

def p_iniEnv(p):
	'''iniEnv : empty'''
	global decFunciones
	global saved
	global top
	saved = top
	if not decFunciones:
		top = Env(top)
	else:
		top = Env(None)

	#print "bloque"


def p_b3(p):
	'''b3 : declaracion b3
	| empty'''

def p_b4(p):
	'''b4 : estatuto b4
	| empty'''

def p_b5(p):
	'''b5 : RKEY'''
	global top
	global saved
	global decFunciones
	global FuncToBuild
	if(not decFunciones):
		top = saved
	else:
		FuncToBuild.LocalTable = top
		top = saved
		
		
############################CONTENIDO DE UNA EXPRESION################################
def p_expresion(p):
	'''expresion : expresion2 expre'''
	
def p_expre(p):
	'''expre : expre2
	| empty'''
	
def p_expre2(p):
	'''expre2 : AND tagmetelog expresion tagsacalog
	| OR tagmetelog expresion tagsacalog'''
	
def p_tagmetelog(p):
	'''tagmetelog : empty'''
	POper.push(p[-1])
	
def p_tagsacalog(p):
	'''tagsacalog : empty'''
	if POper.isEmpty():
		pass
	else:
		while POper.peek()=="&&" or POper.peek()=="||" or POper.peek()==">" or POper.peek()=="<" or POper.peek()=="<=" or POper.peek()==">=" or POper.peek()=="==" or POper.peek()=="!=" or POper.peek() == "+" or POper.peek() == "-" or POper.peek() == "*" or POper.peek() == "/":
			operandoDerecho = PilaO.pop()
			tipoDerecho = PTypes.pop()
			operandoIzquierdo = PilaO.pop()
			tipoIzquierdo = PTypes.pop()
			operador = POper.pop()
			resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
			if resultType == "ERROR":
				print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operandoIzquierdo, operador, tipoDerecho, operandoDerecho
				sys.exit(0)
			else:
				global temporal
				result = "t" + str(temporal)
				temporal = temporal + 1
				quad = Cuadruplo(operador, operandoIzquierdo, operandoDerecho, result)
				cuadru.append(quad)
				PilaO.push(result)
				PTypes.push(resultType)
				
				
			#PilaO.push(POper.pop())
			if POper.isEmpty():
				break

	
###########################CONTENIDO DE UNA EXPRESION2#################################
def p_expresion2(p):
	'''expresion2 : exp e2 '''
	#print "expresion2"


def p_e2(p):
	'''e2 : e3 
	| empty'''

def p_e3(p):
	'''e3 : GT tagrel exp tagsacrel
	| LT tagrel exp tagsacrel
	| LE tagrel exp tagsacrel
	| GE tagrel exp tagsacrel
	| DIF tagrel exp tagsacrel
	| SAME tagrel exp tagsacrel'''
	
def p_tagrel(p):
	'''tagrel : empty'''
	POper.push(p[-1])
	
	
def p_tagsacrel(p):
	'''tagsacrel : empty'''
	if POper.isEmpty():
		pass
	else:
		while POper.peek()==">" or POper.peek()=="<" or POper.peek()=="<=" or POper.peek()==">=" or POper.peek()=="==" or POper.peek()=="!=" or POper.peek() == "+" or POper.peek() == "-" or POper.peek() == "*" or POper.peek() == "/":
			operandoDerecho = PilaO.pop()
			tipoDerecho = PTypes.pop()
			operandoIzquierdo = PilaO.pop()
			tipoIzquierdo = PTypes.pop()
			operador = POper.pop()
			resultType = validacion(tipoDerecho, tipoIzquierdo, operador)
			if resultType == "ERROR":
				print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operandoIzquierdo, operador, tipoDerecho, operandoDerecho
				sys.exit(0)
			else:
				global temporal
				result = "t" + str(temporal)
				temporal = temporal + 1
				quad = Cuadruplo(operador, operandoIzquierdo, operandoDerecho, result)
				cuadru.append(quad)
				PilaO.push(result)
				PTypes.push(resultType)
				
				
			#PilaO.push(POper.pop())
			if POper.isEmpty():
				break

##################EXP###################################
def p_exp(p):
	'''exp : termino tagsacops exp2'''
	#print "exp"

def p_exp2(p):
	'''exp2 : SUMA  tagop exp 
	| RESTA tagop exp
	| empty'''
		
def p_tagop(p):
	'''tagop : empty'''
	POper.push(p[-1])
	#print "Se agrego a la pila sum"
	
def p_tagsacops(p):
	'''tagsacops : empty'''
	if POper.isEmpty():
		pass
	else:
		while POper.peek() == "+" or POper.peek() == "-" or POper.peek() == "*" or POper.peek() == "/":
			operandoDerecho = PilaO.pop()
			tipoDerecho = PTypes.pop()
			operandoIzquierdo = PilaO.pop()
			tipoIzquierdo = PTypes.pop()
			operador = POper.pop()
			resultType = validacion(tipoDerecho, tipoIzquierdo, operador)
			if resultType == "ERROR":
				print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operandoIzquierdo, operador, tipoDerecho, operandoDerecho
				sys.exit(0)
			else:
				global temporal
				result = "t" + str(temporal)
				temporal = temporal + 1
				quad = Cuadruplo(operador, operandoIzquierdo, operandoDerecho, result)
				cuadru.append(quad)
				PilaO.push(result)
				PTypes.push(resultType)
				
				
			#PilaO.push(POper.pop())
			if POper.isEmpty():
				break
		
	
		

####################DECLARACION DE VARIABLES#############################
#def p_declaracion(p):
#	'''declaracion : tipo ID PUNTOCOMA'''
	#AddGlobalVariable(p[1],p[2])
#	global top
#	varContent  = {'type':p[1]}
#	top.put(p[2],varContent)
#	print "declaracion"
	

def p_declaracion(p):
	'''declaracion : tipo ID savevar decla1'''
	#print "Declaracion"
def p_savevar(p):
	'''savevar : empty'''
	global top
	global MemManagerGlobal
	global MemManagerLocal
	if top.prev == None and not decFunciones:
		pos = MemManagerGlobal.save(p[-2],p[-1])
		var = Variable(p[-2],p[-1],pos,1)
		print MemManagerGlobal.memory
	elif not decFunciones:
		pos = MemManagerLocal.save(p[-2],p[-1])
		var = Variable(p[-2],p[-1],pos,1)
		print MemManagerLocal.memory
	else:
		pos = MemManagerLocal.save(p[-2],p[-1])
		var = Variable(p[-2],p[-1],pos,1)
		print MemManagerLocal.memory
	print pos
	top.put(p[-1],var)

def p_decla1(p):
	'''decla1 : declafinal
	| LBRACKET exp decla2'''
	
def p_decla2(p):
	'''decla2 : RBRACKET declafinal
	| COMA exp decla2'''
	#print "declaracion arreglo"
	
def p_declafinal(p):
	'''declafinal : PUNTOCOMA'''


####################DECLARACION DE ARREGLO VARIABLES#############################
#def p_declaracionarr(p):
#	'''declaracionarr : tipo ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET PUNTOCOMA'''
#	print "declaracion arreglo"
	
######################TIPO DE VARIABLES######################################
def p_tipo(p):
	'''tipo : INT
	| FLOAT
	| CHAR
	| STRING
	| BOOL'''
	p[0] = p[1]
	#print "tipo"

##################ASIGNACION A VARIABLES###################################
#def p_asignacion(p):
#	'''asignacion : ID IGUAL expresion PUNTOCOMA'''
#	 "asignacion"

def p_asignacion(p):
	'''asignacion : ID asig2'''
	#print "asignacion"
	
def p_asig2(p):
	'''asig2 : LBRACKET exp asig3
	| asigfinal'''

def p_asig3(p):
	'''asig3 : COMA exp asig3
	| RBRACKET asigfinal'''
	#print "asignacion arreglo"

def p_asigfinal(p):
	'''asigfinal : IGUAL expresion PUNTOCOMA'''
	#POper.push(p[1])

	
##################ASIGNACION A ARREGLOS DE VARIABLES###################################
#def p_asignacionarr(p):
#	'''asignacionarr : ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET IGUAL expresion PUNTOCOMA'''
#	print "asignacion a arreglo"
#########################ESCRITURA####################################
def p_print(p):
	'''print : PRINT LPARENT pr2'''
	#print "esritura"

def p_pr2(p):
	'''pr2 : expresion pr3
	| CADENA pr3'''
	#print "es2"

def p_pr3(p):
	'''pr3 : pr2
	| RPARENT PUNTOCOMA'''
######################CONDICION###############################
def p_condicion(p):	
	'''condicion : IF LKEY expresion RKEY bloque c2'''
	#print "condicion"

def p_c2(p):
	'''c2 : ELSE bloque PUNTOCOMA
	| PUNTOCOMA'''
	#print "c2"

########################TERMINO#################################
def p_termino(p):
	'''termino : factor tagsacopm te2'''
	#print "termino"

def p_te2(p):
	'''te2 : MULT tagm termino 
	| DIV tagm termino
	| empty'''
	
	
	
def p_tagm(p):
	'''tagm : empty'''
	POper.push(p[-1])
		#print "Se agrego a la pila mult"
		
def p_tagsacopm(p):
	'''tagsacopm : empty'''
	if POper.isEmpty():
		pass
	else:
		while POper.peek() == "*" or POper.peek() == "/":
			operandoDerecho = PilaO.pop()
			tipoDerecho = PTypes.pop()
			operandoIzquierdo = PilaO.pop()
			tipoIzquierdo = PTypes.pop()
			operador = POper.pop()
			resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
			if resultType == "ERROR":
				print "INCOMPATIBILIDAD DE TIPOS"
			else:	
				global temporal
				result = "t" + str(temporal)
				temporal = temporal + 1
				quad = Cuadruplo(operador, operandoIzquierdo, operandoDerecho, result)
				cuadru.append(quad)
				PilaO.push(result)
				PTypes.push(resultType)
				
				
			#PilaO.push(POper.pop())
			if POper.isEmpty():
				break
######################FACTOR####################################
def p_factor(p):
	'''factor : LPARENT tagfondofalso expresion RPARENT tagsacafondo
	| f2
	| f3
	| f6
	| f7'''
	#print "factor"
	if p[1] == '{':
		p[0] = p[2]
	else:
		p[0] = p[1]

#llamar a una constante
def p_f2(p):
	'''f2 : varcte'''
	#p[0] = p[1]
	#print p[1]

#llamar a un id
def p_f3(p):
	'''f3 : ID'''
	PilaO.push(p[1])
	print p[1]
	PTypes.push(top.get(p[1]).type)
	#print "SE AGREGO ID AL VECTOR POLACO"
	
def p_tagfondofalso(p):
	'''tagfondofalso : empty'''
	POper.push(p[-1])
	
def p_tagsacafondo(p):
	'''tagsacafondo : empty'''
	while POper.peek() == "+" or POper.peek() == "-" or POper.peek() == "*" or POper.peek() == "/":
		PilaO.push(POper.pop())
		if POper.isEmpty():
			break
	POper.pop()
	
#def p_f4(p):
#	'''f4 : empty'''


#def p_f4(p):
#	'''f4 : LBRACKET exp f5
#	| empty'''
	
#def p_f5(p):
#	'''f5 : COMA exp f5
#	| RBRACKET'''

#llamar a un arreglo
def p_f7(p):
	'''f7 : ID LBRACKET exp f8'''
	print "OPERACION CON DIMENSIONES"
	
def p_f8(p):
	'''f8 : COMA exp f8
	| RBRACKET'''

#llamar a una funcion
def p_f6(p):
	'''f6 : llamafuncion'''
	print "OPERACION CON FUNCIONES"

######################CONTENIDO DE UN ESTATUTO##################################

def p_estatuto(p):
	'''estatuto : asignacion
	| print
	| condicion
	| ciclowhile
	| ciclodowhile
	| ciclofor
	| read
	| comentario
	| cuadrado
	| triangulo
	| casa
	| rectangulo
	| cubo
	| trapecio
	| estrella
	| mueve
	| levanta
	| apoya
	| dimension
	| llamafuncion
	| if'''
#	| potencia
#	| raiz
	#print "estatuto"

#####################COMENTARIO######################################

def p_comentario(p):
	'''comentario : COMENTARIO'''
	#print "Este es un comentario"

######################VARIABLE CONSTANTE#####################################

def p_varcte(p):
	'''varcte : ENTERO tagint
	| FLOTANTE tagfloat
	| CADENA tagcad
	| CARACTER tagcar'''
	
def p_tagint(p):
	'''tagint : empty'''
	PilaO.push(p[-1])
	PTypes.push("INT")
	#print "SE AGREGO CONSTANTE A LA PILA DE OPERANDOS"
	
def p_tagfloat(p):
	'''tagfloat : empty'''
	PilaO.push(p[-1])
	PTypes.push("FLOAT")
	#print "SE AGREGO CONSTANTE A LA PILA DE OPERANDOS"
	
def p_tagcad(p):
	'''tagcad : empty'''
	PilaO.push(p[-1])
	PTypes.push("STRING")
	#print "SE AGREGO CONSTANTE A LA PILA DE OPERANDOS"
	
def p_tagcar(p):
	'''tagcar : empty'''
	PilaO.push(p[-1])
	PTypes.push("CHAR")
	#print "SE AGREGO CONSTANTE A LA PILA DE OPERANDOS"


#####################CICLOS Y OTRAS FUNCIONES####################################
def p_ciclowhile(p):
	'''ciclowhile : WHILE LPARENT expresion RPARENT bloque'''
	#print "ciclo While"

def p_ciclodowhile(p):
	'''ciclodowhile : DO bloque WHILE LPARENT expresion RPARENT PUNTOCOMA'''
	#print "ciclo do while"

def p_read(p):
	'''read : ID IGUAL READ LPARENT RPARENT PUNTOCOMA'''
	#print "lectura"

def p_ciclofor(p):
	'''ciclofor : FOR LPARENT asignacion expresion asignacion RPARENT bloque'''
	#print "ciclo for"
	
def p_if(p):
	'''if : IF LPARENT expresion RPARENT bloque if2'''
	#print "Ciclo If"

def p_if2(p):
	'''if2 : empty
	| ELSE bloque'''

#def p_potencia(p):
#	'''potencia : POW LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
#	print "potencia"

#def p_raiz(p):
#	'''raiz : SQRT LPARENT varcte RPARENT PUNTOCOMA'''
#	print "raiz"
###################ERROR#####################################

def p_error(p):
	print "error de sintaxis", p
	print "error en la linea" +str(p)
	
################FUNCIONES DIIBUJAR###############################


def p_cuadrado(p):
	'''cuadrado : CUADRADO LPARENT exp RPARENT PUNTOCOMA'''
	#print "Dibuja cuadrado"
	
def p_triangulo(p):
	'''triangulo : TRIANGULO LPARENT exp RPARENT PUNTOCOMA'''
	#print "Dibuja triangulo"
	
def p_rectangulo(p):
	'''rectangulo : RECTANGULO LPARENT exp COMA exp RPARENT PUNTOCOMA'''
	#print "Dibuja rectangulo"

def p_casa(p):
	'''casa : CASA LPARENT exp COMA exp RPARENT PUNTOCOMA'''
	#print "Dibuja casa"

def p_estrella(p):
	'''estrella : ESTRELLA LPARENT exp RPARENT PUNTOCOMA'''
	#print "Dibuja estrella"

def p_cubo(p):
	'''cubo : CUBO LPARENT exp RPARENT PUNTOCOMA'''
	#print "Dibuja cubo"

def p_mueve(p):
	'''mueve : MUEVE LPARENT exp COMA exp RPARENT PUNTOCOMA'''
	#print "Mueve"
	
def p_levanta(p):
	'''levanta : LEVANTA LPARENT RPARENT PUNTOCOMA'''
		#print "Levanta lapiz"
	
def p_apoya(p):
	'''apoya : APOYA LPARENT RPARENT PUNTOCOMA'''
	#print "Apoya lapiz"
	
def p_trapecio(p):
	'''trapecio : TRAPECIO LPARENT exp COMA exp RPARENT PUNTOCOMA'''
	#print "Dibuja trapecio"
	
def p_dimension(p):
	'''dimension : DIMENSION LPARENT exp RPARENT PUNTOCOMA'''
	#print "Asigna dimension"

##########################DECLARA UNA FUNCION##########################
def p_function(p):
	'''function : tipo ID buildFunc LPARENT funct11
	| VOID ID buildFunc LPARENT funct11'''
	#print "Declara una funcion"

def p_buildFunc(p):
	'''buildFunc : empty''' 
	global FuncToBuild
	FuncToBuild = Funcion(p[-2], p[-1])
	print FuncToBuild.identifier

	
def p_funct11(p):
	'''funct11 : function4'''

def p_funct111(p):
	'''funct11 : initParamTable funct2'''

def p_initParamTable(p):
	'''initParamTable : empty'''
	global EnvParam
	EnvParam = Env(None)
	
def p_funct2(p):
	'''funct2 : tipo ID initParams funct3'''

def p_initParams(p):
	'''initParams : empty'''
	global EnvParam
	var = Variable(p[-2],p[-1],0,0)
	EnvParam.put(p[-1],var)
	
def p_funtion3(p):
	'''funct3 : COMA funct2'''


def p_function31(p):
	'''funct3 : function4'''

	
def p_function4(p):
	'''function4 : RPARENT noinitFunc bloque initFunc'''

def p_noinitFunc(p):
	'''noinitFunc : empty'''
	global decFunciones
	decFunciones = True
	FuncToBuild.FunctionTable = EnvParam

def p_initFunc(p):
	'''initFunc : empty'''
	global decFunciones
	decFunciones = False
	
##################LLAMA UNA FUNCION###############################
def p_llamafuncion(p):
	'''llamafuncion : ID LPARENT llamaf11'''
	#print "Llama a una funcion"
	
def p_llamaf11(p):
	'''llamaf11 : llamaf2
	| llamaf4'''
	
def p_llamaf2(p):
	'''llamaf2 : exp llamaf3'''

def p_llamaf3(p):
	'''llamaf3 : COMA llamaf2
	| llamaf4'''
	
def p_llamaf4(p):
	'''llamaf4 : RPARENT'''
		
##################EMPTY########################################
def p_empty(p):
	'''empty :'''
	pass

###############BUSCAR ARCHIVO DE PRUEBAS###################################
def buscarPrograma(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has seleccionado \"%s\" \n" %files[int(numArchivo)-1]
	return files[int(numArchivo)-1]	

# directorio = '../tests/'
# archivo = buscarPrograma(directorio)
# test = directorio+archivo
# test = '../tests/' + buscarPrograma(directorio)

fp = codecs.open('../tests/' + buscarPrograma('../tests/'),"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
parser.parse(cadena)



print MemManagerGlobal.memory
print MemManagerLocal.memory
########CUADRUPLOS#################################################################

#print "---------------------------------------------------------------------"
#print "--------------------CUADRUPLOS GENERADOS--------------------"
#for i in cuadru:
	#print i.pos1, i.pos2, i.pos3, i.pos4
#print cuadru[0].pos1, cuadru[0].pos2, cuadru[0].pos3, cuadru[0].pos4
#print "-------------PilaO (Pila de operandos)----------------------"
#PilaO.imprime()
#print
#print "-------------PTypes (Pila de tipos)-------------------------"
#PTypes.imprime()
#print
#print "-------------POper (Pila de operadores)----------------------"
#POper.imprime()
####################################################################################


