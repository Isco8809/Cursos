import numpy as np

a={}
b={}

i=0
while i < 3:
 a[i]=input("Ingrese una criptomoneda")
 b[i]=input(f"Ingrese un valor para la criptomoneda {a[i]}")
 i=i+1
 
x=0
while x<3:
    print(f"La criptomoneda {a[x]} tiene un valor de {b[x]}")
    x=x+1