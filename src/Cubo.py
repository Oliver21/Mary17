#int int
#int float
#int char
#int string
#int bool
#float int
#float float
#float char
#float string
#float bool
#char int
#char float
#char char
#char string
#char bool
#string int
#string float
#string char
#string string
#string bool
#bool int
#bool float
#bool char
#bool string
#bool bool
#           +         -         *        /       &&       ||       <        >        <=       >=       !=       ==       =
cubo =  [['INT',   'INT',    'INT',   'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'INT'],  #INT INT
	['FLOAT',  'FLOAT',  'FLOAT', 'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'INT'],  #INT FLOAT
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#INT CHAR
	['STRING',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#INT STR
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#INT BOOL
	['FLOAT',  'FLOAT',  'FLOAT', 'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'FLOAT'],#FLOAT INT
	['FLOAT',  'FLOAT',  'FLOAT', 'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'FLOAT'],#FLOAT FLO
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#FLO CHAR
	['STRING', 'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#FLO STR
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#FLO BOOL
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#CHAR INT
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#CHAR FLO
	['STRING', 'CHAR',   'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'CHAR'], #CHAR CHAR
	['STRING', 'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'ERROR'],#CHAR STR
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#CHAR BOOL
	['STRING', 'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#STR INT
	['STRING', 'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#STR FLO
	['STRING', 'STRING', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'STRING'],#STR CHAR
	['STRING', 'STRING', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'STRING'],#STR STR
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#STR BOOL
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#BOOL INT
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#BOOL FLO
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#BOOL CHA
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],#BOOL STR
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'BOOL',  'BOOL',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL'],]#BOOL BOOL
	
# 0-INT  1-FLOAT  2-CHAR  3-STRING  4-BOOL
#  0+      1-     2*     3/     4&&     5||    6<     7>    8<=   9>=    10<>     11==    12=	
#print "AQUI VA EL CUBO"
#var1 = 3 #STRING 
#var2 = 2 #CHAR



def revisaVariable(var1):
	if var1 == "INT":
		var1 = 0
	elif var1 == "FLOAT":
		var1= 1
	elif var1 == "CHAR":
		var1= 2
	elif var1 == "STRING":
		var1= 3
	elif var1 == "BOOL":
		var1= 4
	return var1
	
def revisaOperador(op):
	if op == "+":
		op = 0
	elif op == "-":
		op = 1
	elif op == "*":
		op = 2
	elif op == "/":
		op = 3
	elif op == "&&":
		op = 4
	elif op == "||":
		op = 5
	elif op == "<":
		op = 6
	elif op == ">":
		op = 7
	elif op == "<=":
		op = 8
	elif op == ">=":
		op = 9
	elif op == "!=":
		op = 10
	elif op == "==":
		op = 11
	elif op == "=":
		op = 12
	return op
	
	
#realizamos la validacion de los tipos de los argumentos enviados junto con el operador, para saber si es posible realizar cierta operacion
#y regresamos el tipo de dato que se generara de dicha combinacion, en caso de ser error, regresamos la palabra error	
def validacion (var1, var2, operador):
	var1 = revisaVariable(var1)
	var2 = revisaVariable(var2)
	operador = revisaOperador(operador)
	#se realizan estos calculos para llegar al renglon necesario dependiendo de los tipos de datos		
	renglon = var1 * 5 + var2
	columna = operador
	return cubo[renglon][columna]



