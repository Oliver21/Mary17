program caso4:{
	int ij;
	int ia[5];
	int ib[2,2,5];
	ia[0]=0;
	ia[3]=3;
	ia[5]=9;
	ib[0,0,0]=0;
	ib[1,2,4]=4;
	print("El valor de ia[0] es: " + ia[0]);
	print("El valor de ia[3] es: " + ia[3]);
	print("El valor de ib[0,0,0] es: " + ib[0,0,0]);
	print("El valor de ib[1,2,4] es: " + ib[1,2,4]);
	print(ia[3] * ib[1,2,4]);
}