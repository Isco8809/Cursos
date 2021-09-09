import json

with open('Python\BD_Usuarios.json') as js:
    consulta = json.load(js)
    js.close()
    print(consulta)
