program caso6:
function int factorial(int ix){
	if (ix==1){
		return 1;
	}else{
		return ix*factorial(ix - 1);;
	}
}

{
int ir;
int ifact;
int itemp;
ir=1;
print("De que numero quieres calcular el factorial ciclicamente?");
itemp=readint();
ifact=itemp;
	while(itemp >= 1){
	ir=ir*itemp;
	itemp=itemp - 1;
	}
print("El factorial de " + ifact + " es: " + ir);

print("De que numero quieres calcular el factorial recursivamente?");
itemp=readint();
print ("El factorial de " + itemp + " es: " + factorial(itemp););


}