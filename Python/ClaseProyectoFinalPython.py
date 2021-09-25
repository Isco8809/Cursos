import json
import requests
#Se crea la clase que se encarga de consultar los datos del usuario (codigo, criptmonedas y cantidad)
class usuario():
    def __init__(self,codigo):
        self.codigo=codigo
        self.cantidad = self.validarCantidad()

#En este metodo creamos la conexión al json, que tiene la informació de los usuarios, se lee los datos
    def consultarBDUsuarios(self):
        with open('Python\BD_Usuarios.json') as js:
            consulta = json.load(js)
        return consulta

#En este metodo creamos la conexión al json, que tiene la informació de los usuarios, se lee los datos
    def consultarBDCripto(self):
        with open('Python\BD_Criptomoneda.json') as js:
            consulta = json.load(js)
        return consulta

#Verificación de que el usuario ingresado este en el json de los datos para el login
    def codigoUsuario(self):
        verificacion=True
        Datos = self.consultarBDUsuarios()
        while verificacion:
            for a in Datos['Usuarios']:
                if self.codigo in str(a['Codigo']):
                    verificacion=False
            if  verificacion:
                self.codigo = input("El codigo no se encuentra, por favor ingrese el codigo correcto: ")

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
        consulta = self.consultarBDCripto()
        for valor in consulta['Criptomoneda']:
            if self.codigo in str(valor.get('Codigo')):
                moneda = valor['Nombre']
        return moneda
        
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
        with open("Python\BD_Criptomoneda.json", "a") as jsonFile:
            jsonFile.seek(0)
            json.dump(data, jsonFile)
    
    def sumarCriptomoneda(self,posicion):
        datosMoneda = self.consultarBDCripto()
        cantidadInicial = datosMoneda['Criptomoneda']['Nombre'][posicion] 
        cantidadFinal = int(cantidadInicial + self.cantidad)
        
    
    def guardarCriptomoneda(self):
        moneda = self.validarMoneda()
        lista = self.criptomonedaUsuario()
        if moneda in lista:
            valor = lista.index(moneda)
            self.sumarCriptomoneda(valor)
        else:
            print("No hay")
            #valor= lista.append(moneda)
        return valor