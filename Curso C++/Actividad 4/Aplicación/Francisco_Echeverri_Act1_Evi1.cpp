#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	int numero, resultado=1,num=1;
	
	while(num<10)
	{
		cout << "Tabla del : " << num << endl;
		num++;
	}
	
	cout << endl;
	cout << "Seleccione una tabla de multiplicacion: " ;
	cin>>numero;
	
	if(numero > 0 && numero < 9){
		for(int x = 1; x < 10 ;x++)
	{
		resultado = x * numero ;
		cout << numero << " x " << x << " = " << resultado << endl;
	}
	}else{
		cout<<"El numero digitado no es una de las opciones para calcular la tabla de multiplicar."<< endl;
	}
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
