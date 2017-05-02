program caso2:{
	int ix;
	int iy;
	//Aqui entraremos al if e ignorara el else--------------------------------------
	ix=1;
	if (ix<2){
		print("El valor de ix es menor a 2");
	}else{
		print("El valor de ix no es menor a 2");
	}
	//--------------------------------------------------------------------------------

	//Aqui entraremos al else e ignorara el if----------------------------------------
	ix=ix+3;
	if (ix<2){
		print("El valor de ix es menor a 2");
	}else{
		print("El valor de ix no es menor a 2");
	}
	//--------------------------------------------------------------------------------

	//Este ciclo se ejecutara 5 veces------------------------------------------------
	ix=0;
	while(ix < 5){
		print("El valor de ix " + ix + " es menor a 5" );
		ix=ix+1;
	}
	//--------------------------------------------------------------------------------

	//Este ciclo de ejecutara una vez debido a que es un do while---------------------
	iy=1;
	do{
		print("El valor de iy es menor a 1");
	}while(iy<1);
	//---------------------------------------------------------------------------------


	//Ciclo for que se ejecutara 5 veces----------------------------------------------
	for(iy=0; iy<5 iy=iy+1;){
		print("Estamos dentro del for, el valor de iy es: "+ iy);
	}
	//---------------------------------------------------------------------------------
}