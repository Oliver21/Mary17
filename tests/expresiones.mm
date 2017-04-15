program polaco:
int funcionprueba (int iparametro1, string sparametro2, char cparametro3){
		float fflotante;	
		int ifuncion;
		ifuncion= 8 + 3;
		print ("Aqui esta adentro de la funcion");
	}

{	float ia;
	int ib;
	float ik;
	string ic;
	string id;
	string ie;
	string iresultado;
	int icontador;
	int icontador2;
	bool bol;
	bol = 5!=6;
	ib = 7;
	ia=1;
	ia = 4.3 * ib + 7 + 8 * 2 / 3 + 1 * 5 * (5 + 1 + 5 - 3) + 1;
	ic = "hola";
	id = "diego";
	ie = ic + id;
	print(ia);
	//ic = "Ya funciona el programa!!!. Genial";
	print (ie + 7);
	print(bol);
	if (1 < 4){
	print ("el primer valor es menor al segundo, si entro al if");
	} else {
	print ("el primer valor no es menor al segundo, no entro al if");
	}
	icontador=0;
	while(icontador<5){
	print("El contador exterior es: " + icontador);
	icontador2=0;
	while(icontador2<5){
	print("El contador interior es: " + icontador2);
	if(icontador ==2 &&
	 icontador2==2){
	print("Alguno de los contadores es 2");
	}
	icontador2 = icontador2+1;
	}
	icontador = icontador+1;
	}
	cuadrado(-90,-30, 50);
	triangulo(0,0,100);
	mueve(-100,-100);
	read();
		
}
