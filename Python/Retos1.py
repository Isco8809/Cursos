class Trabajor(object):
    def __init__(self,lista):
        var  = self.cadena(lista)
        self.salario = var[0]
        self.cantHoras = var[1]
        self.bonificacion = var[2]
    
    def cadena(self,lista):
        valor=[]
        for x in lista.split(" "):
            valor.append(int(x))
        return valor

    def salarioHoras(self):
        return (self.salario/199)

    def valorHoraExtra(self):
        valor = self.salarioHoras()
        return (valor*1.45)*self.cantHoras
    
    def Bonificacion(self):
        if self.bonificacion == 1:
            return self.salario * 0.055
        else:
            return 0
    
    def totalSalario(self):
        valor = self.valorHoraExtra() 
        boni = self.Bonificacion()
        return round(float(self.salario + valor + boni),1)
    
    def descuentos(self):
        total = self.totalSalario()
        return ((self.totalSalario() * 0.05) + ((self.totalSalario() * 0.04) * 2))

    def salarioFinal(self):
        return round(self.totalSalario() - self.descuentos(),1)