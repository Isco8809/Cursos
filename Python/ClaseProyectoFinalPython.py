def leer(archivoOpen):
    archivoLec = open(archivoOpen+".txt","r")
    contenido = archivoLec.read()
    #archivoLec.close()
    return contenido

contenido = leer("BD_Usuarios")
print(contenido)