'''
Haremos un programa el cual calcule el interes compuesto
con pago de interes en diferentes tiempos
'''
print('Bienvenidos')
print('este programa calcula el interes compuesto')

#Entradas
capital = float(input('Digite el capital inicial '))
interes = int(input('Digite la tasa de interes '))
tiempo = int(input('Digite la cantidad de tiempo en años '))

print('Seleccione el tiempo del pago de interes')
print('1 - Pago de interes diario')
print('2 - pago de interes mensual')
print('3 - pago de interes trimestral')
print('4 - pago de interes anual')
perido = int(input())

#Procesos

if periodo == 1 :
    interesFinal = interes / 100
    tiempofinal = 365 * tiempo
    capitalFinal = capital * (1 + interesfinal / 365)^tiempoFinal
    print('El capital final es de: ',capitalFinal,' con un interes de ',interes,'%')
elif periodo == 2:
    interesFinal = interes / 100
    tiempofinal = 12 * tiempo
    capitalFinal = capital * (1 + interesfinal / 12)^tiempoFinal
    print('El capital final es de: ',capitalFinal,' con un interes de ',interes,'%')
elif periodo == 3:
    interesFinal = interes / 100
    tiempofinal = 4 * tiempo
    capitalFinal = capital * (1 + interesfinal / 4)^tiempoFinal
    print('El capital final es de: ',capitalFinal,' con un interes de ',interes,'%')
elif periodo == 4:
    interesFinal = interes / 100
    tiempofinal = 1 * tiempo
    capitalFinal = capital * (1 + interesfinal / 1)^tiempoFinal
    print('El capital final es de: ',capitalFinal,' con un interes de ',interes,'%')
else:
    print('el tipo de pago qque requiere no lo tenemos en este momento')
    
              
