import json, datetime
import requests
#Se crea la clase que se encarga de consultar los datos del usuario (codigo, criptmonedas y cantidad)
class usuario():
    def __init__(self):
        self.codigo= self.codigoUsuario()
        self.moneda=""
        self.cantidad=0

#En este metodo creamos la conexión al json, que tiene la informació de los usuarios, se lee los datos
    def consultarBDUsuarios(self):
        with open('Python\BD_Usuarios.json') as js:
            consulta = json.load(js)
        return consulta

#En este metodo creamos la conexión al json, que tiene la informació de las criptomonedas, se lee los datos
    def consultarBDCripto(self):
        with open('Python\BD_Criptomoneda.json') as js:
            consulta = json.load(js)
        return consulta

#En este metodo creamos la conexión al json, que tiene la informació de las transacciones, se lee los datos
    def consultarBDTransaccion(self):
        with open('Python\BD_Transaccion.json') as js:
            consulta = json.load(js)
        return consulta

#Verificación de que el usuario ingresado este en el json de los datos para el login
    def codigoUsuario(self):
        verificacion=True
        Datos = self.consultarBDUsuarios()
        usuario = input("Ingrese el codigo de usuario")
        while verificacion:
            for a in Datos['Usuarios']:
                if usuario in str(a['Codigo']):
                    self.codigo = usuario
                    verificacion=False
            if  verificacion:
                usuario = input("El codigo no se encuentra, por favor ingrese el codigo correcto: ")
        return self.codigo

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
        diccionario = {}
        for campos in datos['data']:
            diccionario.setdefault(campos['symbol'],campos['quote']['USD']['price'])
        return diccionario
        
#Lista de criptomonedas que tiene el usuario
    def criptomonedaUsuario(self):
        consulta = self.consultarBDCripto()
        for valor in consulta['Criptomoneda']:
            if self.codigo in str(valor.get('Codigo')):
                return valor.get('Nombre')
        return 0
        
#Validar que la moneda que se ingrese exista!
    def validarMoneda(self):
        valida = True
        while valida:
            moneda = input("Ingrese la moneda: ")
            if moneda in self.listaCriptomonedas().keys():
                valida = False
                self.moneda =moneda
                print("Moneda correcta!") 
            else:
                print("Moneda incorrecta!")
        return self.moneda

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

#valida que la cantidad no sea negativa o igual a cero
    def validarMonto(self):
        self.cantidad = self.validarCantidad()
        while self.cantidad <= 0: 
            print("El monto recibido no puede ser cero o negativo")
            self.cantidad = self.validarCantidad()
        return self.cantidad       

#Creo la conexión para escribir en el archivo, y sumar las monedas que se reciben
    def escribirArchivo(self,data):
        with open("Python\BD_Criptomoneda.json", "w") as jsonFile:
            jsonFile.seek(0)
            json.dump(data, jsonFile, indent=4)
            
    #Creo la conexión para escribir en el archivo, y sumar las monedas que se reciben
    def escribirArchivoTransaccion(self,data):
        with open("Python\BD_Transaccion.json", "w") as jsonFile:
            jsonFile.seek(0)
            json.dump(data, jsonFile, indent=4)
    
#creo que metodo que suma la cantidad de moneda al archivo, primero indico en que posición voy a guardar la cantidad
#averiguo la posición del usuario en la criptomoneda con un contador:
    def sumarCriptomoneda(self,posicion):
        Datos = self.consultarBDCripto()
        cantidadListas=0
        for valores in Datos['Criptomoneda']:
            if self.codigo in str(valores['Codigo']):
                posicionUsuario = cantidadListas
                valor = valores['Cantidad'][posicion] + self.validarMonto()
            cantidadListas+=1
        Datos['Criptomoneda'][posicionUsuario]['Cantidad'][posicion] = valor
        self.escribirArchivo(Datos)   
    
#Con este metodo averiguo si la criptomoneda la tiene el usuario o no, si la tiene le sumo la cantidad a la que tiene, y si no la tiene
#creo el registro con la neuva criptomoneda y la cantidad recibida
    def guardarCriptomoneda(self):
        moneda = self.moneda
        lista = self.criptomonedaUsuario()
        if moneda in lista:
            valor = lista.index(moneda)
            self.sumarCriptomoneda(valor)
        else:print("No hay")
        #valor= lista.append(moneda)

    def guardarTransaccion(self,tipo):
        self.tipo = tipo
        Datos = self.consultarBDTransaccion()
        posicion=0
        fecha = datetime.datetime.now()
        for valores in Datos['Transaccion']:
            if self.codigo in str(valores['Codigo']):
                Datos['Transaccion'][posicion]['Fecha'].append(str(fecha))
                Datos['Transaccion'][posicion]['Tipo'].append(self.tipo)
                Datos['Transaccion'][posicion]['Cantidad'].append(self.cantidad)
                Datos['Transaccion'][posicion]['Moneda'].append(self.moneda)
                Datos['Transaccion'][posicion]['Monto'].append(self.listaCriptomonedas().get(self.moneda))
            posicion+=1
            self.escribirArchivoTransaccion(Datos)   
                