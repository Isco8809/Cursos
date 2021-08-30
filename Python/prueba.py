def escribir(palabra):
    ingresar = input("Desea ingresar nuevo término? \nSI NO: ")
    diccionario={}
    while ingresar == "SI":
        if len(palabra) > 0:
            termino = palabra
        else:    
            termino = input("Escriba el término para el diccionario: ")
            descripcion = input("Escriba la descripcón del término: ")
        diccionario[termino]=descripcion
        ingresar = input("Desea ingresar más atributos \nOpc: SI NO: ")
    archivo.write(str(diccionario))
    archivo.close()
    
def leer(archivoOpen):
    archivoLec = open(archivoOpen+".txt","r")
    contenido = archivoLec.read()
    return contenido

existe = input("Desea 1.Buscar el archivo o 2.Crear el archivo? \n1. 2.")
str(existe)

while existe == '1':
    if existe == '1':
        archivoOpen = input("Ingrese el nombre del archivo que desea abrir: ")
        informacion = leer(archivoOpen)
        existe='3'
    else:
        Nombre = input("Ingrese el nombre del archivo: ")+".txt"
        archivo = open(Nombre,"w")
        escribir("")
        existe='1'
    
palabra = input("Ingrese el término a buscar: ")
if palabra in informacion:
    print(informacion[palabra])
else:
    escribir(palabra)

print(leer(archivoOpen))