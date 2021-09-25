import json
from ClaseProyectoFinalPython import usuario

x = input("Ingrese el codigo del usuario: ")
metodo = usuario(x)
respuesta = metodo.criptomonedaUsuario()
print(respuesta)