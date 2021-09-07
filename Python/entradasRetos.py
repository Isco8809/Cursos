from Retos1 import Trabajor as tb

salario, cantidadHoras, Bonificacion =  input("Ingrese los valores").split(" ")
Daniel = tb(float(salario), float(cantidadHoras), float(Bonificacion))
print(Daniel.totalSalario(), Daniel.salarioFinal())