#MARY17
#Oliver Alejandro Martinez Quiroz A01280416
#Diego Alejandro Mayorga Morales A00813211

import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin

precedence = (
	('right', 'IGUAL'),
	('left', 'LT', 'GT'),
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




#definimos la clase para la tabla por enviroment
#Nos servira para simular el creado de tablas por scope
class Env:
	dict = {}
	#Este atributo es un objeto de la misma clase Env
	#Representa el scope anterior 
	prev = None
	def __init__(ant):
		prev = ant

#funcion que nos sirve para insertar un nuevo simbolo a la tabla
	def put(identifier, content):
			dict[identifier] = content.copy()

#funcion que itera por las tablas para encontrar un simbolo
#empieza por el scope actual y regresa una tabla o None si no encuentra la variable

	def get(identifier):
		e = self.table
		while e != None:
			if identifier in e:
  				return [identifier]
  				break
			else:
				e = e.prev
		return None


#definimos la pila de variables y tipos de datos
Stack_Variables = Stack()
Stack_Types = Stack()

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

####################CONTENIDO DE UN PROGRAMA###################################
def p_program(p):
	'''program : PROGRAM ID DOSPUNTOS p2'''
	#p[0] = program(p[4], "program")
	print "programa"

def p_p2(p):
	'''p2 : declaracion p3'''
	#p[0] = p2(p[1], "p2")
	#print "p2"

def p_p3(p):
	'''p3 : p2
	| bloque'''

########################CONTENIDO DE UN BLOQUE######################################


def p_bloque(p):
	'''bloque : LKEY b2'''
	print "bloque"

def p_b2(p):
	'''b2 : b3
	| RKEY'''

def p_b3(p):
	'''b3 : estatuto b4'''

def p_b4(p):
	'''b4 : b3
	| RKEY'''

###########################CONTENIDO DE UNA EXPRESION#################################
def p_expresion(p):
	'''expresion : exp e2 '''
	print "expresion"


def p_e2(p):
	'''e2 : e3 
	| empty'''

def p_e3(p):
	'''e3 : GT exp
	| LT exp
	| LT GT exp'''

##################EXP###################################
def p_exp(p):
	'''exp : termino exp2'''
	print "exp"

def p_exp2(p):
	'''exp2 : SUMA exp 
	| RESTA exp
	| empty'''	

####################DECLARACION DE VARIABLES#############################
def p_declaracion(p):
	'''declaracion : tipo ID PUNTOCOMA'''
	#p_creartabla(p)
	AddGlobalVariable(p[1],p[2])
	print "declaracion"

######################TIPO DE VARIABLES######################################
def p_tipo(p):
	'''tipo : INT
	| FLOAT
	| CHAR
	| STRING
	| BOOL'''
	p[0] = p[1]
	print "tipo"

##################ASIGNACION A VARIABLES###################################
def p_asignacion(p):
	'''asignacion : ID IGUAL expresion PUNTOCOMA'''
	print "asignacion"
#########################ESCRITURA####################################
def p_print(p):
	'''print : PRINT LPARENT pr2'''
	print "esritura"

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
	print "condicion"

def p_c2(p):
	'''c2 : ELSE bloque PUNTOCOMA
	| PUNTOCOMA'''
	#print "c2"

########################TERMINO#################################
def p_termino(p):
	'''termino : factor te2'''
	print "termino"

def p_te2(p):
	'''te2 : MULT termino 
	| DIV termino
	| empty'''	
######################FACTOR####################################
def p_factor(p):
	'''factor : LKEY expresion RKEY
	| f2'''
	print "factor"
	if p[1] == '{':
		p[0] = p[2]
	else:
		p[0] = p[1]

def p_f2(p):
	'''f2 : SUMA varcte
	| RESTA varcte
	| varcte'''
	if p[1] == '+' or p[1] == '-':
		p[0] = p[2]
	else:
		p[0] = p[1]
	#print p[0]





######################CONTENIDO DE UN ESTATUTO##################################

def p_estatuto(p):
	'''estatuto : asignacion
	| print
	| condicion
	| ciclowhile
	| ciclodowhile
	| ciclofor
	| read
	| declaracion
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
	| function'''
#	| potencia
#	| raiz
	print "estatuto"

#####################COMENTARIO######################################

def p_comentatio(p):
	'''comentario : COMENTARIO'''
	print "Comentario"

######################VARIABLE CONSTANTE#####################################

def p_varcte(p):
	'''varcte : ID
	| ENTERO
	| FLOTANTE
	| CADENA
	| CARACTER'''
	p[0]=p[1] 
	print "varcte"


#####################CICLOS Y OTRAS FUNCIONES####################################
def p_ciclowhile(p):
	'''ciclowhile : WHILE LPARENT expresion RPARENT bloque'''
	print "ciclo While"

def p_ciclodowhile(p):
	'''ciclodowhile : DO bloque WHILE LPARENT expresion RPARENT PUNTOCOMA'''
	print "ciclo do while"

def p_read(p):
	'''read : ID IGUAL READ LPARENT RPARENT PUNTOCOMA'''
	print "lectura"

def p_ciclofor(p):
	'''ciclofor : FOR LPARENT asignacion expresion asignacion RPARENT bloque'''
	print "ciclo for"

#def p_potencia(p):
#	'''potencia : POW LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
#	print "potencia"

#def p_raiz(p):
#	'''raiz : SQRT LPARENT varcte RPARENT PUNTOCOMA'''
#	print "raiz"
###################ERROR#####################################

def p_error(p):
	print "error de sintaxis", p
	print "error en la linea" +str(p.lineno)
	
################FUNCIONES DIIBUJAR###############################


def p_cuadrado(p):
	'''cuadrado : CUADRADO LPARENT varcte RPARENT PUNTOCOMA'''
	print "Dibuja cuadrado"
	
def p_triangulo(p):
	'''triangulo : TRIANGULO LPARENT varcte RPARENT PUNTOCOMA'''
	print "Dibuja triangulo"
	
def p_rectangulo(p):
	'''rectangulo : RECTANGULO LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
	print "Dibuja rectangulo"

def p_casa(p):
	'''casa : CASA LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
	print "Dibuja casa"

def p_estrella(p):
	'''estrella : ESTRELLA LPARENT varcte RPARENT PUNTOCOMA'''
	print "Dibuja estrella"

def p_cubo(p):
	'''cubo : CUBO LPARENT varcte RPARENT PUNTOCOMA'''
	print "Dibuja cubo"

def p_mueve(p):
	'''mueve : MUEVE LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
	print "Mueve"
	
def p_levanta(p):
	'''levanta : LEVANTA LPARENT RPARENT PUNTOCOMA'''
	print "Levanta lapiz"
	
def p_apoya(p):
	'''apoya : APOYA LPARENT RPARENT PUNTOCOMA'''
	print "Apoya lapiz"
	
def p_trapecio(p):
	'''trapecio : TRAPECIO LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
	print "Dibuja trapecio"
	
def p_dimension(p):
	'''dimension : DIMENSION LPARENT varcte RPARENT PUNTOCOMA'''
	print "Asigna dimension"
	
def p_function(p):
	'''function : tipo ID LPARENT funct2'''
	print "Declara una funcion"
	
def p_funct2(p):
	'''funct2 : tipo varcte funct3'''
	
def p_funtion3(p):
	'''funct3 : COMA funct2
	| RPARENT bloque'''
		
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

directorio = '../tests/'
archivo = buscarPrograma(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)
print global_string
print global_int

print result

