program caso8:{
	int ix;
	int ia[9];
	ia[0]=10;
	ia[1]=4;
	ia[2]=5;
	ia[3]=2;
	ia[4]=24;
	ia[5]=3;
	ia[6]=1234;
	ia[7]=21;
	ia[8]=254;
	ia[9]=232;
	print("Que valor quieres buscar en la variable dimensionada ia[]?");
	ix=readint();
	print("El valor "+ ix + " se encuentra en la posicion " + find(ix).ia[]);
}