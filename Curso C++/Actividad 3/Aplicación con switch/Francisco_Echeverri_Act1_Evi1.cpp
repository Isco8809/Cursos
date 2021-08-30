#include <iostream>
#include <stdlib.h>

using namespace std;
//Definición de la función main
int main ()
{
	char referencia[40];
	char Descripcion[50], letra;
	string tipo;
	int talla,cantidad,num;
	float costo, precio,utilidad,utilidadTotal,PrecioTotal,CostoTotal,PorcentajeUtilidad;
	
	
	cout << "ADMINISTRAR VENTA DE ZAPATOS"<< endl;
	cout << "Digite la referencia del zapato..." << endl;
	cin.getline(referencia , 40);
	cout<<"Digite una descripcion del zapato..."<< endl;
	cin.getline(Descripcion, 50);
	cout<<"Digite la talla..."<< endl;
	cin>>talla;
	cout<<"Digita la letra si esta disponible o no para la venta S/N..."<< endl;
	cin>>letra;
	cout<<"Digite la cantidad de zapatos..."<< endl;
	cin>>cantidad;
	cout<<"Digite el costo por unidad del zapato..."<< endl;
	cin>>costo;
	cout<<"Digite el precio de venta por unidad del zapato..."<< endl;
	cin>>precio;
	system("cls");
	
	
	CostoTotal = costo * cantidad;
	PrecioTotal = precio * cantidad;
	utilidad = precio - costo;
	utilidadTotal = PrecioTotal - CostoTotal;
	//PorcentajeUtilidad = (utilidadTotal/CostoTotal)*100;
	if(costo <= 30000)
	{
		num = 1;
	} else if(costo <= 60000)
	{
		num = 2;
	}else
	{
		num = 3;
	}
	
	switch(num)
	{
		case 1:
			PorcentajeUtilidad = 50 ;
			tipo = "A";
			break;
		case 2:
			PorcentajeUtilidad = 40 ;
			tipo = "B";
			break;
		case 3:
			PorcentajeUtilidad = 30 ;
			tipo = "C";
			break;
	}
	
	cout << "LOS DATOS REGISTRADOS SON LOS SIGUIENTES"<< endl;
	cout<<"REFERENCIA: "<< referencia << endl;
	cout<<"TIPO: "<< tipo << endl;
	cout<<"DESCRIPCIÓN: "<< Descripcion << endl;
	cout<<"TALLA: "<< talla << endl;
	cout<<"DISPONIBILIDAD: "<< letra << endl;
	cout<<"CANTIDAD DE ZAPATOS: "<< cantidad << endl;
	cout<<"COSTO UNIDAD: "<< costo << endl;
	cout<<"COSTO TOTAL: "<< CostoTotal << endl;
	cout<<"PRECIO UNIDAD: "<< precio << endl;
	cout<<"PRECIO TOTAL DE "<< cantidad << " UNIDADES:" << PrecioTotal << endl;
	cout<<"UTILIDAD POR UNIDAD: "<< utilidad << endl;
	cout<<"UTILIDAD TOTAL: "<< utilidadTotal << endl;
	cout<<"PORCENTAJE DE UTILIDAD: "<< PorcentajeUtilidad << endl;
	
	
	cout<<"Gracias por digitar la informacion "<< endl;
	system("pause");
	
	//Francisco Javier Echverri
	
	return EXIT_SUCCESS;
}
