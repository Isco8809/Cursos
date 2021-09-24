import json
import requests
#Se crea la clase que se encarga de consultar los datos del usuario (codigo, criptmonedas y cantidad)
class usuario():
    def __init__(self, codigo):
        self.codigo = codigo
        self.moneda = self.validarMoneda()
        self.cantidad = self.validarCantidad()

#En este metodo creamos la conexión al json, que tiene la informació de los usuarios, se lee los datos
    def consultarBD(self):
        with open('Python\BD_Usuarios.json') as js:
            #consulta = json.dumps(js)
            consulta1 = json.loads(js)
            js.close()
        return consulta1

#Verificación de que el usuario ingresado este en el json de los datos para el login
    def codigoUsuario(self):
        verificacion=True
        print("buena")
        Datos = self.consultarBD()
        while verificacion:
            for a in Datos['Usuarios']:
                if self.codigo in str(a['Codigo']):
                    x=a
                    verificacion=False
            if  verificacion:
                self.codigo = input("El codigo no se encuentra, por favor ingrese el codigo correcto: ")
        return x

#Conexión a la página de criptomonedas
    def conexionCriptomonedas(self):
        headers = {  'Accepts': 'application/json',  
                    'X-CMC_PRO_API_KEY':  'b1bc1067-1001-4842-a6c8-f82d1dba7d25'}
        conexion = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
        #conexion = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers).json()
        return conexion

#Creamos una lista de las criptomonedas de la página, para una rápida validación de que existan
    def listaCriptomonedas(self):
        datos = self.conexionCriptomonedas()
        lista=[]
        for campos in datos['data']:
            lista.append(campos['symbol'])
        tuple(lista)
        return lista
        
#Lista de criptomonedas que tiene el usuario
    def criptomonedaUsuario(self):
        datos_usuario = self.codigoUsuario()
        lista = []
        for valor in datos_usuario['Criptomonedas']['Cripto']:
            lista.append(valor)
        return lista
    
#Validar que la moneda que se ingrese exista!
    def validarMoneda(self):
        valida = True
        while valida:
            moneda = input("Ingrese la moneda: ")
            if moneda in self.listaCriptomonedas():
                valida = False
                print("Moneda correcta!") 
            else:
                print("Moneda incorrecta!")
        return moneda

#Se valida que el codigo para recibir moneda sea diferente al que se logueo
    def validarCodigo(self):
        valida = True
        while valida:
            codigo = input("Ingrese el codigo: ")
            if codigo != self.codigo:
                valida = False
                print("Codigo correcto!") 
            else:
                print("El codigo debe ser diferente al tuyo!")
        return codigo

#Validad que el numero ingresado sea un flotante y no un string
    def validarCantidad(self):
        while True:
            try:
                numero = float(input("Ingrese la cantidad: "))
                break
            except ValueError:
                print("El numero ingresado es incorrecto")
        return numero
    
    def escribirArchivo(self,data):
        with open("Python\BD_Usuarios.json", "w") as jsonFile:
            jsonFile.seek(0)
            json.dump(data, jsonFile)
    
    def sumarCriptomoneda(self,posicion):
        datos_usuario = self.codigoUsuario()
        cantidadInicial = datos_usuario['Criptomonedas']['Cantidad'][posicion] 
        cantidadFinal = int(cantidadInicial + self.cantidad)
        Datos = self.consultarBD()
        print("impresión de datos")
        #print(Datos.keys())
        # Datos['Usuarios']['Criptomonedas']['Cantidad'][posicion] = cantidadFinal
        # self.escribirArchivo(Datos)
        # for a in Datos['Usuarios']:
        #         if self.codigo in str(a['Codigo']):
        #             a['Criptomonedas']['Cantidad'][posicion] = cantidadFinal        
        #             archivo = self.escribirArchivo(a)
    
#En este metodo validamos si la moneda ya la tiene el usuario
    def guardarCriptomoneda(self):
        lista = self.criptomonedaUsuario()
        if self.moneda in lista:
            posicion = lista.index(self.moneda)
            cantidad = self.sumarCriptomoneda(posicion)
        else:
            print("No hay")
            #valor= lista.append(moneda)
        return int(posicion)