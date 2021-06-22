'''
Elaborar una aplicación en Python que resuelva el siguiente problema
Diseñe un programa que lea una fecha por teclado y calcule la fecha del día siguiente. Implemente el ciclo for en la solución
'''

print('Bienvenido')
print('Universidad El Bosque - MisionTic')

cantidad = int(input('Cantidad de fechas a ingresar '))

for procesos in range(0,cantidad) :

    bisiesto = False
    #Entradas 
    year = int(input('Digite el año deseado '))
    month = int(input('Digite el mes deseado '))
    day = int(input('Digite el dia deseado '))

    if year % 400 == 0 :
        bisiesto = True
    elif year % 4 == 0 :
        bisiesto = True

    if month in (1, 3 , 5 , 7, 8, 10, 11, 12) :
        diasMes = 31
    elif  month == 2 :
        if bisiesto:
            diasMes = 29
        else :
            diasMes = 28
    else:
        diasMes = 30

    if day < diasMes :
        day += 1
    else:
        day = 1
        if month == 12 :
            month = 1
            year += 1
        else:
            month += 1
    print('El dia despues de la fecha que ingresaste es: ',year,'-',month,'-',day)
    
