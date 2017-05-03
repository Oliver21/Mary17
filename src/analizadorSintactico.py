# -*- coding: utf-8 -*
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

#definicion de funciones globales que necesitamos acceder en cualquier momento de la ejecuccion
top = None
saved = None
#Localfunc = None
decFunciones = False
TablaFunciones = None
FuncToBuild = None
EnvParam = None
DecFuncIndividual = False
LlegoReturn = False
esdimen=False

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


#definimos una clase que nos servira como campo para la descripcion de la dimencion
class Dimension:
	def __init__(self):
		self.nextDim = None
		self.antDim = None
		self.LsDIM = None
		self.LiDIM = None
		self.mDIM = None


#La clase Funcion funciona como template para la entrada de variables
class Funcion:
	def __init__(self, type, identifier):
		self.type = type
		self.numParam = None
		self.identifier = identifier
		self.Cont = None
		self.ParamTable = []
		self.LocalVars = []
		self.LocalTable = None
		self.ReturnValue = None
	def getParamType(self,index):
		if index < len(self.ParamTable):
			return self.ParamTable[index]
		else:
			return None

	def getVarMemory(self,index):
		if index < len(self.LocalVars):
			#print self.LocalVars[index].identifier
			return self.LocalVars[index].memory
		else:
			return None


#La clase Variable funciona como template para la entrada de variables
class Variable:
	def __init__(self, type, identifier, memory, size):
		self.type = type
		self.memory = memory
		self.identifier = identifier
		self.size = size
		self.Auxil = None

	#Metodo que regresa a la primera posicion de las dimensiones encadenadas	
	def goHeadDim(self):
		while not self.size == None:
			#print self.size.LsDIM
			headSize = self.size
			#self.size.antDim.nextDim = self.size
			self.size = self.size.antDim
		#print "ESTA afuera DEL WHILE"
		#print self.size.LsDIM
		self.size = headSize

	def goDimForward(self):
		if self.size.nextDim == None or self.size == None:
			return False
		else:
			#self.size.nextDim.antDim = self.size
			self.size = self.size.nextDim
			return True

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
		if not identifier in self.dict: 
			self.dict[identifier] = content
			return True
		else:
			return False

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
		print "La variable " + identifier + " no ha sido declarada"
		sys.exit()
		return None
#funcion que nos permite liberar la memoria de las variables para su reuso
	def release(self):
		global UnivMemManager
		for i in self.dict:
			UnivMemManager.release(self.dict[i].memory)
			if not self.dict[i].size == None:
				temp = self.dict[i].Auxil 
				while not temp == 0:
					 UnivMemManager.release(int(self.dict[i].memory) + temp)
					 temp = temp - 1
			else:
				UnivMemManager.release(self.dict[i].memory)

#Funcion para ver las variables hasta el momento guardadas.
	def showVars(self):
		e = self
		while e != None:
			for k in e.dict:
	  				print e.dict[k].identifier
			e = e.prev
	def showMemContent(self):
		global UnivMemManager
		e = self
		while e != None:
			for k in e.dict:
	  				print UnivMemManager.find(e.dict[k].memory)
			e = e.prev

#definicion de la tabla de funciones
global_functions_table = {}
class FunctionTable:
	def __init__(self):
		self.dict = {}

	def put(self,name,function):
		if not name in self.dict:
			self.dict[name] = function
			return True
		else:
			return False

	def get(self,name):
		if name in self.dict:
			return self.dict[name]
		else:
			return None

#funcion que nos sirve para insertar una nueva entrada a la tabla
	#def put(self, identifier, content):
			#self.dict[identifier] = content

#funcion que itera por las tablas para encontrar un simbolo
#regresa una funcion o None si no encuentra la funcion
	def get(self, identifier):
		for k in self.dict:
			if identifier == k:
  				return self.dict[k]
  				break
		return None


class MemManager:
	def __init__(self):
		self.memory = {}

	def saveTEMP(self, value):
		cont = 20000
		for key, val in self.memory.iteritems():
			if not cont in self.memory:
				break
			elif self.memory[cont] == None:
				break
			cont = cont + 1
		self.memory[cont] = value
		return str(cont)

	def saveReturnValue(self,type,value):
		if type == "INT":
			cont = 0
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "FLOAT":
			cont = 2000
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "CHAR":
			cont = 4000
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "STRING":
			cont = 6000
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "BOOL":
			cont = 8000
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value
		return str(cont)


	def saveDimensions(self, type, value, size):
		global decFunciones
		if decFunciones:
			aux = 10000
		else:
			aux = 0
		if type == "INT":
			cont = 0 + aux

		elif type == "FLOAT":
			cont = 2000 + aux

		elif type == "CHAR":
			cont = 4000 + aux

		elif type == "STRING":
			cont = 6000 + aux

		elif type == "BOOL":
			cont = 8000 + aux
		else:
			return None

		for key, val in self.memory.iteritems():
				if (not cont in self.memory) or self.memory[cont] == None:
					vacioHastaAhora = True
					newCont = 0
					while vacioHastaAhora and not newCont == size:
						if (not (cont + newCont) in self.memory) or self.memory[cont + newCont] == None:		
							vacioHastaAhora = True
						else:
							vacioHastaAhora = False
						newCont = newCont + 1;
					if vacioHastaAhora :
						newCont = 0
						while not newCont == size:
							self.memory[cont + newCont] = value
							newCont = newCont + 1
						break
				cont = cont + 1
		return str(cont)

	def save(self, type, value):
		global decFunciones
		if decFunciones:
			aux = 10000
		else:
			aux = 0
		if type == "INT":
			cont = 0 + aux
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "FLOAT":
			cont = 2000 + aux
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "CHAR":
			cont = 4000 + aux
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "STRING":
			cont = 6000 + aux
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value

		if type == "BOOL":
			cont = 8000 + aux
			for key, val in self.memory.iteritems():
				if not cont in self.memory:
					break
				elif self.memory[cont] == None:
					break
				cont = cont + 1
			self.memory[cont] = value
		return str(cont)


	def find(self,position):
		if int(position) in self.memory:
			return self.memory[int(position)]
		else:
			return None

	def release(self,position):
		if int(position) in self.memory:
			self.memory[int(position)] = None
			return True
		else:
			return False
			
	def asigna(self,position, valor):
		self.memory[int(position)]= valor

		

