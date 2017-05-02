program caso7: 
	int iterm1;
	int iterm2;
	int ifibo;
	int icontadorfibo;
function int fibonacci(int in){ 
	int itemp;
	int itemp2;

    if (in<2){
    	return in;}
    else{
    	itemp2=fibonacci(in- 2);;
        return fibonacci(in - 1); + itemp2;}
   }
{
int inum;
int ires;
int icont;
inum=0;
ires=0;
    print("Cuantas veces quieres hacer el ciclo de fibonacci de manera recursia?");
    inum=readint();
    print("NUMEROS DE FIBONACCI");
    fibonacci(inum);
   for(icont=1; icont<=inum icont=icont+1;)
   {
      ires = fibonacci(icont);;
      print(ires);
    }
iterm1=0;
iterm2=1;
inum=1;
icontadorfibo=1;
print("Hasta que numero quieres calcular fibonaci ciclico");
ifibo=readint();
print("FIBONACCI CICLICLO");
	while(inum<ifibo){
		print(inum);
        inum = iterm1 + iterm2;
        iterm1 = iterm2;
        iterm2 = inum;
        icontadorfibo = icontadorfibo+1;
    }


}