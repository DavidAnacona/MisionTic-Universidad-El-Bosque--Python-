"""
Fundamentos de Programacion
Universidad El Bosque - Min Tic 
Este programa saca el promedio de nota de cada estudiante y de cada materia
"""
# Definimos La matriz vacia
matriz = []
# Definiendo el tamaño de la matriz de forma dinamica
filas = int(input("Digite cantidad de materias = "))
columnas = int(input("Digite cantidad de estudiantes = "))
# Creacion de la matriz (filas X columnas y rellena de ceros)
for x in range(filas):
    matriz.append([0]*columnas)
# Cargar datos en la matriz solicitados al usuario
for a in range(filas):
    for b in range(columnas):
        print ("Digite la nota de cada estudiante [",a," ]", "[",b,"]=" )  
        matriz [a][b]= int(input())

# Suma datos en la matriz solicitados al usuario
print (matriz)
suma = 0
acumulador_positivos = 0
acumulador_negativos = 0
for a in range(filas):
    for b in range(columnas):
        suma = suma + matriz [a][b]
        promedio=suma/columnas
    print ("El promadio de la materia [", a, "]es: ",promedio)
    suma=0
for b in range(columnas):
    for a in range(filas):
        suma = suma + matriz [a][b]
        promedio=suma/filas
    print ("El promedio del estudiante [", b, "]es: ",promedio)
    suma=0