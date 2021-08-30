import requests

def valor(Nombre):
  url = 'https://api.binance.com/api/v3/ticker/price?symbol='
  urlConcatenada =  url+Nombre+"USDT"
  return urlConcatenada

def criptomoneda(nombre):
  criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
  if nombre in criptos:
    return True
  else:
    return False

Nombre = input("Ingrese el nombre de la criptomoneda")

while not criptomoneda(Nombre):
  Nombre = input("Ingrese un nombre de la criptomoneda valido")
  
urlCompleta = valor(Nombre)
urlCompleta = requests.get(urlCompleta).json()
print(urlCompleta["price"])
