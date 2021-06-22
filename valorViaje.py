'''
Elaborar una aplicación en Python que resuelva el siguiente problema:
Determinar el precio de un billete de ida y vuelta en ferrocarril,
conociendo la distancia a recorrer y sabiendo que, si el número de días
de estancia es superior a siete y la distancia superior a 800 kilómetros,
el billete tiene una reducción del 30%. El Precio por kilómetro es de $20000.
Implemente el ciclo for en la solución
'''

print('Bienvenidos')
print('Universidad El Bosque -  MisionTic')

cantidadViajeros = int(input('Digite la cantidad de personas a cotizar costos '))

for procesos in range(0,cantidadViajeros) :
    #Entradas
    distanciaViaje = int(input('Digite la cantidad de Km a recorrer de ida '))
    diasEstancia = int(input('Digite la cantidad de dias de instancia '))

    #Procesos
    distanciaTotal  =  distanciaViaje * 2
    if diasEstancia>7 and distanciaTotal > 800 :
        valor = distanciaTotal * 20.000
        descuento = valor * 0.30
        valorViaje = valor - descuento
        #Salida
        print('Tienes un descuento del 30% que representa $',descuento)
        print('El valor del viaje con tiquetes ida y vuelta y una estancia de ',diasEstancia,' dias es de $',valorViaje)
    else :
        valor = distanciaTotal * 20.000
        print('El valor del viaje con tiquetes ida y vuelta con una estancia de ',diasEstancia,' dias es de $',valor)
        