#Inicializamos muestro administrador de memorias
UnivMemManager = MemManager()

#########DEFINIMOS UNA LISTA VACIA PARA CUADRUPLOS#########################
cuadru=[]
POper=Stack()
PilaO=Stack()
PTypes=Stack()
PSaltos=Stack()
PilaDimensionadas=Stack()
PilaDim=Stack()
PilaEspera=Stack()
PilaDi=Stack()

temporal = 1
nombredelafuncion=""
contadorParametro=0

####################CONTENIDO DE UN PROGRAMA###################################
def p_program(p):
	'''program : PROGRAM  cuadrupro ID initTop DOSPUNTOS p2'''

def p_initTop(p):
	'''initTop : empty'''
	#top es la tabla de variables del scope actual
	global top
	global TablaFunciones 
	TablaFunciones = FunctionTable()
	top = Env(None)

def p_p2(p):
	'''p2 : p3
	| initFunctions p4
	| p5'''

def p_p3(p):
	'''p3 : declaracion p3
	| initFunctions p4'''

def p_initFunctions(p):
	'''initFunctions : empty'''
	global saved
	global top
	saved = top

def p_p4(p):
	'''p4 : function p4
	| p5'''

def p_p5(p):
	'''p5 : cuadrupro2 bloque delMem'''	

#generamos el cuadruplo GoTo que nos llevara al main para iniciar la ejecucion	
def p_cuadrupro(p):
	'''cuadrupro : empty'''
	x = Cuadruplo(pos1 = "GoTo")
	cuadru.append(x)

#asignamos la posicion en donde comienza el main (ejecucion del programa)	
def p_cuadrupro2(p):
	'''cuadrupro2 : empty'''
	global saved
	global top
	top = saved
	cuadru[0].pos4 = len(cuadru)

def p_delMem(p):
	'''delMem : empty'''
	global top
	top.release()

########################CONTENIDO DE UN BLOQUE######################################
def p_bloque(p):
	'''bloque : iniEnv LKEY b3 b4 b5'''

def p_iniEnv(p):
	'''iniEnv : empty'''
	global saved
	global top
	global decFunciones
	if not decFunciones:
		saved = top
		top = Env(saved)	

def p_b3(p):
	'''b3 : declaracion b3
	| empty'''

def p_b4(p):
	'''b4 : estatuto b4
	| empty'''

def p_b5(p):
	'''b5 : recEnv RKEY'''

def p_recEnv(p):
	'''recEnv : empty'''
	global top
	global saved
	global EnvParam
	global decFunciones
	if not decFunciones:
		top.release()
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

#verificamos el contenido de la pila de operadores antes de almacenar el valor nuevo....en cado de que contanga alguno de
#los operadores vistos abajo primero sacaremos los operadores para generar cuadruplos
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
			#validamos los tipos de datos de acuerdo al cubo semantico, para saber si la operacion es compatible entre estos
			resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
			if resultType == "ERROR":
				print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operador, tipoDerecho
				sys.exit(0)
			else:
				global temporal
				nombre = "t" + str(temporal)
				temporal = temporal + 1
				result = "mem-" + UnivMemManager.saveTEMP(nombre)
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
	
#verificamos el contenido de la pila de operadores antes de almacenar el valor nuevo....en cado de que contanga alguno de
#los operadores vistos abajo primero sacaremos los operadores para generar cuadruplos	
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
			#validamos el tipo de dato para ver si la operacion es compatible entre estos
			resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
			if resultType == "ERROR":
				print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operador, tipoDerecho
				sys.exit(0)
			else:
				global temporal
				nombre = "t" + str(temporal)
				temporal = temporal + 1
				result = "mem-" + UnivMemManager.saveTEMP(nombre)
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

