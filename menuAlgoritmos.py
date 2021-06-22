"""
haremos un menu en el que llamaremos todos los ejercicios que
estaremos realizando durante el ciclo
"""


reiniciar = "s"

while reiniciar == "s":

    print("\n\t Bienvenidos ")
    print("\n\t A continuacion mostraremos un listado de todos los program,as realizados")
    print("\n\t Elaborado por David Santiago Anacona Castellanos")
    print("\n\t 1 - Operaciones Matematicas")
    print("\n\t 2 - Area de un triangulo")
    print("\n\t 3 - Area y longitud de un circulo")
    print("\n\t 4 - salario semanal")
    print("\n\t 5 - Interes compuesto")
    print("\n\t 6 - Factura con Iva del 15")
    print("\n\t 7 - Ecuaciones algebraicas")
    print("\n\t 8 - Nomina")
    print("\n\t 9 - Reto 1--Semana 1 y 2-Factura")
    print("\n\t 10 - Sondeo de edades y pesos")
    print("\n\t 11 - reto 2 - Descuentos en matricula")
    print("\n\t 12 - Calificacion segun puntaje - ciclo For")
    print("\n\t 13 - reto 3 - Salida de  campo")
    print("\n\t 14 - Cadenas ")
    print("\n\t 15 - Valor de viaje con ciclo For")
    print("\n\t 16 - Dia despues de fecha ingresada")
    print("\n\t 17 - Caracterizacion de numeros")
    print("\n\t 18 - Reto 4: Nomina Docentes")
    print("\n\t 19 - Matriz de estudiantes")
    print("\n\t 20 - Persistencia de datos - Productos tienda")
    print("\n\t 21 - Reto 5: Agenda beneficiarios")
    
    opcion = int(input("\n\t El programa a ver es: "))

    if opcion ==1 :
        import operacionesMatematicas
    elif opcion == 2 :
        import areaTriangulo
    elif opcion == 3 :
        import calculosCirculo
    elif opcion == 4:
        import salarioSemanal
    elif opcion == 5 :
        import impuestoCompuesto
    elif opcion == 6 :
        import facturaIva15
    elif opcion == 7 :
        import ecuacionesAlgebraicas
    elif opcion == 8 :
        import nomina
    elif opcion == 9 :
        import reto1
    elif opcion == 10 :
        import sondePesos
    elif opcion == 11 :
        import reto2
    elif opcion == 12 :
        import calificacionSegunPuntaje
    elif opcion == 13:
        import reto3
    elif opcion == 14 :
        import cadenas
    elif opcion == 15 :
        import valorViaje
    elif opcion == 16 :
        import diaDespuesDeFecha
    elif opcion == 17 :
        import caracterizacionNumeros
    elif opcion == 18 :
        import reto4
    elif opcion == 19 :
        import matriz
    elif opcion == 20 :
        import archivos.py
    elif opcion == 21 : 
        import reto5
        
        
        


    
