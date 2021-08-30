#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	float Base,Altura, Base1, trapecio;
	
	
	cout << "FIGURAS GEOMETRICAS"<< endl;
	cout << "PARA EL AREA DEL TRAPECIO INGRESE LOS SIGUIENTES DATOS  " << endl << endl;
	cout<<"VALOR BASE: "<< endl;
	cin>>Base;
	cout<<"VALOR ALTURA: "<< endl;
	cin>>Altura;
	cout<<"VALOR DE BASE 2: "<< endl;
	cin>>Base1;
	system("cls");
	
	trapecio = ((Base * Base1)/2)*Altura;
	
	cout << "EL AREA PARA EL TRAPECIO ES: "<< endl;
	cout<< trapecio << endl;
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
