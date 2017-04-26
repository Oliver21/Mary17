program polaco:

FUNCTION int funcionprueba (int iparametro1, string sparametro2, char cparametro3){
		float fflotante;	
		int ifuncion;
		print ("Aqui esta adentro de la funcionprueba");
		ifuncion= 8 + 3;
		ifuncion = ifuncion + iparametro1;
		print ("El parametro 1 recibido es: " + iparametro1);
		print("El parametro 2 recibido es: " + sparametro2);
		print ("El parametro 3 recibido es: " + cparametro3);
		print (ifuncion);
		print ("Aqui termina la funcionprueba");
		//return 5;
	}

FUNCTION int funcionprueba2 (int ix){
	int ia;
	print ("Aqui esta adentro de la funcionprueba2");
	print ("El parametro 1 recibido es: " + ix);
	ia=ix;
	funcionprueba(ia, "paramtro22", "p");
	funcionprueba(50, "paramtro22", "z");
	print (ia);
	print ("Aqui esta termina la funcionprueba2");
}

FUNCTION int frecursiva (int contador){
	int iconta;
	iconta=contador;
	print ("Este es el contador" + iconta);
	iconta=iconta+1;
	if (iconta!=10){
		frecursiva(iconta);
		if (1<2){
			int im;
			im=iconta;
			print (im);
		}
	}
}
{	float ia;
	int ib;
	float ik;
	string ic;
	string id;
	string ie;
	string iresultado;
	string sentrada;
	int icontador;
	int icontador2;
	int icontadorfibo;
	int iterm1;
	int iterm2;
	int fibonaci;
	int iposx;
	int iposy;
	bool bol;
	bool sderecha;
	bool sizquierda;
	bool iderecha;
	bool iizquierda;
	bool bnoentro;
	int ifo;
	string snombre;
	bol = 6!=6;
	ib = 7;
	ia=1;
	//return 10;
	ia = 4.3 * ib + 7 + 8 * 2 / 3 + 1 * 5 * (5 + 1 + 5 - 3) + 1;
	ic = "hola";
	id = "diego";
	ie = ic + id;
	print(ia);
	//ic = "Ya funciona el programa!!!. Genial";
	print (ie + 7);
	//funcionprueba(5*2, "parametro2", "a");
	//funcionprueba2(9);
	frecursiva(1);
	print(bol);
	if (1 < 4){
		print ("el primer valor es menor al segundo, si entro al if");
		} 
	else {
		print ("el primer valor no es menor al segundo, no entro al if");
	}
	icontador=0;
	while(icontador<5){
		print("El contador exterior es: " + icontador);
		icontador2=0;
		while(icontador2<5){
			print("El contador interior es: " + icontador2);
			if(icontador ==2 && icontador2==2){
				print("El valor de ambos contadores es 2");
			}
			icontador2 = icontador2+1;
		}
		icontador = icontador+1;
	}
	for (ifo = 0; ifo<10 ifo=ifo+1;){
		int ifo;
		for(ifo = 0; ifo<2 ifo=ifo+1;){
				print ("Esta es la " + ifo + " vez que entra al for");
		}
	}
	///////////////funciones especiales/////////////
	//cubo(-90,-30, 100);
	//cuadrado(0,0,30);
	//triangulo(0,0,100);
	//levanta();
	//mueve(-100,-100);
	//apoya();
	//mueve(200,100);
	///////////////////////////////////////////////
	ijuanchutero = 3;
	print("Cual es tu nombre");
	snombre=read();
	iposx=0;
	iposy=0;
	bnoentro=true;
	iderecha=false;
	iizquierda=false;
	sderecha=true;
	sizquierda=false;
	icontadorfibo=1;
	iterm1=0;
	iterm2=1;
	fibonaci=1;
	print("AQUI VA FIBBONACI");
	
	while(fibonaci<55){
		if(sderecha && bnoentro){
			iposx=iposx-fibonaci;
			iposy=iposy-fibonaci;
			mueve(iposx*10,iposy*10);
			bnoentro=false;
			sderecha=false;
			sizquierda=true;
		}
		if(sizquierda && bnoentro){
			iposx=iposx+fibonaci;
			iposy=iposy-fibonaci;
			mueve(iposx*10,iposy*10);
			bnoentro=false;
			sizquierda=false;
			iizquierda=true;
		}
		if(iderecha && bnoentro){
			iposx=iposx-fibonaci;
			iposy=iposy+fibonaci;
			mueve(iposx*10,iposy*10);
			bnoentro=false;
			iderecha=false;
			sderecha=true;
		}
		if(iizquierda && bnoentro){
			iposx=iposx+fibonaci;
			iposy=iposy+fibonaci;
			mueve(iposx*10,iposy*10);
			bnoentro=false;
			iizquierda=false;
			iderecha=true;
		}		
		bnoentro=true;
		print(fibonaci);
        fibonaci = iterm1 + iterm2;
        iterm1 = iterm2;
        iterm2 = fibonaci;
        icontadorfibo = icontadorfibo+1;
    }
    print("tu nombre es: "+ snombre);	
}
