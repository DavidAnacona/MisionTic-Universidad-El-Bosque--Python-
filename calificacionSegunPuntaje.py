"""
Utilizando esta información, escribir una aplicación en python, que acepte una calificación numérica del estudiante (0-100),
convierta esta calificación a su equivalente en letra para una población de 50 estudiantes,
diga cuantos estudiantes están en A, cuantos, en B, C, D ó F. El programa debe solicitarle al usuario el número de estudiantes a clasificar

Entradas
cantidadEstudiantes: representa la cantidad de estudiantes que se van a evaluar}
puntaje: representa el puntaje que saco el estudiante en numeros
procesos = 0;
Procesos

Condicional (puntaje>=90): la calificacion es A
Condicional (puntaje<90 && puntaje>=80) la calificacion es B
Condicional (puntaje<80 && puntaje>=70) la calificacion es C
Condicional (puntaje<70 && puntaje>=60) la calificacion es D
Condicional (puntaje<60) la calificacion es F

Salidas
El estudiante saco una calificacion de: + calificacion
"""
print("Bienvenidos a la Universidad vagancia")
print("Haremos la conversion del puntaje obtenido en el examen")

cantidadEstudiantesEnA = 0
cantidadEstudiantesEnB = 0
cantidadEstudiantesEnC = 0
cantidadEstudiantesEnD = 0
cantidadEstudiantesEnF = 0

cantidadEstudiantes = int(input("Digite la cantidad de estudiantes    "))

for procesos in range(0,cantidadEstudiantes):

    puntaje = int(input("Digite el puntaje en el examen obtenido por el estudiante  "))

    if(puntaje>=90):
        print("El estudiante tuvo una calificacion de A en el examen")
        cantidadEstudiantesEnA = cantidadEstudiantesEnA + 1
    elif(puntaje<90 and puntaje>=80):
        print("El estudiante tuvo una calificacion de B en el examen")
        cantidadEstudiantesEnB = cantidadEstudiantesEnB + 1
    elif(puntaje<80 and puntaje>=70):
        print("El estudiante tuvo una calificacion de C en el examen")
        cantidadEstudiantesEnC = cantidadEstudiantesEnC + 1
    elif(puntaje<70 and puntaje>=60):
        print("El estudiante tuvo una calificacion de D en el examen")
        cantidadEstudiantesEnD = cantidadEstudiantesEnD + 1
    elif(puntaje<60:
        print("El estudiante tuvo una calificacion de F en el examen")
        cantidadEstudiantesEnF = cantidadEstudiantesEnF + 1

print("La cantidad de estudiantes que obtuvieron una calificacion de A: ",cantidadEstudiantesEnA)
print("La cantidad de estudiantes que obtuvieron una calificacion de B: ",cantidadEstudiantesEnB)
print("La cantidad de estudiantes que obtuvieron una calificacion de C: ",cantidadEstudiantesEnC)
print("La cantidad de estudiantes que obtuvieron una calificacion de D: ",cantidadEstudiantesEnD)
print("La cantidad de estudiantes que obtuvieron una calificacion de F: ",cantidadEstudiantesEnF)



        
    
        
