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
#           +         -         *        /       &&       ||       <        >        <=       >=       <>       ==       =
cubo =  [['INT',   'INT',    'INT',   'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'INT'],
	['FLOAT',  'FLOAT',  'FLOAT', 'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'INT'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['FLOAT',  'FLOAT',  'FLOAT', 'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'FLOAT'],
	['FLOAT',  'FLOAT',  'FLOAT', 'FLOAT', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'FLOAT'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['STRING', 'CHAR',   'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'CHAR'],
	['STRING', 'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['STRING', 'STRING', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'STRING'],
	['STRING', 'STRING', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'BOOL',  'STRING'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR', 'ERROR'],
	['ERROR',  'ERROR',  'ERROR', 'ERROR', 'BOOL',  'BOOL',  'ERROR', 'ERROR', 'ERROR', 'ERROR', 'BOOL',  'BOOL',  'BOOL'],]
	
# 0-INT  1-FLOAT  2-CHAR  3-STRING  4-BOOL
#  0+      1-     2*     3/     4&&     5||    6<     7>    8<=   9>=    10<>     11==    12=	
#print "AQUI VA EL CUBO"
#var1 = 3 #STRING 
#var2 = 2 #CHAR


#print cubo[((var1*5)+(var2))][1]

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
	elif op == "<>":
		op = 10
	elif op == "==":
		op = 11
	elif op == "=":
		op = 12
	return op
	
	
	
def validacion (var1, var2, operador):
	var1 = revisaVariable(var1)
	var2 = revisaVariable(var2)
	operador = revisaOperador(operador)
		
	renglon = var1 * 5 + var2
	columna = operador
	return cubo[renglon][columna]



