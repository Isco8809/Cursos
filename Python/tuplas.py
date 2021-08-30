import requests as rq

url= 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
apiKey = 'b1bc1067-1001-4842-a6c8-f82d1dba7d25'
headers = {  'Accepts': 'application/json',  
           'X-CMC_PRO_API_KEY':  apiKey}
data = rq.get(url,headers=headers).json()

moneda=[]
for valores in data['data']:
    moneda.append(valores['name'])

tuplaMoneda = tuple(moneda)
tuplaMoneda1 = tuple(moneda)

Nombre=input("Ingrese el nombre de la criptomoneda a buscar")

def criptomoneda(Nombre):
    return Nombre in tuplaMoneda
print(max(tuplaMoneda))

if criptomoneda(Nombre):
    print("La criptomoneda ingresada es valida")
else:
    print("La criptomoneda no es valida")