#verificamos el contenido de la pila de operadores antes de almacenar el valor nuevo....en cado de que contanga alguno de
#los operadores vistos abajo primero sacaremos los operadores para generar cuadruplos
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
			#revisamos si la operacion es compatible entre los tipos de operadores de la pila
			resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
			if resultType == "ERROR":
				print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operador, tipoDerecho
				sys.exit(0)
			else:
				global temporal
				nombre = "t" + str(temporal)
				temporal = temporal + 1
				result = "mem-" + UnivMemManager.saveTEMP(nombre)
				quad = Cuadruplo(operador, operandoIzquierdo, operandoDerecho, result)
				cuadru.append(quad)
				PilaO.push(result)
				PTypes.push(resultType)
				
				
			#PilaO.push(POper.pop())
			if POper.isEmpty():
				break
		
	
		

####################DECLARACION DE VARIABLES#############################
def p_declaracion(p):
	'''declaracion : tipo ID savevar decla1'''
	#print "Declaracion"

var = None
DIM = None
R = None
DimAnt = None
DimNext = None
def p_savevar(p):
	'''savevar : empty'''
	global var
	#global Localfunc
	var = Variable(p[-2],p[-1],None,None)

def p_decla1(p):
	'''decla1 : saveMemNormal declafinal 
	| LBRACKET decDimensionada exp saveLimSup decla2'''

def p_saveMemNormal(p):
	'''saveMemNormal : empty '''
	global var
	pos = UnivMemManager.save(var.type,var.identifier)
	var.memory = pos

#Obtener un campo para la dimension; Ligar ese campo a la variable
#DIM = 1 R = 1
def p_decDimensionada(p):
	'''decDimensionada : empty'''
	global var
	global DIM
	global R
	global DimAnt
	global esdimen
	esdimen=True
	DimAnt = Dimension()
	DIM = 1
	R = 1

#Almacenar en campo de dimensionada la constante del limite superior
#Acumulamos R
def p_saveLimSup(p):
	'''saveLimSup : empty'''
	global PilaO
	global PTypes
	global var
	global R
	global esdimen
	if PTypes.pop() == "INT":
		DimAnt.LsDIM = PilaDi.pop()
		PilaO.pop()
		DimAnt.LiDIM = 0
		R = (DimAnt.LsDIM - DimAnt.LiDIM + 1) * R
	else:
		print "Declaracion de dimension incorrecta, la dimension debe ser un valor entero"
		sys.exit()

def p_decla2(p):
	'''decla2 : RBRACKET guardaMemDimen declafinal
	| COMA SigDimension exp saveLimSup decla2'''

#DIM = DIM + 1
#Obtener un nuevo campo para la siguiente descripcion
#Ligar el campo anterior con  el nuevo campo
def p_SigDimension(p):
	'''SigDimension : empty '''
	global DIM
	global var
	global DimAnt
	global DimNext
	DIM = DIM + 1
	newDim = Dimension()
	newDim.antDim = DimAnt
	DimAnt.nextDim = newDim
	DimAnt = newDim

def p_guardaMemDimen(p):
	'''guardaMemDimen : empty'''
	global var
	global DimAnt
	global DIM
	global R
	var.size = DimAnt
	var.goHeadDim()
	DIM = 1
	suma = 0
	aux = R
	flagBol = True
	while flagBol:
		var.size.mDIM = R / (var.size.LsDIM - var.size.LiDIM + 1)
		R = var.size.mDIM
		suma = suma + var.size.LiDIM * var.size.mDIM
		DIM = DIM + 1
		flagBol = var.goDimForward()
	k = suma
	var.size.mDIM = -k
	pos = UnivMemManager.saveDimensions(var.type,var.identifier,aux)
	var.memory = pos
	var.Auxil = aux 
	var.goHeadDim()

def p_declafinal(p):
	'''declafinal : PUNTOCOMA'''
	global var
	global top
	global UnivMemManager
	global TablaFunciones
	global decFunciones
	global FuncToBuild
	global esdimen
	if decFunciones:
		FuncToBuild.LocalVars.append(var)
		TablaFunciones.get(FuncToBuild.identifier).LocalVars.append(var)
	top.put(var.identifier,var)
	esdimen=False;
	
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

def p_asignacion(p):
	'''asignacion : ID meteid asigfinal
	| f7 asigfinal'''
	global decFunciones
	if not decFunciones:
		pass
#buscamos la posicion de memoria del ID recibido y lo metemos a la pila de operandos
#despues metemos el tipo a la pila de tipos
def p_meteid(p):
	'''meteid :  empty''' 
	PilaO.push("mem-"+top.get(p[-1]).memory)
	PTypes.push(top.get(p[-1]).type)
	
	
def p_asig2(p):
	'''asig2 : LBRACKET exp asig3
	| asigfinal'''

def p_asig3(p):
	'''asig3 : COMA exp asig3
	| RBRACKET asigfinal'''

def p_asigfinal(p):
	'''asigfinal : IGUAL tagmeteig asigf2'''
	#POper.push(p[1])
	
def p_asigf2(p):
	'''asigf2 : expresion tagig PUNTOCOMA
	| read tagig
	| readint tagig'''

#metemos a la pila de operadores el operador recibido ( = )	
def p_tagmeteig(p):
	'''tagmeteig : empty'''
	POper.push(p[-1])


