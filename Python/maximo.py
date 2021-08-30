def Valor():
    valor=""
    while not valor.replace(".","",1).isdigit():
        valor = input("ingrese un valor real valido")
    return valor

def Cantidad():
    cant=""
    while not cant.replace(".","",1).isdigit():
        cant = input("Ingrese la cantidad de Criptomonedas")
    return cant

def cripto(nombre):
    criptomoneda = ["BTC", "BCC", "LTC", "ETH", "ETC", "XRP"]
    ValorTotal, CantidadTotal = 0 , 0
    while nombre not in criptomoneda:
        nombre = input("Ingrese un nombre valido de la criptomoneda")
    ValorTotal = Valor()
    CantidadTotal = Cantidad()
    return ValorTotal , CantidadTotal

a=0
var=0
Monto = 0
Cantidades = 0
while a < 3:
    NOmbre=input("Ingrese el nombre de la cripto")
    Datos=cripto(NOmbre)
    Monto = Monto + float(Datos[var])
    Cantidades = Cantidades + float(Datos[var+1])
    a=a+1

print(f"La cantidad de criptomones acumuladas es de {Cantidades} con un monto total de {Monto}")