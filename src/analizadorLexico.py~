#MARY17
#Oliver Alejandro Martinez Quiroz A01280416
#Diego Alejandro Mayorga Morales A00813211

import ply.lex as lex
import re
import codecs
import os
import sys


#tokens = ['ID', 'MULT', 'DIV', 'SUMA', 'RESTA', 'LPARENT', 'RPARENT', 'COMA',
#'PUNTOCOMA', 'DOSPUNTOS', 'PUNTO', 'LBRACKET', 'RBRACKET', 'LKEY', 'RKEY', 'IGUAL', 'LT', 'GT',
#'COMSIMPLE', 'COMDOBLE', 'ENTERO', 'FLOTANTE', 'CARACTER', 'CADENA'
#	]

reservadas = ['INT','FLOAT','IF','ELSE','VAR','PRINT','PROGRAM', 'DO', 'WHILE', 'CHAR', 'STRING', 'BEGIN', 'END', 'FOR', 'FUNCTION', 'BOOL', 'READ', 'POW', 'SQRT', 'CUADRADO', 'TRIANGULO', 'RECTANGULO', 'CASA', 'TRAPECIO', 'ESTRELLA', 'CIRCULO', 'LEVANTA',
'APOYA', 'CUBO', 'MUEVE', 'DIMENSION', 'VOID']

#reservadas = {
#	'begin':'BEGIN',
#	'end':'END',
#	'if':'IF',
#	'else':'ELSE',
#	'while':'WHILE',
#	'do':'DO',
#	'for':'FOR',
#	'print':'PRINT',
#	'int':'INT',
#	'float':'FLOAT',
#	'char':'CHAR',
#	'string':'STRING'
#}

#tokens = tokens+list(reservadas.values())
#reservadas = list(reservadas.values())

tokens = reservadas + ['ID', 'MULT', 'DIV', 'SUMA', 'RESTA', 'LPARENT', 'RPARENT', 'COMA',
'PUNTOCOMA', 'DOSPUNTOS', 'PUNTO', 'LBRACKET', 'RBRACKET', 'LKEY', 'RKEY', 'IGUAL', 'LT', 'GT',
'COMSIMPLE', 'COMDOBLE', 'ENTERO', 'FLOTANTE', 'CARACTER', 'CADENA', 'NOESNADA', 'COMENTARIO', 'BOLEANO',
'RAIZ', 'POTENCIA'	
	]

t_ignore = '\t'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMA = r'\,'
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r'\:'
t_PUNTO = r'\.'
t_IGUAL = r'\='
t_LT = r'<'
t_GT = r'>'
t_COMSIMPLE = r'\''
t_COMDOBLE = r'\"'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'


def t_ccode_nonspace(t):
	r'\s+'

def t_ID(t):
	r'[i|f|c|s|b|p] [a-zA-Z0-9_]+'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	return t

def t_NOESNADA(t):
	r'[a-zA-Z]+'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
	return t	
	
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMENTARIO(t):
	r'\/\/.*'
	pass

def t_FLOTANTE(t):
	r'[0-9]+([.][0-9]+)'
	t.value = float(t.value)
	return t
	
def t_ENTERO(t):
	r'[\-]?[0-9]+'
	t.value = int(t.value)
	return t

def t_CARACTER(t):
	r'[\"][a-zA-Z][\"]'
	return t
	
def t_CADENA(t):
	r'["]([^"])+["]'
	return t

def t_error(t):
	print "caracter ilegal '%s'" %t.value[0]
	t.lexer.skip(1)


#def buscarPrograma(directorio):
#	ficheros = []
#	numArchivo = ''
#	respuesta = False
#	cont = 1

#	for base, dirs, files in os.walk(directorio):
#		ficheros.append(files)

#	for file in files:
#		print str(cont)+". "+file
#		cont = cont+1

#	while respuesta == False:
#		numArchivo = raw_input('\nNumero del test: ')
#		for file in files:
#			if file == files[int(numArchivo)-1]:
#				respuesta = True
#				break

#	print "Has seleccionado \"%s\" \n" %files[int(numArchivo)-1]
#	return files[int(numArchivo)-1]	


#directorio = '/home/oliver/Escritorio/Compiladores/tests/'
#archivo = buscarPrograma(directorio)
#test = directorio+archivo
#fp = codecs.open(test,"r","utf-8")
#cadena = fp.read()
#fp.close()

analizador=lex.lex()
#analizador.input(cadena)

#while True:
#	tok = analizador.token()
#	if not tok : break
#	print tok



				

	

