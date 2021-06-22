"""
haremos un programa el cual calcula el area y la longitud de un circulo para ello utilizaremos las siguientes formulas

longitud = 2 * pi * radio
area = radio * radio * pi 

"""
from math import pi 
print("Programa que calcula el area y la longitud de un circulo")

#Entrada
radio = float(input("digite el radio del circulo "))

#Procesos

longitudCirculo = 2 * pi * radio
area = radio * radio * pi

#Salidas
print("El circulo con base ",radio," tiene una area de ",area," y tiene una longitud de ",longitudCirculo)