def p_tagig(p):
	'''tagig : empty'''
	operandoDerecho = PilaO.pop()
	tipoDerecho = PTypes.pop()
	operandoIzquierdo = PilaO.pop()
	tipoIzquierdo = PTypes.pop()
	operador = POper.pop()
	#revisamos la compatibilidad entre los operandos y el operador utilizados
	resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
	if resultType == "ERROR":
		print "Incompatibilidad entre los tipos de la operacion: ", tipoIzquierdo, operador, tipoDerecho
		sys.exit(0)
	else:
		#global temporal
		#result = "t" + str(temporal)
		#temporal = temporal + 1
		quad = Cuadruplo(pos1 = operador, pos2=operandoDerecho, pos4=operandoIzquierdo)
		cuadru.append(quad)
		#PilaO.push(result)
		#PTypes.push(resultType)
	
#########################ESCRITURA####################################
def p_print(p):
	'''print : PRINT LPARENT pr2'''

def p_pr2(p):
	'''pr2 : expresion pr3'''

def p_pr3(p):
	'''pr3 : tagimprime RPARENT PUNTOCOMA'''

#generamos el cuadruplo para imprimir en pantalla pasando la posicion de memoria que se imprimira
def p_tagimprime(p):
	'''tagimprime : empty'''
	quad = Cuadruplo(pos1 = "PRINT", pos4=PilaO.pop())
	cuadru.append(quad)

########################TERMINO#################################
def p_termino(p):
	'''termino : factor tagsacopm te2'''

def p_te2(p):
	'''te2 : MULT tagm termino 
	| DIV tagm termino
	| empty'''
	
