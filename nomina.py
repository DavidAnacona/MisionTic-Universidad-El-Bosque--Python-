'''
Elabore una nómina de 1 empleado, averigüe las fórmulas para hallar todos los
elementos,  recargo nocturno por días u horas,
Fondo de solidaridad con condicional para el que gane más de 4 salarios mínimos,
limpiar pantalla después de las entradas para que se vea mejor, ciclos.
'''
from os import system
reiniciar = 's';
pagoTotalNomina = 0
while reiniciar == 's':
    #Entradas
    print('Bienvenidos')
    print('El siguiente programa calcula la Nomina de un empleado por semana')

    cedula = int(input('Digite la cedula del empleado '))
    nombre = input('Digite el nombre del empleado ')
    salario = float(input('Digite el salario base del trabajador, es el valor firmado en el contrato '))
    dias = int(input('Digite los dias trabajados por el empleado '))
    horasExtrasDiurnas = int(input('Digite la cantidad de horas extras DIURNAS laboradas por el empleado '))
    horasExtrasNocturnas = int(input('Digite la cantidad de horas extras NOCTURNAS  laboradas por el empleado '))
    horasExtrasFestivas = int(input('Digite la cantidad de horas extras FESTIVAS laboradas por el empleado '))
    diasLaboradosNoches = int(input('Digite la cantidad de dias laborados en la noche '))

    sueldo = (salario / 30) * dias
    valorHorasExtrasDiurnas = ((salario / 30) / 8) * 1.25  * horasExtrasDiurnas
    valorHorasExtrasNocturnas = ((salario / 30)/8) * 1.75 * horasExtrasNocturnas
    valorHorasExtrasFestivas = ((salario / 30) / 8) * 2 * horasExtrasFestivas

    if salario <= 1817052 :
        subsidio = 106454 / 30 * dias
    else:
        subsidio = 0

    if diasLaboradosNoches > 0 :
        recargoNocturno = (salario/30) * diasLaboradosNoches * 1*35
    else:
        recargoNocturno = 0

    totalDevengado = sueldo  + subsidio + valorHorasExtrasDiurnas + valorHorasExtrasNocturnas + valorHorasExtrasFestivas + recargoNocturno
    salud = ((totalDevengado - subsidio)*4) / 100
    pension = ((totalDevengado - subsidio)*4)/100

    if salario >= 3634104 :
        fondo = (salario * 1)/100
    else:
        fondo = 0

    totalDeducido = salud + pension + fondo 
    netoPagado = totalDevengado - totalDeducido

    system("cls")
    print('**********************************************************')
    print('Cedula del empleado: ',cedula)
    print('Nombre del empleado: ',nombre)
    print('Salario base: ',salario)
    print('Dias laborados: ',dias)
    print('Numero de horas extras diurnas: ',horasExtrasDiurnas)
    print('Numero de horas extras nocturnas: ',horasExtrasNocturnas)
    print('Numero horas extras festivas: ',horasExtrasFestivas)
    print('Numero de dias laborados en la noche: ',diasLaboradosNoches)
    print('********************************************************')
    print('\n\t Total Devengado')
    print('Sueldo mes: ',sueldo)
    print('subsidio: ',subsidio)
    print('Valor horas extras diurnas: ',valorHorasExtrasDiurnas)
    print('Valor horas extras nocturnas: ',valorHorasExtrasNocturnas)
    print('Valor horas extras festivos: ',valorHorasExtrasFestivas)
    print('Dias laborados en la noche: ',diasLaboradosNoches)
    print('Recargo nocturno: ',recargoNocturno)
    print('Recargo Devengado: ',totalDevengado)
    print('*********************************************************')
    print('\n\t Total Deducido')
    print('Salud: ',salud)
    print('Pension: ',pension)
    print('Fondo de solidaridad: ',fondo)
    print('Total deducido: ',totalDeducido)
    print('*********************************************************')
    print('\n\t Neto pagado')
    print('Valor a pagar: ',netoPagado)
    print('*********************************************************')
    reiniciar = input('Señor usuario, Desea liquidar otro empleado: s / n')
    pagoTotalNomina = pagoTotalNomina + netoPagado

print('*************************************************************')
print('*************************************************************')
print('Valor total de la nomina a pagar')
print('total: ',pagoTotalNomina)
print('*************************************************************')
print('*************************************************************')

    







    
