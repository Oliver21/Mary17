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


#Funcion que convierte listas anidadas en un
def dimensiona(lis):
     for i in lis:
         if isinstance(i, Iterable) and not isinstance(i, basestring) and not isinstance(i, tuple):
             for x in dimensiona(i):
                 yield x
         else:        
             yield i



#definimos la clase para la tabla por enviroment
#Nos servira para simular el creado de tablas por scope
class Variable:
	def __init__(self, type, identifier, memory, size):
		self.type = type
		self.memory = memory
		self.identifier = identifier
		self.size = size

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

#definicion de la tabla global de variables
top = Env(None)
saved = Env(None)
decFunciones = False

#definicion de variables globales y espacios disponibles
global_int = {}
global_int_count = 0
global_float = {}
global_float_count = 200
global_bool = {}
global_bool_count = 400 
global_string = {}
global_string_count = 600
global_char = {}
global_char_count = 800


#definicion de variables locales y espacios disponibles
def local():
	local_int = {}
	local_int_count = 1000
	local_float = {}
	local_float_count = 1200
	local_bool = {}
	local_bool_count = 1400 
	local_string = {}
	local_string_count = 1600
	local_char = {}
	local_char_count = 1800


#Funcion que busca una variable decladarada global
def SearchGlobalVariable(identifier):
	global global_int
	if identifier in global_int:
		return True
	elif identifier in global_float:
		return True
	elif identifier in global_bool:
		return True
	elif identifier in global_string:
		return True
	elif identifier in global_char:
		return True
	else :
		return False

#Funcion que busca una variable decladarada local
def SearchLocalVariable(identifier):
	if identifier in local_int:
		return True
	elif identifier in local_float:
		return True
	elif identifier in local_bool:
		return True
	elif identifier in local_string:
		return True
	elif identifier in local_char:
		return True
	else :
		return False


#Funcion que agrega una variable local si su nombre no esta asignado aun
def AddGlobalVariable(type,identifier):
	#Se necesita especificar que las variables que usare son las que declare globalmente
	global global_float_count
	global global_int_count
	global global_int
	global global_float
	global global_bool
	global global_bool_count
	global global_string_count
	global global_string
	global global_char
	global global_char_count
	#print(type + " " + identifier)
	#itero a lo largo de la pila para agregar todas las variables que pueda haber en ella
	if SearchGlobalVariable(identifier):
		print("error: la variable ya ha sido declarada")
	else:
		#Se agrega la variable a su diccionario dependiendo de su tipo
		variable = {}
		if type == 'INT':
			variable['position'] = global_int_count
			global_int_count = global_int_count + 1
			global_int[identifier] = variable.copy()
		elif type == 'FLOAT':
			variable['position'] = global_float_count
			global_float_count = global_float_count + 1
			global_float[identifier] = variable.copy()
		elif type == 'STRING':
			variable['position'] = global_string_count
			global_string_count = global_string_count + 1
			global_string[identifier] = variable.copy()
		elif type == 'CHAR':
			variable['position'] = global_char_count
			global_char_count = global_char_count + 1
			global_char[identifier] = variable.copy()
		elif type == 'BOOL':
			variable['position'] = global_bool_count
			global_bool_count = global_bool_count + 1
			global_bool[identifier] = variable.copy()
		else:
			print("error: tipo de variable incorrecto");


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
	if(not decFunciones):
		saved = top
		top = Env(top)
		print "{"
		print "Entra"
	print "bloque"


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
	if(not decFunciones):
		top = saved
		print "}"
		
		
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
	'''declaracion : tipo ID decla1'''
	var = Variable(p[1],p[2],0,0)
	global top
	global decFunciones
	if not decFunciones:  
		top.put(p[2],var)
	#print "Declaracion"


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
	global decFunciones
	global top
	if not decFunciones:
		print(p[1])
		#print(top.get(p[1]).identifier + ":" + top.get(p[1]).type)
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
	'''function : tipo ID LPARENT funct11
	| VOID ID LPARENT funct11'''
	if p[4] != None:
		global_functions_table[p[2]] = {'type':p[1],'parameters': list(dimensiona(p[4]))}
	else:
		global_functions_table[p[2]] = {'type':p[1],'parameters': [] }
	#print "Declara una funcion"
	
def p_funct11(p):
	'''funct11 : function4'''

def p_funct111(p):
	'''funct11 : funct2'''
	p[0] = p[1]
	
def p_funct2(p):
	'''funct2 : tipo ID funct3'''
	p[0] = []
	p[0].append((p[1],p[2]))
	if p[3] != None:
		p[0].append(p[3])
	
def p_funtion3(p):
	'''funct3 : COMA funct2'''
	p[0] = p[2]


def p_function31(p):
	'''funct3 : function4'''
	p[0] = p[1]

	
def p_function4(p):
	'''function4 : RPARENT noinitFunc bloque initFunc'''

def p_noinitFunc(p):
	'''noinitFunc : empty'''
	global decFunciones
	decFunciones = True

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
result = parser.parse(cadena)

print global_functions_table

print result


#analizador=lex.lex()
#analizador.input(cadena)
########CUADRUPLOS#################################################################	
print "---------------------------------------------------------------------"
print "--------------------CUADRUPLOS GENERADOS--------------------"
for i in cuadru:
	print i.pos1, i.pos2, i.pos3, i.pos4
#print cuadru[0].pos1, cuadru[0].pos2, cuadru[0].pos3, cuadru[0].pos4
print "-------------PilaO (Pila de operandos)----------------------"
PilaO.imprime()
print
print "-------------PTypes (Pila de tipos)-------------------------"
PTypes.imprime()
print
print "-------------POper (Pila de operadores)----------------------"
POper.imprime()
####################################################################################