#metemos el operador a la pila de operaodres (+) o (-)	
def p_tagm(p):
	'''tagm : empty'''
	POper.push(p[-1])
		
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
			#revisamos compatibilidad entre los tipos de los operandos y el operador
			resultType = validacion(tipoIzquierdo, tipoDerecho, operador)
			if resultType == "ERROR":
				print "INCOMPATIBILIDAD DE TIPOS"
				sys.exit()
			else:
				#generamos memoria temporal en donde se almacenara el resultado de la operacion cuando se ejecute
				global temporal
				nombre = "t" + str(temporal)
				temporal = temporal + 1
				result = "mem-" + UnivMemManager.saveTEMP(nombre)
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
	| f7
	| f9'''
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
	PilaO.push("mem-"+top.get(p[1]).memory)
	PTypes.push(top.get(p[1]).type)
	
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
	
def p_f7(p):
	'''f7 : ID LBRACKET tagrevisadime exp tagmetedim f8'''

def p_f8(p):
	'''f8 : COMA tagotradim exp tagmetedim f8
	| RBRACKET tagterminadim'''

def p_tagrevisadime(p):
	'''tagrevisadime : empty'''
	global Dim
	nombre = p[-2]
	if top.get(nombre).size==None:
		print "La variable " + nombre + " no tiene dimensiones"
		sys.exit()
	else:
		Dim=1
		PilaDimensionadas.push(nombre)
		PilaDim.push(Dim)
		POper.push(p[-1])

#generamos el cuadruplo para verificar los limites de la variable dimensionada
def p_tagmetedim(p):
	'''tagmetedim : empty'''
	global Dim
	valor = PilaO.peek()
	nombre=PilaDimensionadas.peek()
	lsuperior=top.get(nombre).size.LsDIM
	quad = Cuadruplo("Verifica", valor, 0, lsuperior)
	cuadru.append(quad)

	if  top.get(nombre).size.nextDim != None:
		aux = PilaO.pop()
		result = "mem-" + UnivMemManager.saveTEMP(0)
		quad = Cuadruplo("*" , aux, top.get(nombre).size.mDIM , result)
		cuadru.append(quad)
		PilaO.push(result)
	if Dim>1:
		aux2 = PilaO.pop()
		aux1 = PilaO.pop()
		result = "mem-" + UnivMemManager.saveTEMP(0)
		quad = Cuadruplo("+" , aux1, aux2 , result)
		cuadru.append(quad)
		PilaO.push(result)

#revisamos el numero de dimensiones a las que estamos intentando acceder
def p_tagotradim(p):
	'''tagotradim : empty'''
	nombre=PilaDimensionadas.peek()
	if top.get(nombre).size.nextDim==None:
		print "Estas asignando mas dimensiones de las necesitadas por la variable " + nombre
		sys.exit() 
	global Dim
	Dim = Dim + 1
	PilaDim.push(Dim)
	nombre=PilaDimensionadas.peek()
	top.get(nombre).goDimForward()

#revisamos si se pasaron las dimensiones necesarias a la variable dimensionada
def p_tagterminadim(p):
	'''tagterminadim : empty'''
	nombre=PilaDimensionadas.peek()
	if top.get(nombre).size.nextDim!=None:
		print "Faltan mas dimensiones para la variable " + nombre
		sys.exit() 
	aux1=PilaO.pop()
	nombre=PilaDimensionadas.peek()
	result = "mem-" + UnivMemManager.saveTEMP(0)
	quad = Cuadruplo("+" , aux1, top.get(nombre).size.mDIM , result)
	cuadru.append(quad)
	quad = Cuadruplo("+" , result, top.get(nombre).memory , result)
	cuadru.append(quad)
	result="mem-" + result
	PilaO.push(result)
	POper.pop()
	PilaDimensionadas.pop()
	top.get(nombre).goHeadDim()

#llamar a una funcion
def p_f6(p):
	'''f6 : llamafuncion'''

def p_guardafunc(p):
	'''guardafunc : empty'''
	result = "mem-" + UnivMemManager.saveTEMP(0)
	PilaO.push(result)

def p_f9(p):
	'''f9 : find'''


def p_find(p):
	'''find : FIND  tagfon LPARENT tagfondofalso exp RPARENT tagsaca PUNTO ID LBRACKET tagfind RBRACKET'''


def p_tagfind(p):
	'''tagfind : empty'''
	if top.get(p[-2]).size==None:
		print "No puedes hacer find de una variable no dimensionada"
	else:
		result=result = "mem-" + UnivMemManager.saveTEMP(0)
		PTypes.pop()
		quad=Cuadruplo(pos1="find", pos2=PilaO.pop(), pos3=str(top.get(p[-2]).memory) + "-" + str(top.get(p[-2]).Auxil), pos4=result)
		cuadru.append(quad)
		PTypes.push("INT")
		PilaO.push(result)
		POper.pop()

def p_tagsaca(p):
	'''tagsaca : empty'''
	POper.pop()

def p_tagfon(p):
	'''tagfon : empty'''
	POper.push("(")


def p_sort(p):
	'''sort : SORT LPARENT RPARENT PUNTO ID LBRACKET RBRACKET PUNTOCOMA'''
	if top.get(p[5]).size==None:
		print "No puedes hacer sort de una variable no dimensionada"
		sys.exit()
	else:
		quad=Cuadruplo(pos1="sort", pos2=top.get(p[5]).memory, pos3=top.get(p[5]).Auxil)
		cuadru.append(quad)
######################CONTENIDO DE UN ESTATUTO##################################

def p_estatuto(p):
	'''estatuto : asignacion
	| print
	| ciclowhile
	| ciclodowhile
	| ciclofor
	| read
	| readint
	| comentario
	| cuadrado
	| triangulo
	| casa
	| rectangulo
	| cubo
	| trapecio
	| estrella
	| firma
	| mueve
	| levanta
	| apoya
	| dimension
	| llamafuncion
	| return
	| if
	| sort'''
#	| potencia
#	| raiz

#####################COMENTARIO######################################

def p_comentario(p):
	'''comentario : COMENTARIO'''

######################VARIABLE CONSTANTE#####################################

def p_varcte(p):
	'''varcte : ENTERO tagint
	| FLOTANTE tagfloat
	| CADENA tagcad
	| CARACTER tagcar
	| TRUE tagbol
	| FALSE tagbol'''

#guardamos en memoria el valor recibido y generamos el cuadruplo con esa posicion de memoria
#guardamos en la pila de tipos el tipo del valor recibido	
def p_tagint(p):
	'''tagint : empty'''
	result = "mem-" + UnivMemManager.saveTEMP(p[-1])
	PilaO.push(result)
	PTypes.push("INT")
	if esdimen:
		PilaDi.push(p[-1])

#guardamos en memoria el valor recibido y generamos el cuadruplo con esa posicion de memoria
#guardamos en la pila de tipos el tipo del valor recibido		
def p_tagfloat(p):
	'''tagfloat : empty'''
	result = "mem-" + UnivMemManager.saveTEMP(p[-1])
	PilaO.push(result)
	PTypes.push("FLOAT")

#guardamos en memoria el valor recibido y generamos el cuadruplo con esa posicion de memoria
#guardamos en la pila de tipos el tipo del valor recibido		
def p_tagcad(p):
	'''tagcad : empty'''
	result = "mem-" + UnivMemManager.saveTEMP("\""+ p[-1]+"\"")
	PilaO.push(result)
	PTypes.push("STRING")

#guardamos en memoria el valor recibido y generamos el cuadruplo con esa posicion de memoria
#guardamos en la pila de tipos el tipo del valor recibido		
def p_tagcar(p):
	'''tagcar : empty'''
	result = "mem-" + UnivMemManager.saveTEMP("\""+ p[-1]+"\"")
	PilaO.push(result)
	PTypes.push("CHAR")

#guardamos en memoria el valor recibido y generamos el cuadruplo con esa posicion de memoria
#guardamos en la pila de tipos el tipo del valor recibido		
def p_tagbol(p):
	'''tagbol : empty'''
	result = "mem-" + UnivMemManager.saveTEMP(p[-1])
	PilaO.push(result)
	PTypes.push("BOOL")


#####################CICLOS Y OTRAS FUNCIONES####################################
def p_ciclowhile(p):
	'''ciclowhile : WHILE taginiciawhile LPARENT expresion RPARENT tagwhile bloque tagregresawhile'''

#guardamos la posicion del cuadruplo actual para saber a donde regresar en el ciclo	
def p_taginiciawhile(p):
	'''taginiciawhile : empty'''
	PSaltos.push(len(cuadru))

#revisamos si la condicion a evaluar es booleana, en caso de no serlo mostramos un mensaje de error		
def p_tagwhile(p):
	'''tagwhile : empty'''
	expType = PTypes.pop()
	if not expType == "BOOL":
		print "Error en el tipo de expresion a analizar en el ciclo while"
		sys.exit()
	else:
		result = PilaO.pop()
		quad = Cuadruplo(pos1="GoToF", pos2=result)
		cuadru.append(quad)
		PSaltos.push(len(cuadru)-1)
		
def p_tagregresawhile(p):
	'''tagregresawhile : empty'''
	end = PSaltos.pop()
	returne = PSaltos.pop()
	quad = Cuadruplo(pos1="GoTo", pos4=returne)
	cuadru.append(quad)
	cuadru[end].pos4=len(cuadru)

##################################CICLO DO WHILE###########################################################
def p_ciclodowhile(p):
	'''ciclodowhile : DO taginiciado bloque WHILE LPARENT expresion tagcondiciondo RPARENT PUNTOCOMA'''


def p_taginiciado(p):
	'''taginiciado : empty'''
	PSaltos.push(len(cuadru))

#revisamos si la condicion a evaluar es booleana, en caso de no serlo mostramos un mensaje de error		
def p_tagcondiciondo(p):
	'''tagcondiciondo : empty'''
	expType = PTypes.pop()
	if not expType == "BOOL":
		print "Error en la expresion al analizar el ciclo do while"
		sys.exit()
	else:
		result = PilaO.pop()
		regresa = PSaltos.pop()
		quad = Cuadruplo(pos1="GotoT", pos2=result, pos4=regresa)
		cuadru.append(quad)

#####################################################################################################################
#generamos el cuadruplo de lectura
def p_read(p):
	'''read : READ LPARENT RPARENT PUNTOCOMA'''
	result = "mem-" + UnivMemManager.save("STRING", "temporallectura")
	PilaO.push(result)
	PTypes.push("STRING")
	quad = Cuadruplo(pos1="READ", pos4=result)
	cuadru.append(quad)

#generamos el cuadruplo para leer valores numericos
def p_readint(p):
	'''readint : READINT LPARENT RPARENT PUNTOCOMA'''
	result = "mem-" + UnivMemManager.save("INT", "temporalentero")
	PilaO.push(result)
	PTypes.push("INT")
	quad = Cuadruplo(pos1="READINT", pos4=result)
	cuadru.append(quad)


def p_ciclofor(p):
	'''ciclofor : FOR LPARENT asignacion expresion tagevaluafor asignacion tagespera RPARENT bloque tagasigna tagterminafor'''

#revisamos si la condicion a evaluar es booleana, en caso de no serlo mostramos un mensaje de error		
def p_tagevaluafor(p):
	'''tagevaluafor : empty'''
	if not PTypes.pop() == "BOOL":
		print "Error en la condicion evaluada en el IF"
		sys.exit()
	else:
		result = PilaO.pop()
		quad = Cuadruplo(pos1="GoToF", pos2=result)
		cuadru.append(quad)
		PSaltos.push(len(cuadru)-1)
		PSaltos.push(len(cuadru)-2)

def p_tagterminafor(p):
	'''tagterminafor : empty'''
	end = PSaltos.pop()
	cuadru[end].pos4=len(cuadru)

def p_tagespera(p):
	'''tagespera : empty'''
	PilaEspera.push(cuadru.pop())

def p_tagasigna(p):
	'''tagasigna : empty'''
	cuadru.append(PilaEspera.pop())
	end = PSaltos.pop()
	quad = Cuadruplo(pos1="GoTo", pos4=end)
	cuadru.append(quad)


def p_if(p):
	'''if : IF LPARENT expresion tagif RPARENT bloque if2'''

def p_if2(p):
	'''if2 : tagterminaif
	| ELSE tagelse bloque tagterminaif'''

#revisamos si la condicion a evaluar es booleana, en caso de no serlo mostramos un mensaje de error	
def p_tagif(p):
	'''tagif : empty'''
	if not PTypes.pop() == "BOOL":
		print "Error en la condicion evaluada en el IF"
		sys.exit()
	else:
		result = PilaO.pop()
		quad = Cuadruplo(pos1="GoToF", pos2=result)
		cuadru.append(quad)
		PSaltos.push(len(cuadru)-1)
		
def p_tagelse(p):
	'''tagelse : empty'''
	end = PSaltos.pop()
	cuadru[end].pos4=(len(cuadru)+1)
	quad = Cuadruplo(pos1="GoTo")
	cuadru.append(quad)
	PSaltos.push(len(cuadru)-1)
		
def p_tagterminaif(p):
	'''tagterminaif : empty'''
	end = PSaltos.pop()
	cuadru[end].pos4=len(cuadru)

def p_return(p):
	'''return : RETURN llegoRet expresion PUNTOCOMA'''
	quad = Cuadruplo(pos1= "Return", pos2=PilaO.pop())
	cuadru.append(quad)

def p_llegoRet(p):
	'''llegoRet : empty'''
	global LlegoReturn
	global TablaFunciones
	global FuncToBuild
	if(FuncToBuild.type == "VOID"):
		print "valor de retorno inesperado"
		sys.exit()
	else:
		LlegoReturn = True

#def p_potencia(p):
#	'''potencia : POW LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
#	print "potencia"

