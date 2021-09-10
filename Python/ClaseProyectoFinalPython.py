import json
#Se crea la clase que se encarga de consultar los datos del usuario (codigo, criptmonedas y cantidad)
class usuario():
    def __init__(self, codigo):
        self.codigo = codigo

    def consultarBD(self):
        with open('Python\BD_Usuarios.json') as js:
            consulta = json.load(js)
            js.close()
        return consulta

    def codigoUsuario(self):
        conexion = self.consultarBD()
        
        if self.codigo == conexion['Usuarios']['Criptomonedas']:
            
        for a in otra['Usuarios'][0]['Criptomonedas'][0]['Cripto']:
            print(a)
        return a
    
    # def datosUsuario(self):
        