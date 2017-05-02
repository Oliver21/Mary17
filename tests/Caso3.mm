program caso3:
//declaramos la funcion cuadrado pasando valor como parametro y declarando variables dentro de la funcion
function int cuadradoo(int ia){
	int ib;
	ib=ia*ia;
	return ib;
}

//declaramos la funcion cubo sin declaraciones de variables dentro de ella
function int cuboo(int ia){
	return ia*ia*ia;
}

{
int ix;
ix=3;
print("El cuadrado del numero " + ix + " es: " + cuadradoo(ix););
print("El cubo del numero " + ix + " es: " + cuboo(ix););
	
}