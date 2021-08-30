#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	float Base, Altura, paralelo;
	
	
	cout << "FIGURAS GEOMETRICAS"<< endl;
	cout << "PARA EL AREA DEL PARALELOGRAMO INGRESE LOS SIGUIENTES DATOS  " << endl << endl;
	cout<<"VALOR BASE: "<< endl;
	cin>>Base;
	cout<<"VALOR ALTURA: "<< endl;
	cin>>Altura;
	system("cls");
	
	paralelo = Base *Altura ;
	
	cout << "EL AREA PARA EL PARALELOGRAMO ES: "<< endl;
	cout<< paralelo << endl;
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
