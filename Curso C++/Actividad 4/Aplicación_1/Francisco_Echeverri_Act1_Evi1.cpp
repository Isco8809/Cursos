#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	string referencia,Descripcion,letra;
	int talla,cantidad;
	float costo, precio,utilidad,utilidadTotal,PrecioTotal,CostoTotal,PorcentajeUtilidad;
	
	cout << "Desea registrar un Zapato s/n: ";
	cin>>letra;	
	
	while(letra !="n")
	{
	cout << "Digite la referencia del zapato: ";
	cin>>referencia;
	cout<<"Digite una descripcion del zapato: ";
	cin>>Descripcion;
	cout<<"Digite la talla: ";
	cin>>talla;		
	cout<<"Digite el costo por unidad del zapato: ";
	cin>>costo;	
	cout << "Desea registrar OTRO Zapato s/n: ";
	cin>>letra;	
	}
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
