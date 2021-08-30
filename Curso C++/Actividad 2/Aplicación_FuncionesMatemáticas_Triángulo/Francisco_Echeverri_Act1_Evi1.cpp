#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	
	float Base, Altura, triangulo;
	
	
	cout << "FIGURAS GEOMETRICAS"<< endl;
	cout << "PARA EL AREA DEL TRIANGULO INGRESE LOS SIGUIENTES DATOS  " << endl << endl;
	cout<<"VALOR BASE: "<< endl;
	cin>>Base;
	cout<<"VALOR ALTURA: "<< endl;
	cin>>Altura;
	system("cls");
	
	triangulo = (Base * Altura)/2;
	
	cout << "EL AREA PARA EL TRINAGULO ES: "<< endl;
	cout<< triangulo << endl;
	
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
