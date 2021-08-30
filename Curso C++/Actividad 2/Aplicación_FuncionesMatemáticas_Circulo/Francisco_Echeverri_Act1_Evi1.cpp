#include <iostream>
#include <stdlib.h>
#include <math.h>
using namespace std;
//Definición de la función main
int main ()
{
	float radio,pi=3.1416,circulo;
	
	
	cout << "FIGURAS GEOMETRICAS"<< endl;
	cout << "PARA EL AREA DEL CIRCULO INGRESE LOS SIGUIENTES DATOS  " << endl << endl;
	cout<<"VALOR DEL RADIO: "<< endl;
	cin>>radio;
	system("cls");
	
	circulo = pi * pow(radio,2);
	
	cout << "EL AREA PARA EL CIRCULO ES: "<< endl;
	cout<< circulo << endl;
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
