#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	float Diagonal1,Diagonal2,rombo;
	
	
	cout << "FIGURAS GEOMETRICAS"<< endl;
	cout << "PARA EL AREA DEL ROMBO INGRESE LOS SIGUIENTES DATOS  " << endl << endl;
	cout<<"VALOR DE DIAGONAL 1: "<< endl;
	cin>>Diagonal1;
	cout<<"VALOR DE DIAGONAL 2: "<< endl;
	cin>>Diagonal2;
	system("cls");
	
	rombo = (Diagonal1 * Diagonal2)/2;
	
	cout << "EL AREA PARA EL ROMBO ES: "<< endl;
	cout<< rombo << endl;
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
