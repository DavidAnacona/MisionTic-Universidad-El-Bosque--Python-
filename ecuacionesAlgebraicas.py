'''
Realizaremos un programa el cual realice
algunas operaciones algebraicas especificas
'''

'''
Primera ecuacion a resolver 4x^2 - 2x +  7
'''
import math

print('Programa que da solcuion a algunas ecuacion algebraicas')
print('Ecuacion a resolver: 4x^2 - 2x + 7 ')

#Entrada
incognita = float(input('Digite un valor para X '))

#proceso
numeroElevar = 4 * incognita
operacion1 = pow(numeroElevar,2) - ((2*incognita) + 7)

#Salida

print('La solucion de la ecuacion 4x^2 - 2x + 7 es: ',operacion1)

#Entrada 
print('Segunda ecuacion a resolver √b^2 - 4ac ')
incognitaA = float(input('Digite un valor para a '))
incognitaB = float(input('Digite un valor para b '))
incognitaC = float(input('Digite un valor para c '))
#Proceso
operacion2 = pow(incognitaB,2) - (4 * incognitaA * incognitaC)
raizCuadrada = math.sqrt(operacion2**2)

print('El resultado de la segunda ecuacion es: ',raizCuadrada)

#Entrada
print('Tercera ecuacion a resolver x+y/x - 3x/5 ')
incognitaX = float(input('Digite un valor para x '))
incognitaY = float(input('Digite un valor para Y '))

#Proceso

dividendo1 = incognitaX + incognitaY
primeraFraccion = dividendo1 / incognitaX
dividendo2 = 3 * incognitaX
segundaFraccion = dividendo2 / 5

operacionFinal = primeraFraccion - segundaFraccion

#Salida

print('La solucion de la tercera ecuacion es: ', operacionFinal)