#def p_raiz(p):
#	'''raiz : SQRT LPARENT varcte RPARENT PUNTOCOMA'''
#	print "raiz"
###################ERROR#####################################

def p_error(p):
	print "error de sintaxis en la linea " + str(p.lineno)
	print p
	sys.exit()
	
################FUNCIONES DIIBUJAR###############################


def p_cuadrado(p):
	'''cuadrado : CUADRADO LPARENT exp COMA exp COMA exp RPARENT tagcuadro PUNTOCOMA'''

def p_tagcuadro(p):
	'''tagcuadro : empty'''
	quad = Cuadruplo(pos1 = "CUADRADO", pos2=PilaO.pop(), pos3=PilaO.pop(), pos4=PilaO.pop())
	cuadru.append(quad)
	
	
def p_triangulo(p):
	'''triangulo : TRIANGULO LPARENT exp COMA exp COMA exp RPARENT tagtriangulo PUNTOCOMA'''
	
def p_tagtriangulo(p):
	'''tagtriangulo : empty'''
	quad = Cuadruplo(pos1 = "TRIANGULO", pos2=PilaO.pop(), pos3=PilaO.pop(), pos4=PilaO.pop())
	cuadru.append(quad)
	
def p_rectangulo(p):
	'''rectangulo : RECTANGULO LPARENT exp COMA exp RPARENT PUNTOCOMA'''

