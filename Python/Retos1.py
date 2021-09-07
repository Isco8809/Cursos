class Trabajor():
    def __init__(self,salario, cantidaHoras, bonificacion):
        self.salario = salario
        self.cantHoras = cantidaHoras
        self.bonificacion = bonificacion

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
    
    def holaMundo(self):
        return print("Hola")