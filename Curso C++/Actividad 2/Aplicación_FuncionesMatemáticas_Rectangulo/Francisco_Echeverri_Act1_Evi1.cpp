#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
		float Base, Altura, rectangulo;
	
	
	cout << "FIGURAS GEOMETRICAS"<< endl;
	cout << "PARA EL AREA DEL RECTANGULO INGRESE LOS SIGUIENTES DATOS  " << endl << endl;
	cout<<"VALOR BASE: "<< endl;
	cin>>Base;
	cout<<"VALOR ALTURA: "<< endl;
	cin>>Altura;
	system("cls");
	
	rectangulo = Base * Altura;
	
	cout << "EL AREA PARA EL RECTANGULO ES: "<< endl;
	cout<< rectangulo << endl;
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
