import json
from ClaseProyectoFinalPython import usuario

datos = usuario()
metodo = datos.balanceGeneral()
print(metodo)

# opcion = 0
# while opcion != 6:
#     opcion = int(input("\n 1.Recibir cantidad: \n 2.Transferir monto: \n 3.Mostrar balance una moneda: \n 4.Mostrar balance general: \n 5.Mostrar histórico de transacciones: \n 6.Salir del programa \n"))
#     if opcion == 1:
#         datos.validarMoneda()
#         datos.validarCodigo()
#         datos.guardarCriptomoneda()
#         datos.guardarTransaccion("Recibir")
#     elif opcion == 2 :
#         datos.criptomonedaUsuarioTransferir()
#         datos.validarMontoPosible()
#         datos.restarMonto()
#         datos.guardarTransaccion("Transferir")
#     elif opcion == 3:
#         moneda = datos.validarMoneda()
#         print(f"La moneda {moneda}: el cual tiene un costo actual de : {datos.montoCriptoActual()}, y cuenta con una cantidad de : {datos.cantidadCriptoBilletera()} para un total de {datos.montoBilletera()}")