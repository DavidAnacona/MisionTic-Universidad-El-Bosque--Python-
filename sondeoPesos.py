"""
Una persona desea realizar un muestreo con n personas para determinar el
promedio de peso de los niños, jóvenes,
adultos y viejos que existen en su zona habitacional y cuantos son de
cada uno de las categorías. Se determinan las categorías con base en la
siguiente tabla

Entradas
nombre: Representa el nombre del encuestado
edad: Almacena la edad del encuestado
peso: Almacena el peso del encuestado

Procesos
variable de ciclo: reiniciar y que se encarga de definir si se agregan usuarios a la encuesta
variable que cuente el numero de personas que cumplan con los rangos especificos

condicionales(edad entre 0 y 13 niños)
condicionales(edad entre 14 y 30 jovenes)
condicionales(edad entre 31 y 60 adultos)
condicionales(edad mayor de 61 mayores)

Salida
nombre: Representa el nombre del encuestado
edad: Almacena la edad del encuestado
peso: Almacena el peso del encuestado
"""

#Entradas
contadorNiños = 0
acumuladorPesoNiños = 0
contadorJovenes = 0
acumuladorPesoJovenes = 0
contadorAdultos = 0
acumuladorPesoAdultos = 0
contadorMayores = 0
acumuladorPesoMayores = 0

reiniciar = "s"

while reiniciar == "s":
    nombre = input("Digite el nombre del encuestado: ")
    edad = int(input("Ingresa tu edad en años: "))
    peso = float(input("Ingrese el peso en kilogramos: "))

    #procesos
    if edad>0 and edad<=13 :
        contadorNiños = contadorNiños + 1
        acumuladorPesoNiños = acumuladorPesoNiños + peso

    elif edad>=14 and edad<=30 :
        contadorJovenes = contadorJovenes + 1
        acumuladorPesoJovenes = acumuladorPesoJovenes + peso

    elif edad>=31 and edad<=60 :
        contadorAdultos = contadorAdultos + 1
        acumuladorPesoAdultos = acumuladorPesoAdultos + peso
    elif edad>=61 :
        contadorMayores = contadorMayores + 1
        acumuladorPesoMayores = acumuladorPesoMayores + peso
    else: print("La edad ingresada es incorrecta")
    reiniciar = input("Desea ingresar otro encuestado s / n: ")

contadorTotal = contadorNiños + contadorJovenes + contadorAdultos + contadorMayores
print("Resultados de la encuesta")
print("Poblacion total de encuestado: ",contadorTotal)
print("Numero de niños = ", contadorNiños)
print("Numero de jovenes = ",contadorJovenes)
print("Numero de Adultos = ",contadorAdultos)
print("Numero de mayores = ",contadorMayores)
if contadorNiños == 0: contadorNiños = 1
promedioNiños = acumuladorPesoNiños / contadorNiños
if contadorJovenes == 0: contadorJovenes = 1
promedioJovenes = acumuladorPesoJovenes / contadorJovenes
if contadorAdultos == 0: contadorAdultos = 1
promedioAdultos = acumuladorPesoAdultos / contadorAdultos
if contadorMayores == 0: contadorMayores = 1
promedioMayores = acumuladorPesoMayores / contadorMayores
print("Promedio de peso niños encuestados: ",promedioNiños)
print("Promedio de peso jovenes encuestados: ",promedioJovenes)
print("Promedio de peso adultos encuestados: ",promedioAdultos)
print("Promedio de peso mayores encuestados: ",promedioMayores)

























