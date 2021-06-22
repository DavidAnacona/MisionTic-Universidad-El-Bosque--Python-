"""
Programa el cual calcula el salario semanal
tenidendo en cuenta las horas trabajadas por dia y el valor por hora
"""

print("Bienvenidos")
print('Empresa la Vagancia')
print('Vamos a calcular el slario semanal de un trabajador')
#Entradas
horasLunes = int(input('Digite las horas laboradas del dia lunes '))
horasMartes = int(input('Digite las horas trabajadas del dia martes '))
horasMiercoles = int(input('Digite las horas trabajadas del dia miercoles '))
horasJueves = int(input('Digite las horas trabajadad del dia jueves '))
horasViernes = int(input('Digite las horas trabajadas del dia viernes '))
horasSabado = int(input('Digite las horas trabajadas del dia sabado '))
valorHora = float(input('Digite el valor de la hora '))

#Procesos
horasTotales  = horasLunes + horasMartes + horasMiercoles + horasJueves + horasViernes + horasSabado
salarioSemanal = valorHora * horasTotales

#Salidas

print('Horas laboradas en la semana: ',horasTotales)
print('el salario semanal es de: ',salarioSemanal)

                  
