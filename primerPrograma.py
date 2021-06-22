'''
El programa de Ingeniería ambiental de la Universidad El Bosque en una de sus salidas de 
campo, ha registrado un par de temperaturas diarias (máxima, mínima) para todos los días que 
permanecieron en campo. Dadas las condiciones del terreno donde se encontraban, no era 
posible tener temperaturas menores de 5 grados ni mayores de 35 grados, que se consideraron 
errores, pero igual se registraron para su estudio posterior. La pareja de temperaturas (0,0) 
indicará que se han terminado los datos de la salida de campo
'''
print('Bienvenidos')
print('Universidad El Bosque - MisionTic')

acabar = 1
errorTempMaxima = 0
errorTempMinima = 0
errorTempAmbas = 0
totalTempMaxima = 0
totalTempMinima = 0
#Entradas
dias = int(input('Digite la cantidad de dias de la salida de campo '))
for i in range(0,dias) :

    print('Digite la temperatura maxima del dia ',i + 1,': ')
    tempMaxima =  float(input())
    print('Digite la temperatura minima del dia ',i + 1,': ')
    tempMinima = float(input())
    
    if tempMaxima == 0 and tempMinima == 0 :
        break
    if tempMaxima>35 and tempMinima<5 :
        errorTempAmbas += 1
    elif tempMaxima > 35 :
        errorTempMaxima += 1
    elif tempMinima <5 :
        errorTempMinima += 1
    else:
        totalTempMaxima = totalTempMaxima + tempMaxima
        totalTempMinima = totalTempMinima + tempMinima
            
totalErrores = errorTempAmbas + errorTempMaxima + errorTempMinima
diasSinErrores = dias - totalErrores
mediaTempMaxima = totalTempMaxima / diasSinErrores
mediaTempMinima = totalTempMinima / diasSinErrores
porcentajeError = (diasSinErrores / dias) * 100
print('Total dias que dura la salida de campo: ',dias)
print('Total dias en los que se tuvieron errores de temperatura: ',totalErrores)
print('Dias con errores de temperatura menor a 5 grados: ',errorTempMinima)
print('Dias con errores de temperatura mayor a 35 grados: ',errorTempMaxima)
print('Dias con errores en ambas temperaturas: ',errorTempAmbas)
print('La media de la temperatura maxima sin tener en cuenta los dias que se presentaron errores es: ',mediaTempMaxima)
print('La media de la temperatura minima sin tener en cuenta los dias que se presentaron errores es: ',mediaTempMinima)
print('El porcentaje en los que se reportaron errores fueron: ',porcentajeError,'%')
