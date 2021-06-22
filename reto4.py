def datos():
    global valorHora, horas
    horas = int(input('Digite el numero de horas trabajadas en la semana '))
    valorHora = int(input('Digite el valor de la hora '))
    return valorHora, horas
    
def salarioBruto():
    if horas <= 40 and horas >= 0 :
        salario = horas * valorHora
        horasExtras = 0 
    elif horas > 40:
        salarioSinRecargo = 40 * valorHora
        horasExtras = (horas - 40 ) * valorHora * 1.5
        salario = salarioSinRecargo + horasExtras
        
    return salario
    
def parafiscales():
    parafiscales = salarioBruto() *  (9/100)
    
    return parafiscales
    
def primaCesantias():
    primaCesantias = salarioBruto() * (8.33/100)
    
    return primaCesantias
    
def interesCesantias():
    interesCesantias = salarioBruto() * (1/100)
    
    return interesCesantias
    
def salud():
    salud = salarioBruto() * (4/100)
    
    return salud
    
def pension():
    pension = salarioBruto() * (4/100)
    
    return pension
    
def vacaciones():
    vacaciones = salarioBruto() * (4.17/100)
    
    return vacaciones


def totalDescuento():
    
    totalDescuento = parafiscales()+salud()+pension()
    
    return totalDescuento
    
def sueldoNeto():
    sueldoNeto = salarioBruto() - totalDescuento()
    
    return sueldoNeto
    
datos()
if horas <= 40 and horas >= 0:
    salarioSinRecargo = horas * valorHora
    horasExtras = 0
    
elif horas > 40 :
    salarioSinRecargo = 40 * valorHora
    horasExtras = (horas - 40)* valorHora*1.5
    salario = salarioSinRecargo + horasExtras

print('Salario sin horas extras: $',salarioSinRecargo)
print('Valor horas extras: $',horasExtras)
print('Salario bruto: $',salarioBruto())
print('Descuento por parafiscales: $',parafiscales())
print('Descuento por salud: $',salud())
print('Descuento por pension: $',pension())
print('total descuentos: 4',totalDescuento())
print('Sueldo neto a pagar: $',sueldoNeto())
print('Prima: $',primaCesantias())
print('Cesantias: $',primaCesantias())
print('interes cesantias: $',interesCesantias())
print('Vacaciones: $',vacaciones())
