import json
#from ClaseProyectoFinalPython import usuario

with open('Python\BD_Usuarios.json') as js:
    consulta = json.load(js)
    js.close()
    print(consulta)
    
name = input()

for a in consulta['Usuarios']:
    if name in str(a['Codigo']):
        print(a['Nombre'])
        pass