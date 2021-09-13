import json
from ClaseProyectoFinalPython import usuario

x = input()
metodo = usuario(x)
respuesta = metodo.criptomonedaUsuario()
print(respuesta)