import requests

dominio = "https://api.binance.com"

def moneda(Cripto):
    criptomoneda = ['BTC' , 'LTC' , 'BCC' , 'ETH' , 'ETC']
    if Cripto in criptomoneda:
        return True
    else:
        return False
    
def Cant(Cantidad):
    return Cantidad.replace(",","",1).isdigit()

def urlCompleta(url):
    return requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+url+"USDT") 

Nombre=[]
cantidad=[]
Cotizacion=[]

i=0
while i < 3:
    Cripto = input("Ingrese el nombre de la criptomoneda")
    while not moneda(Cripto):
        print("EL nombre de la criptomoneda no es valido!")
        Cripto = input("Ingrese un nombre de criptomoneda correcto")
        
    Nombre.append(Cripto)
    data = urlCompleta(Cripto).json()
    Cotizacion.append(data["price"])
    Canti = input("Ingrese la cantidad de criptomonedas")
    
    while not Cant(Canti):
        print("La cantidad ingresada no es un numero real!")
        Canti = input("Ingrese una cantidad correcta")
    cantidad.append(Canti)
    i=i+1
    
x=0 
acum=0   
while x < 3:
    print(f"La criptomoneda {Nombre[x]} tiene un valor de {Cotizacion[x]} y tiene una cantidad de {cantidad[x]}")
    acum=acum+(float(Cotizacion[x])*float(cantidad[x]))
    x=x+1
    
print(f"En total tiene {acum}")
