
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rigthigualleftLTGTleftSUMARESTAleftMULTDIVleftLBRACKETRBRACKETleftLPARENTRPARENTleftLKEYRKEYINT FLOAT IF ELSE VAR PRINT PROGRAM DO WHILE CHAR STRING BEGIN END FOR FUNCTION BOOL PRINT READ ID MULT DIV SUMA RESTA LPARENT RPARENT COMA PUNTOCOMA DOSPUNTOS PUNTO LBRACKET RBRACKET LKEY RKEY IGUAL LT GT COMSIMPLE COMDOBLE ENTERO FLOTANTE CARACTER CADENA NOESNADA COMENTARIO BOLEANOprogram : PROGRAM ID DOSPUNTOS p2p2 : vars bloquep2 : bloquebloque : LKEY b2bloque : LKEY b3b2 : estatuto b3b2 : estatuto b2b3 : RKEYexpresion : e2expresion : e2 e3 e2e2 : expe3 : LTe3 : GTe3 : LT GTexp : terminoexp : exp ex2 expex2 : SUMAex2 : RESTAvars : tipo ID PUNTOCOMAtipo : INTtipo : FLOATtipo : CHARtipo : STRINGtipo : BOOLasignacion : ID IGUAL expresion PUNTOCOMAescritura : PRINT LKEY es2es2 : expresion es3es2 : CADENA es3es3 : es2es3 : RKEY PUNTOCOMAcondicion : IF LKEY expresion RKEY bloque c2c2 : ELSE bloque PUNTOCOMAc2 : PUNTOCOMAtermino : factortermino : factor t2t2 : MULT terminot2 : DIV terminofactor : LKEY expresion RKEYfactor : f2f2 : SUMA varctef2 : RESTA varctef2 : varcteestatuto : asignacionestatuto : escrituraestatuto : condicionestatuto : ciclowhileestatuto : ciclodowhileestatuto : cicloforestatuto : readestatuto : printestatuto : COMENTARIOvarcte : IDvarcte : ENTEROvarcte : FLOTANTEvarcte : CADENAciclowhile : WHILE LPARENT expresion RPARENT bloqueciclodowhile : DO bloque WHILE LPARENT expresion RPARENT PUNTOCOMAread : ID IGUAL READ LPARENT RPARENT PUNTOCOMAprint : PRINT LPARENT varcte RPARENT PUNTOCOMAciclofor : FOR LPARENT asignacion expresion asignacion RPARENT bloque'
    