def p_casa(p):
	'''casa : CASA LPARENT exp COMA exp RPARENT PUNTOCOMA'''

def p_estrella(p):
	'''estrella : ESTRELLA LPARENT exp COMA exp COMA exp RPARENT tagestrella PUNTOCOMA'''

def p_tagestrella(p):
	'''tagestrella : empty'''
	quad = Cuadruplo(pos1 = "ESTRELLA", pos2=PilaO.pop(), pos3=PilaO.pop(), pos4=PilaO.pop())
	cuadru.append(quad)

def p_firma(p):
	'''firma : FIRMA LPARENT RPARENT PUNTOCOMA'''
	quad = Cuadruplo(pos1 = "FIRMA")
	cuadru.append(quad)


def p_cubo(p):
	'''cubo : CUBO LPARENT exp COMA exp COMA exp RPARENT tagcubo PUNTOCOMA'''
	
def p_tagcubo(p):
	'''tagcubo : empty'''
	quad = Cuadruplo(pos1 = "CUBO", pos2=PilaO.pop(), pos3=PilaO.pop(), pos4=PilaO.pop())
	cuadru.append(quad)

def p_mueve(p):
	'''mueve : MUEVE LPARENT exp COMA exp RPARENT tagmueve PUNTOCOMA'''
	
def p_tagmueve(p):
	'''tagmueve : empty'''
	quad = Cuadruplo(pos1 = "MUEVE", pos2=PilaO.pop(), pos3=PilaO.pop())
	cuadru.append(quad)
	
def p_levanta(p):
	'''levanta : LEVANTA LPARENT RPARENT PUNTOCOMA'''
	quad = Cuadruplo(pos1 = "LEVANTA")
	cuadru.append(quad)
	
def p_apoya(p):
	'''apoya : APOYA LPARENT RPARENT PUNTOCOMA'''
	quad = Cuadruplo(pos1 = "APOYA")
	cuadru.append(quad)
	
def p_trapecio(p):
	'''trapecio : TRAPECIO LPARENT exp COMA exp RPARENT PUNTOCOMA'''
	
def p_dimension(p):
	'''dimension : DIMENSION LPARENT exp RPARENT PUNTOCOMA'''

##########################DECLARA UNA FUNCION##########################
def p_function(p):
	'''function : FUNCTION pfunc'''

def p_pfunc(p):
	'''pfunc : tipo ID buildFunc LPARENT funct11
	| VOID ID buildFunc LPARENT funct11'''

def p_buildFunc(p):
	'''buildFunc : empty'''
	#iniciamos a construir nuestro objeto funcion
	#que sera guardado en nuestra tabla de funciones
	#agregandole el tipo y su identificador como atributos
	global FuncToBuild
	global top
	FuncToBuild = Funcion(p[-2], p[-1])
	if not p[-2] == "VOID":
		pos = UnivMemManager.save(p[-2], p[-1])
		FuncToBuild.ReturnValue = Variable(p[-2], p[-1], pos, None)
		TablaFunciones.put(p[-1], FuncToBuild)
		top.put(p[-1],FuncToBuild.ReturnValue)
	else:
		TablaFunciones.put(p[-1], FuncToBuild)
	
def p_funct11(p):
	'''funct11 : function4'''

def p_funct111(p):
	'''funct11 : initParamTable funct2'''

def p_initParamTable(p):
	'''initParamTable : empty'''
	#iniciamos el ambiente de variables locales
	#y el de la tabla de parametros
	#global Localfunc
	global EnvParam
	global top
	EnvParam =[]
	#Localfunc = Env(None)
	top = Env(top)
	
def p_funct2(p):
	'''funct2 : tipo ID initParams funct3'''

def p_initParams(p):
	'''initParams : empty'''
	#guardamos cada parametro en ambas tablas de
	#locales y parametros
	global UnivMemManager
	global decFunciones
	global TablaFunciones
	#global Localfunc
	global FuncToBuild
	global EnvParam
	decFunciones = True
	pos = UnivMemManager.save(p[-2],p[-1])
	var = Variable(p[-2],p[-1],pos,None)
	FuncToBuild.LocalVars.append(var)
	TablaFunciones.get(FuncToBuild.identifier).LocalVars.append(var)
	#EnvParam.put(p[-1],var)
	EnvParam.append(p[-2]);
	TablaFunciones.get(FuncToBuild.identifier).ParamTable.append(p[-2])
	#Localfunc.put(p[-1],var)
	top.put(p[-1],var)

