#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	char referencia[40];
	char Descripcion[50], letra;
	int talla, costo, precio;
	cout << "ADMINISTRAR VENTA DE ZAPATOS"<< endl;
	cout << "Digite la referencia del zapato..." << endl;
	cin.getline(referencia , 40);
	cout<<"Digite una descripcion del zapato..."<< endl;
	cin.getline(Descripcion, 50);
	cout<<"Digite la talla..."<< endl;
	cin>>talla;
	cout<<"Digita la letra si esta disponible o no para la venta S/N..."<< endl;
	cin>>letra;
	cout<<"Digite el costo del zapato..."<< endl;
	cin>>costo;
	cout<<"Digite el precio de venta del zapato..."<< endl;
	cin>>precio;
	system("cls");
	
	cout << "LOS DATOS REGISTRADOS SON LOS SIGUIENTES"<< endl;
	cout<<"REFERENCIA: "<< referencia << endl;
	cout<<"DESCRIPCIÓN: "<< Descripcion << endl;
	cout<<"TALLA: "<< talla << endl;
	cout<<"DISPONIBILIDAD: "<< letra << endl;
	cout<<"COSTO: "<< costo << endl;
	cout<<"PRECIO: "<< precio << endl;
	
	cout<<"Gracias por digitar la información "<< endl;
	system("pause");
	
	return EXIT_SUCCESS;
}