_lr_action_items = {'DO':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,41,42,64,85,86,88,92,100,102,103,109,110,112,113,114,116,],[17,-4,-5,-51,17,-46,-45,-50,-49,-8,-48,-47,-43,-44,-7,-6,-26,-27,-29,-28,-25,-56,-59,-30,-58,-33,-31,-57,-60,-32,]),'READ':([44,],[67,]),'IGUAL':([32,66,],[44,90,]),'CHAR':([4,],[11,]),'WHILE':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,37,41,42,64,85,86,88,92,100,102,103,109,110,112,113,114,116,],[18,-4,-5,-51,18,-46,-45,-50,-49,-8,-48,-47,-43,-44,46,-7,-6,-26,-27,-29,-28,-25,-56,-59,-30,-58,-33,-31,-57,-60,-32,]),'PROGRAM':([0,],[1,]),'PRINT':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,41,42,64,85,86,88,92,100,102,103,109,110,112,113,114,116,],[21,-4,-5,-51,21,-46,-45,-50,-49,-8,-48,-47,-43,-44,-7,-6,-26,-27,-29,-28,-25,-56,-59,-30,-58,-33,-31,-57,-60,-32,]),'RESTA':([38,40,44,45,47,48,51,52,53,54,55,56,57,59,60,62,63,65,70,71,72,73,74,75,77,78,79,81,82,83,90,92,95,96,97,98,99,101,],[49,49,49,49,-39,-15,-42,-55,-34,-53,49,-52,-9,81,-54,49,49,49,49,-41,-40,49,-35,49,-12,-13,49,-18,49,-17,49,-25,-37,-36,-38,-14,-10,81,]),'COMENTARIO':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,41,42,64,85,86,88,92,100,102,103,109,110,112,113,114,116,],[22,-4,-5,-51,22,-46,-45,-50,-49,-8,-48,-47,-43,-44,-7,-6,-26,-27,-29,-28,-25,-56,-59,-30,-58,-33,-31,-57,-60,-32,]),'SUMA':([38,40,44,45,47,48,51,52,53,54,55,56,57,59,60,62,63,65,70,71,72,73,74,75,77,78,79,81,82,83,90,92,95,96,97,98,99,101,],[50,50,50,50,-39,-15,-42,-55,-34,-53,50,-52,-9,83,-54,50,50,50,50,-41,-40,50,-35,50,-12,-13,50,-18,50,-17,50,-25,-37,-36,-38,-14,-10,83,]),'STRING':([4,],[6,]),'LPARENT':([18,21,27,46,67,],[38,39,43,70,91,]),'PUNTOCOMA':([15,19,20,29,41,42,47,48,51,52,53,54,56,57,59,60,68,71,72,74,84,87,95,96,97,99,101,105,106,107,115,],[36,-4,-5,-8,-7,-6,-39,-15,-42,-55,-34,-53,-52,-9,-11,-54,92,-41,-40,-35,102,103,-37,-36,-38,-10,-16,109,110,113,116,]),'LT':([47,48,51,52,53,54,56,57,59,60,63,71,72,74,95,96,97,101,],[-39,-15,-42,-55,-34,-53,-52,77,-11,-54,-55,-41,-40,-35,-37,-36,-38,-16,]),'CADENA':([38,39,40,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,65,70,71,72,73,74,75,77,78,79,81,82,83,90,92,95,96,97,98,99,101,],[52,52,63,52,52,-39,-15,52,52,-42,-55,-34,-53,52,-52,-9,-11,-54,63,63,52,52,-41,-40,52,-35,52,-12,-13,52,-18,52,-17,52,-25,-37,-36,-38,-14,-10,-16,]),'DOSPUNTOS':([3,],[4,]),'RPARENT':([47,48,51,52,53,54,56,57,58,59,60,61,71,72,74,91,92,94,95,96,97,99,101,104,],[-39,-15,-42,-55,-34,-53,-52,-9,80,-11,-54,84,-41,-40,-35,105,-25,107,-37,-36,-38,-10,-16,108,]),'$end':([2,5,13,16,19,20,29,41,42,],[0,-1,-3,-2,-4,-5,-8,-7,-6,]),'GT':([47,48,51,52,53,54,56,57,59,60,63,71,72,74,77,95,96,97,101,],[-39,-15,-42,-55,-34,-53,-52,78,-11,-54,-55,-41,-40,-35,98,-37,-36,-38,-16,]),'LKEY':([4,8,17,21,33,36,38,40,44,45,47,48,51,52,53,54,55,56,57,59,60,62,63,65,70,71,72,73,74,75,77,78,79,80,81,82,83,90,92,93,95,96,97,98,99,101,108,111,],[14,14,14,40,45,-19,55,55,55,55,-39,-15,-42,-55,-34,-53,55,-52,-9,-11,-54,55,55,55,55,-41,-40,55,-35,55,-12,-13,55,14,-18,55,-17,55,-25,14,-37,-36,-38,-14,-10,-16,14,14,]),'FOR':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,41,42,64,85,86,88,92,100,102,103,109,110,112,113,114,116,],[27,-4,-5,-51,27,-46,-45,-50,-49,-8,-48,-47,-43,-44,-7,-6,-26,-27,-29,-28,-25,-56,-59,-30,-58,-33,-31,-57,-60,-32,]),'RKEY':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,41,42,47,48,51,52,53,54,56,57,59,60,62,63,64,69,71,72,74,76,85,86,88,92,95,96,97,99,100,101,102,103,109,110,112,113,114,116,],[29,-4,-5,-51,29,-46,-45,-50,-49,-8,-48,-47,-43,-44,-7,-6,-39,-15,-42,-55,-34,-53,-52,-9,-11,-54,87,87,-26,93,-41,-40,-35,97,-27,-29,-28,-25,-37,-36,-38,-10,-56,-16,-59,-30,-58,-33,-31,-57,-60,-32,]),'ELSE':([19,20,29,41,42,106,],[-4,-5,-8,-7,-6,111,]),'ID':([1,6,7,9,10,11,12,14,19,20,22,23,24,25,26,28,29,30,31,34,35,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,64,65,70,71,72,73,74,75,77,78,79,81,82,83,85,86,88,89,90,92,95,96,97,98,99,100,101,102,103,109,110,112,113,114,116,],[3,-23,15,-20,-21,-22,-24,32,-4,-5,-51,32,-46,-45,-50,-49,-8,-48,-47,-43,-44,56,56,56,-7,-6,66,56,56,-39,-15,56,56,-42,-55,-34,-53,56,-52,-9,-11,-54,56,56,-26,56,56,-41,-40,56,-35,56,-12,-13,56,-18,56,-17,-27,-29,-28,66,56,-25,-37,-36,-38,-14,-10,-56,-16,-59,-30,-58,-33,-31,-57,-60,-32,]),'IF':([14,19,20,22,23,24,25,26,28,29,30,31,34,35,41,42,64,85,86,88,92,100,102,103,109,110,112,113,114,116,],[33,-4,-5,-51,33,-46,-45,-50,-49,-8,-48,-47,-43,-44,-7,-6,-26,-27,-29,-28,-25,-56,-59,-30,-58,-33,-31,-57,-60,-32,]),'MULT':([47,51,52,53,54,56,60,63,71,72,97,],[-39,-42,-55,75,-53,-52,-54,-55,-41,-40,-38,]),'INT':([4,],[9,]),'FLOAT':([4,],[10,]),'BOOL':([4,],[12,]),'FLOTANTE':([38,39,40,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,65,70,71,72,73,74,75,77,78,79,81,82,83,90,92,95,96,97,98,99,101,],[60,60,60,60,60,-39,-15,60,60,-42,-55,-34,-53,60,-52,-9,-11,-54,60,60,60,60,-41,-40,60,-35,60,-12,-13,60,-18,60,-17,60,-25,-37,-36,-38,-14,-10,-16,]),'ENTERO':([38,39,40,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,62,63,65,70,71,72,73,74,75,77,78,79,81,82,83,90,92,95,96,97,98,99,101,],[54,54,54,54,54,-39,-15,54,54,-42,-55,-34,-53,54,-52,-9,-11,-54,54,54,54,54,-41,-40,54,-35,54,-12,-13,54,-18,54,-17,54,-25,-37,-36,-38,-14,-10,-16,]),'DIV':([47,51,52,53,54,56,60,63,71,72,97,],[-39,-42,-55,73,-53,-52,-54,-55,-41,-40,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'f2':([38,40,44,45,55,62,63,65,70,73,75,79,82,90,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'vars':([4,],[8,]),'termino':([38,40,44,45,55,62,63,65,70,73,75,79,82,90,],[48,48,48,48,48,48,48,48,48,95,96,48,48,48,]),'b2':([14,23,],[19,41,]),'b3':([14,23,],[20,42,]),'bloque':([4,8,17,80,93,108,111,],[13,16,37,100,106,114,115,]),'ciclowhile':([14,23,],[24,24,]),'varcte':([38,39,40,44,45,49,50,55,62,63,65,70,73,75,79,82,90,],[51,61,51,51,51,71,72,51,51,51,51,51,51,51,51,51,51,]),'tipo':([4,],[7,]),'estatuto':([14,23,],[23,23,]),'program':([0,],[2,]),'ex2':([59,101,],[82,82,]),'factor':([38,40,44,45,55,62,63,65,70,73,75,79,82,90,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'print':([14,23,],[26,26,]),'expresion':([38,40,44,45,55,62,63,65,70,90,],[58,62,68,69,76,62,62,89,94,68,]),'read':([14,23,],[28,28,]),'ciclofor':([14,23,],[30,30,]),'condicion':([14,23,],[25,25,]),'c2':([106,],[112,]),'ciclodowhile':([14,23,],[31,31,]),'e3':([57,],[79,]),'e2':([38,40,44,45,55,62,63,65,70,79,90,],[57,57,57,57,57,57,57,57,57,99,57,]),'p2':([4,],[5,]),'es3':([62,63,],[85,88,]),'es2':([40,62,63,],[64,86,86,]),'asignacion':([14,23,43,89,],[34,34,65,104,]),'t2':([53,],[74,]),'exp':([38,40,44,45,55,62,63,65,70,79,82,90,],[59,59,59,59,59,59,59,59,59,59,101,59,]),'escritura':([14,23,],[35,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID DOSPUNTOS p2','program',4,'p_program','analizadorSintactico.py',23),
  ('p2 -> vars bloque','p2',2,'p_p2','analizadorSintactico.py',28),
  ('p2 -> bloque','p2',1,'p_p21','analizadorSintactico.py',33),
  ('bloque -> LKEY b2','bloque',2,'p_bloque','analizadorSintactico.py',37),
  ('bloque -> LKEY b3','bloque',2,'p_bloque1','analizadorSintactico.py',41),
  ('b2 -> estatuto b3','b2',2,'p_b2','analizadorSintactico.py',45),
  ('b2 -> estatuto b2','b2',2,'p_b21','analizadorSintactico.py',49),
  ('b3 -> RKEY','b3',1,'p_b3','analizadorSintactico.py',53),
  ('expresion -> e2','expresion',1,'p_expresion','analizadorSintactico.py',57),
  ('expresion -> e2 e3 e2','expresion',3,'p_expresion1','analizadorSintactico.py',61),
  ('e2 -> exp','e2',1,'p_e2','analizadorSintactico.py',65),
  ('e3 -> LT','e3',1,'p_e3','analizadorSintactico.py',69),
  ('e3 -> GT','e3',1,'p_e31','analizadorSintactico.py',73),
  ('e3 -> LT GT','e3',2,'p_e32','analizadorSintactico.py',77),
  ('exp -> termino','exp',1,'p_exp','analizadorSintactico.py',81),
  ('exp -> exp ex2 exp','exp',3,'p_exp1','analizadorSintactico.py',85),
  ('ex2 -> SUMA','ex2',1,'p_ex2','analizadorSintactico.py',89),
  ('ex2 -> RESTA','ex2',1,'p_ex21','analizadorSintactico.py',93),
  ('vars -> tipo ID PUNTOCOMA','vars',3,'p_vars','analizadorSintactico.py',97),
  ('tipo -> INT','tipo',1,'p_tipo','analizadorSintactico.py',101),
  ('tipo -> FLOAT','tipo',1,'p_tipo1','analizadorSintactico.py',105),
  ('tipo -> CHAR','tipo',1,'p_tipo2','analizadorSintactico.py',109),
  ('tipo -> STRING','tipo',1,'p_tipo3','analizadorSintactico.py',113),
  ('tipo -> BOOL','tipo',1,'p_tipo4','analizadorSintactico.py',117),
  ('asignacion -> ID IGUAL expresion PUNTOCOMA','asignacion',4,'p_asignacion','analizadorSintactico.py',121),
  ('escritura -> PRINT LKEY es2','escritura',3,'p_escritura','analizadorSintactico.py',125),
  ('es2 -> expresion es3','es2',2,'p_es2','analizadorSintactico.py',129),
  ('es2 -> CADENA es3','es2',2,'p_es21','analizadorSintactico.py',133),
  ('es3 -> es2','es3',1,'p_es3','analizadorSintactico.py',137),
  ('es3 -> RKEY PUNTOCOMA','es3',2,'p_es31','analizadorSintactico.py',141),
  ('condicion -> IF LKEY expresion RKEY bloque c2','condicion',6,'p_condicion','analizadorSintactico.py',145),
  ('c2 -> ELSE bloque PUNTOCOMA','c2',3,'p_c2','analizadorSintactico.py',149),
  ('c2 -> PUNTOCOMA','c2',1,'p_c21','analizadorSintactico.py',153),
  ('termino -> factor','termino',1,'p_termino','analizadorSintactico.py',158),
  ('termino -> factor t2','termino',2,'p_termino1','analizadorSintactico.py',162),
  ('t2 -> MULT termino','t2',2,'p_t2','analizadorSintactico.py',166),
  ('t2 -> DIV termino','t2',2,'p_t21','analizadorSintactico.py',170),
  ('factor -> LKEY expresion RKEY','factor',3,'p_factor','analizadorSintactico.py',174),
  ('factor -> f2','factor',1,'p_factor1','analizadorSintactico.py',178),
  ('f2 -> SUMA varcte','f2',2,'p_f2','analizadorSintactico.py',182),
  ('f2 -> RESTA varcte','f2',2,'p_f21','analizadorSintactico.py',186),
  ('f2 -> varcte','f2',1,'p_f22','analizadorSintactico.py',190),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','analizadorSintactico.py',194),
  ('estatuto -> escritura','estatuto',1,'p_estatuto1','analizadorSintactico.py',198),
  ('estatuto -> condicion','estatuto',1,'p_estatuto2','analizadorSintactico.py',202),
  ('estatuto -> ciclowhile','estatuto',1,'p_estatuto3','analizadorSintactico.py',206),
  ('estatuto -> ciclodowhile','estatuto',1,'p_estatuto4','analizadorSintactico.py',210),
  ('estatuto -> ciclofor','estatuto',1,'p_estatuto5','analizadorSintactico.py',214),
  ('estatuto -> read','estatuto',1,'p_estatuto6','analizadorSintactico.py',218),
  ('estatuto -> print','estatuto',1,'p_estatuto7','analizadorSintactico.py',222),
  ('estatuto -> COMENTARIO','estatuto',1,'p_estatuto8','analizadorSintactico.py',226),
  ('varcte -> ID','varcte',1,'p_varcte','analizadorSintactico.py',230),
  ('varcte -> ENTERO','varcte',1,'p_varcte1','analizadorSintactico.py',234),
  ('varcte -> FLOTANTE','varcte',1,'p_varcte2','analizadorSintactico.py',238),
  ('varcte -> CADENA','varcte',1,'p_varcte3','analizadorSintactico.py',242),
  ('ciclowhile -> WHILE LPARENT expresion RPARENT bloque','ciclowhile',5,'p_ciclowhile','analizadorSintactico.py',246),
  ('ciclodowhile -> DO bloque WHILE LPARENT expresion RPARENT PUNTOCOMA','ciclodowhile',7,'p_ciclodowhile','analizadorSintactico.py',250),
  ('read -> ID IGUAL READ LPARENT RPARENT PUNTOCOMA','read',6,'p_read','analizadorSintactico.py',254),
  ('print -> PRINT LPARENT varcte RPARENT PUNTOCOMA','print',5,'p_print','analizadorSintactico.py',258),
  ('ciclofor -> FOR LPARENT asignacion expresion asignacion RPARENT bloque','ciclofor',7,'p_ciclofor','analizadorSintactico.py',262),
]
