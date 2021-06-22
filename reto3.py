
errorTempMaxima = 0
errorTempMinima = 0
errorTempAmbas = 0
totalTempMaxima = 0
totalTempMinima = 0
totalDias = 0
#Entradas
reiniciar = 's'
while reiniciar == 's' :
    
    tempMaxima =  float(input())
    tempMinima = float(input())
    
    if tempMaxima == 0 and tempMinima == 0 :
        break
    if tempMaxima>35 and tempMinima<5 :
        errorTempAmbas += 1
        totalDias += 1 
    elif tempMaxima > 35 :
        errorTempMaxima += 1
        totalDias += 1
    elif tempMinima <5 :
        errorTempMinima += 1
        totalDias +=1 
    else:
        totalTempMaxima = totalTempMaxima + tempMaxima
        totalTempMinima = totalTempMinima + tempMinima
        totalDias += 1
            
totalErrores = errorTempAmbas + errorTempMaxima + errorTempMinima
diasSinErrores = totalDias - totalErrores
mediaTempMaxima = totalTempMaxima / diasSinErrores
mediaTempMinima = totalTempMinima / diasSinErrores
porcentajeError =  (totalErrores * 100) / totalDias
print(totalDias)
print(totalErrores)
print(errorTempMinima)
print(errorTempMaxima)
print(errorTempAmbas)
print(mediaTempMaxima)
print(mediaTempMinima)
print(porcentajeError)
