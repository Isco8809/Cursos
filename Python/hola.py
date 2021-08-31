def abrir(Nombre):
    archivo = open(Nombre+".txt","r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def crear(Nombre):
    archivo = open(Nombre+".txt","x")
    archivo.close()

def escribir(Nombre,palabra):
    diccionario=''
    archivo = open(Nombre+".txt","at")
    ##termino = input("Escriba el término para el diccionario: ")
    descripcion = input("Escriba la descripcón del término: ")
    diccionario=str(palabra)+':'+str(descripcion)
    archivo.write(str(diccionario))
    print(archivo)
    archivo.close()
    
existe = 1
Nombre=""

while existe == 2 or existe == 1:
    existe = int(input("Desea consultar o crear el glosario de terminos de la criptomoneda \n 1.Crear 2.Consultar"))
    
    if existe == 1:
        Nombre=input("Ingrese el nombre del archivo a crear: ")
        crear(Nombre)
        
    elif existe == 2:
        Nombre=input("Nombre del archivo que desea abrir para consultar: ")
        archivo = abrir(Nombre)
        diccionario = {}
        palabra = input("Que termino desea consultar: ")
        
        if palabra in diccionario:
            print("palabra clave: ", palabra)
            
        else:
            rspuesta= input("El termino no existe, lo desea agregar? \n1.SI 2.NO")
            
            if rspuesta == "SI":
                escribir(Nombre,palabra)
                
            else:
                print("No fue agregado")      
                      
    else:
        print("la opcion no es valida")
