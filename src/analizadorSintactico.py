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
def AddGlobalVariable(typew, identifier):
	print("Tipo de variable: "  + str(typew) + " Nombre de variable: " + str(identifier))
	if SearchGlobalVariable(identifier):
		print("error: la variable ya ah sido declarada");
	else:
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
	'''p3 : p2'''

def p_p31(p):
	'''p3 : bloque'''
	#print "p2"

########################CONTENIDO DE UN BLOQUE######################################


def p_bloque(p):
	'''bloque : LKEY b2'''
	print "bloque"

def p_bloque1(p):
	'''bloque : LKEY b3'''
	print "bloque"

def p_b2(p):
	'''b2 : estatuto b3'''
	#print "b2"

def p_b21(p):
	'''b2 : estatuto b2'''
	#print "b2"

def p_b3(p):
	'''b3 : RKEY'''
	#print "b3"

###########################CONTENIDO DE UNA EXPRESION#################################
def p_expresion(p):
	'''expresion : e2'''
	print "expresion"

def p_expresion1(p):
	'''expresion : e2 e3 e2'''
	print "expresion"

def p_e2(p):
	'''e2 : exp'''
	#print "e2"

def p_e3(p):
	'''e3 : LT'''	
	#print "e3"

def p_e31(p):
	'''e3 : GT'''	
	#print "e3"

def p_e32(p):
	'''e3 : LT GT'''	
	#print "e3"
##################EXP###################################
def p_exp(p):
	'''exp : termino'''
	print "exp"
	
def p_exp1(p):
	'''exp : exp ex2 exp'''
	print "exp"

def p_ex2(p):
	'''ex2 : SUMA'''
	#print "ex2"

def p_ex21(p):
	'''ex2 : RESTA'''
	#print "ex2"
####################GENERAR TABLAS####################################

def p_creartabla(p):	
	print "Nombre de la variable: " + p[2]
	print "Se ha creado la tabla de variables"

####################DECLARACION DE VARIABLES#############################
def p_declaracion(p):
	'''declaracion : tipo ID PUNTOCOMA'''
	p_creartabla(p)
	AddGlobalVariable(p[1],p[2])
	print "declaracion"
######################TIPO DE VARIABLES######################################
def p_tipo(p):
	'''tipo : INT'''
	print "tipo"

def p_tipo1(p):
	'''tipo : FLOAT'''
	print "tipo"

def p_tipo2(p):
	'''tipo : CHAR'''
	print "tipo"

def p_tipo3(p):
	'''tipo : STRING'''
	print "tipo"

def p_tipo4(p):
	'''tipo : BOOL'''
	print "tipo"
##################ASIGNACION A VARIABLES###################################
def p_asignacion(p):
	'''asignacion : ID IGUAL expresion PUNTOCOMA'''
	print "asignacion"
#########################ESCRITURA####################################
def p_print(p):
	'''print : PRINT LPARENT es2'''
	print "esritura"

def p_es2(p):
	'''es2 : expresion es3'''
	#print "es2"

def p_es21(p):
	'''es2 : varstring es3'''
	#print "es2"

def p_es3(p):
	'''es3 : es2'''
	#print "es3"

def p_es31(p):
	'''es3 : RPARENT PUNTOCOMA'''
	#print "es3"
######################CONDICION###############################
def p_condicion(p):	
	'''condicion : IF LKEY expresion RKEY bloque c2'''
	print "condicion"

def p_c2(p):
	'''c2 : ELSE bloque PUNTOCOMA'''
	#print "c2"
	
def p_c21(p):
	'''c2 : PUNTOCOMA'''
	#print "c2"

########################TERMINO#################################
def p_termino(p):
	'''termino : factor'''
	print "termino"

def p_termino1(p):
	'''termino : factor t2'''
	print "termino"

def p_t2(p):
	'''t2 : MULT termino'''
	#print "t2"

def p_t21(p):
	'''t2 : DIV termino'''
	#print "t2"
######################FACTOR####################################
def p_factor(p):
	'''factor : LKEY expresion RKEY'''
	print "factor"

def p_factor1(p):
	'''factor : f2'''
	print "factor"
	
def p_f2(p):
	'''f2 : SUMA varcte'''
	#print "f2"

def p_f21(p):
	'''f2 : RESTA varcte'''
	#print "f2"

def p_f22(p):
	'''f2 : varcte'''
	#print "f2"
######################CONTENIDO DE UN ESTATUTO##################################

def p_estatuto(p):
	'''estatuto : asignacion'''
	print "estatuto"

def p_estatuto1(p):
	'''estatuto : print'''
	print "estatuto"

def p_estatuto2(p):
	'''estatuto : condicion'''
	print "estatuto"

def p_estatuto3(p):
	'''estatuto : ciclowhile'''
	print "estatuto"

def p_estatuto4(p):
	'''estatuto : ciclodowhile'''
	print "estatuto"

def p_estatuto5(p):
	'''estatuto : ciclofor'''
	print "estatuto"

def p_estatuto6(p):
	'''estatuto : read'''
	print "estatuto"

def p_estatuto7(p):
	'''estatuto : declaracion'''
	print "estatuto"

def p_estatuto8(p):
	'''estatuto : comentario'''
	print "estatuto"

def p_estatuto9(p):
	'''estatuto : potencia'''
	print "estatuto"

def p_estatuto10(p):
	'''estatuto : raiz'''
	print "estatuto"
#####################COMENTARIO######################################

def p_comentatio(p):
	'''comentario : COMENTARIO'''
	print "Comentario"

######################VARIABLE CONSTANTE#####################################

def p_varcte(p):
	'''varcte : ID'''
	print "varcte"

def p_varcte1(p):
	'''varcte : ENTERO'''
	print "varcte"

def p_varcte2(p):
	'''varcte : FLOTANTE'''
	print "varcte"

def p_varstring(p):
	'''varstring : CADENA'''
	print "varstring"

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

def p_potencia(p):
	'''potencia : POW LPARENT varcte COMA varcte RPARENT PUNTOCOMA'''
	print "potencia"

def p_raiz(p):
	'''raiz : SQRT LPARENT varcte RPARENT PUNTOCOMA'''
	print "raiz"
###################ERROR#####################################

def p_error(p):
	print "error de sintaxis", p
	print "error en la linea" +str(p.lineno)

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

print result

