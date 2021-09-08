import json

f  = open('Python\BD_Usuarios.json','r')
content  = f.read()
print(content)
jsondecoded = json.dumps(content)

for entidad in jsondecoded["Nombre"]:
    print(entidad)