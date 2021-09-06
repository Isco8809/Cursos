class formula(object):
    def __init__(self, lista):
        var  = self.cadena(lista)
        self.recorrido  = var[0]
        self.velocidad = var[1]
        self.tiempo = var[2]
        
    def calculo(self):
        metros = self.velocidad * 1000
        segundo = self.tiempo / 60
        return (metros*segundo)/self.recorrido

    def porcentaje(self):
        return (self.calculo() *100)/60

    def condicion(self):
        return float(100-self.porcentaje())

    def cadena(self,lista):
        valor=[]
        for x in lista.split(" "):
            valor.append(int(x))
        return valor
    
    def imprimir(self):
        if round(self.condicion(),1) <= 0.0:
            return "Velocidad normal"
        elif round(self.condicion(),1) < 15:
            return "Nuevo record"
        else:
            return "Entrevista"

    def verificacion(self):
        if self.recorrido < 0 or self.velocidad < 0 or self.tiempo < 0:
            return "Medición erronea"
        else:
            return self.imprimir()