import json
#Se crea la clase que se encarga de consultar los datos del usuario (codigo, criptmonedas y cantidad)
class usuario():
    def __init__(self):
        pass

    def consultarBD(self):
        with open('Python\BD_Usuarios.json') as js:
            consulta = json.load(js)
            js.close()
        return consulta

    def condigoUsuario(self):
        consulta = self.consultarBD()
        for a in consulta['Usuarios'][0]['Criptomonedas'][0]['Cripto']:
            print(a)
        return a