import json

with open("BD_Usuarios.json") as file:
    JsonObject = json.load(file)
    file.close

Nombre = JsonObject['Nombre']

print(Nombre)