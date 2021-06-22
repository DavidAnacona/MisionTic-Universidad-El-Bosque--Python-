"""
Fundamentos de Programacion
Programa que caracteriza los numeros en positivos, negativos o ceros
Universidad El Bosque - Min Tic 
El siguiente programa lee una lista de numeros y nos indica 
los separa por positivos, negativos y ceros
elaboramos una suma de cada categoria de numeros y nos muestra 
la cantidad de numeros de cada categoria 
"""

print("\t Universidad El Bosque - MisionTic ")
print("\t Programa que caracteriza los numeros ingresados ")

#Declaracion de acumuladores y contadores 
cantidadPositivos = 0
cantidadNegativos = 0 
cantidadNeutros = 0 
sumaPositivos = 0
sumaNegativos = 0
cantidadProcesos = 1 

listaNumeros = int(input("\t Digite la cantidad de numeros a categorizar: "))

while cantidadProcesos <= listaNumeros:
    numero = int(input("\t Digite un numero: "))

    #Procesos
    if numero>0:
        cantidadPositivos += 1
        sumaPositivos += numero
    elif numero<0:
        cantidadNegativos += 1
        sumaNegativos += numero
    else:
        cantidadNeutros += 1

    cantidadProcesos += 1

#salidas 

print("\t Resultados de la categorizacion de la lista de numeros ingresados ")
print("\t Cantidad de numeros ingresados= ",listaNumeros)
print("\t Cantidad de numeros positivos= ",cantidadPositivos)
print("\t Suma de numeros positivos= ",sumaPositivos)
print("\t Cantidad de numeros negativos= ",cantidadNegativos)
print("\t Suma de numeros negativos= ",sumaNegativos)
print("\t Cantidad de numeros neutros= ",cantidadNeutros)