def p_funtion3(p):
	'''funct3 : COMA funct2'''


def p_function31(p):
	'''funct3 : function4'''

	
def p_function4(p):
	'''function4 : RPARENT initFunc bloque noinitFunc'''

def p_initFunc(p):
	'''initFunc : empty'''
	global FuncToBuild
	global EnvParam	
	FuncToBuild.ParamTable = EnvParam
	FuncToBuild.Cont = len(cuadru)


def p_noinitFunc(p):
	'''noinitFunc : empty'''
	global decFunciones
	global top
	global FuncToBuild
	global LlegoReturn
	if not LlegoReturn and not FuncToBuild.type == "VOID":
		print "La funcion " + FuncToBuild.identifier + " necesita un valor de retorno"
		sys.exit()
	FuncToBuild.LocalTable = top
	TablaFunciones.get(FuncToBuild.identifier).LocalTable.release()
	decFunciones = False
	quad = Cuadruplo(pos1="ENDPROC")
	cuadru.append(quad)

##################LLAMA UNA FUNCION###############################
def p_llamafuncion(p):
	'''llamafuncion : ID LPARENT tagverificafuncion llamaf11'''

def p_llamaf11(p):
	'''llamaf11 : llamaf2
	| llamaf4'''
	
def p_llamaf2(p):
	'''llamaf2 : exp tagrevisaparam llamaf3'''

def p_llamaf3(p):
	'''llamaf3 : COMA tagotroargumento llamaf2
	| llamaf4'''
	
def p_llamaf4(p):
	'''llamaf4 : RPARENT  tagterminallamada PUNTOCOMA'''

#revisamos si la funcion a la que estamos llamando existe en la tabla de funciones
def p_tagverificafuncion(p):
	'''tagverificafuncion : empty'''
	global nombredelafuncion
	global contadorParametro
	if TablaFunciones.get(p[-2]) == None:
		print "La funcion " + p[-2] + " no existe" 
		sys.exit()
	else:
		contadorParametro=1
		nombreFuncion=p[-2]
		nombredelafuncion=nombreFuncion
		POper.push(p[-1])
		quad = Cuadruplo(pos1 = "ERA", pos2 =nombreFuncion)
		cuadru.append(quad)

#revisamos los parametros que se envian en la llamada de la funcion (tipo y numero de argumentos)
def p_tagrevisaparam(p):
	'''tagrevisaparam : empty'''
	argumentoEnviado = TablaFunciones.get(nombredelafuncion).getParamType(contadorParametro-1);
	if argumentoEnviado == None:
		print "Estas enviando más argumentos de los que solicita la funcion "
		sys.exit()
	argument = PilaO.pop()
	argumentType = PTypes.pop()
	if argumentType != argumentoEnviado:
		print "Hay incompatibilidad entre el tipo de parametros enviados a la funcion " + nombredelafuncion
		sys.exit()
	else:
		quad=Cuadruplo(pos1 = "param", pos2 = argument, pos4="param"+str(contadorParametro))
		cuadru.append(quad)

#aumentamos el contador porque significa que viene otro parametro
def p_tagotroargumento(p):
	'''tagotroargumento : empty'''
	global contadorParametro
	contadorParametro = contadorParametro + 1

#revisamos si la funcion tiene todos los parametros necesarios
#generamos el cuadruplo para ir a la subrutina de esa funcion
def p_tagterminallamada(p):
	'''tagterminallamada : empty'''
	argumentoEnviado = TablaFunciones.get(nombredelafuncion).getParamType(contadorParametro);
	if argumentoEnviado != None:
		print "La funcion requiere más parametros"
		sys.exit()
	quad =Cuadruplo(pos1="gosub", pos2=nombredelafuncion)
	cuadru.append(quad)
	memoria = TablaFunciones.get (nombredelafuncion).ReturnValue.memory
	tipo = TablaFunciones.get (nombredelafuncion).ReturnValue.type
	PilaO.push("mem-" + memoria)
	PTypes.push(tipo)
	POper.pop()

		
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

#UnivMemManager.asigna(8,"hahahaha")
#print UnivMemManager.find(8)
#print "---------------------------------------------------------------------"
#print "--------------------MEMORIA--------------------"
#print UnivMemManager.memory	


#print TablaFunciones.get("funcionEnv").ReturnValue.identifier
#print TablaFunciones.get("funcionEnv").	ReturnValue.memory
#print TablaFunciones.get("funcionEnv").getVarMemory(5)
#print TablaFunciones.get("iBarney").LocalTable.get("ij").memory



###################################################################################
########CUADRUPLOS#################################################################

#print "---------------------------------------------------------------------"
#print "--------------------CUADRUPLOS GENERADOS--------------------"
#q = 0
#for i in cuadru:
#	print str(q) + " | ",
#	print i.pos1, i.pos2, i.pos3, i.pos4
#	q = q + 1 
###########################################################################
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


