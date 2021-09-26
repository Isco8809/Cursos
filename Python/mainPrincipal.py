import json
from ClaseProyectoFinalPython import usuario

x = input("Ingrese el codigo de usuario")
datos = usuario(x)
metodo = datos.guardarCriptomoneda()
print(metodo)

# opcion = 0
# while opcion != 6:
#     opcion = int(input("\n 1.Recibir cantidad: \n 2.Transferir monto: \n 3.Mostrar balance una moneda: \n 4.Mostrar balance general: \n 5.Mostrar histórico de transacciones: \n 6.Salir del programa \n"))
#     if opcion == 1:
#         moneda = datos.validarMoneda()
#         cantidad = datos.validarCantidad()
#         codigo = datos.validarCodigo()
        