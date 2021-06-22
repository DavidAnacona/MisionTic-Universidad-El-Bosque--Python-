"""
Reto Semana 3

Entradas
nombre: Representa el nombre del candidato
apellido: Representa el apellido del candidato
edad: Almacena la edad del candidato
puntajeExamen : Almacen el puntaje obtenido en el examen por el candidato
salariosMensuales: Almacena el numero de salarios minimos mensuales del ingreso familiar del candidato

Proceso

Edades
Condicional(edad>=15 and edad<=18) Obtiene 25% descuento
Condicional(edad>=19 and edad<=21) Obtiene 15% descuento
Condicional(edad>=22 and edad<=25) Obtiene 10% descuento
Condicional(edad>25)No obtiene descuento

Salario
Condicional(salariosMensuales<=1) Obtiene 30% descuento
Condicional(salariosMensuales>1 and salariosMensuales<=2) Obtiene 20% descuento
Condicional(salariosMensuales>2 and salariosMensuales<=3) Obtiene 10% descuento
Condicional(salariosMensuales>3 and salariosMensuales<=4) Obtiene 5% descuento
Condicional(salariosMensuales>4) No obtiene descuento

Puntajes examen
Condicional(puntajeExamen<80)No obtiene descuento
Condicional(puntajeExamen>=80 and puntajeExamen<86) Obtiene 30% de descuento
Condicional(puntajeExamen>=86 and puntajeExamen<91) Obtiene 35% de descuento
Condicional(puntajeExamen>=91 and puntajeExamen<96) Obtiene 40% de descuento
Condicional(puntajeExamen>=96) Obtiene 45% de descuento

Salidas

nombre: Representa el nombre del candidato
apellido: Representa el apellido del candidato
cantidadDescuentoTotal: Representa el porcentaje de descuento total obtenido por el candidato
"""
acumuladorDescuentoTotal = 0;
reiniciar = "s";

while reiniciar == "s":
    nombre = input("Digite el nombre del candidato ")
    apellido = input("Digite los apellidos del candidato ")
    edad = int(input("Digite la edad del candidato en años "))
    puntajeExamen = float(input("Digite el puntaje obtenido por el candidato en el examen "))
    salariosMensuales = float(input("Digite la cantidad de salarios minimos mensuales de ingreso familiar del candidato "))

    print("El candidato ",nombre," ",apellido, " con una edad de ",edad," años obtiene los siguientes descuentos")
    if edad>=15 and edad<=18 :
        acumuladorDescuentoTotal = acumuladorDescuentoTotal + 25
        print("El candidato obtiene un descuento de 25% por edad")
        
        if salariosMensuales<=1 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
            print("El candidato obtiene un descuento del 30% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>1 and salariosMensuales<=2 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 20
            print("El candidato obtiene un descuento del 20% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>2 and salariosMensuales<=3 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 10
            print("El candidiato obtiene un descuento del 10% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>3 and salariosMensuales<=4 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 5
            print("El candidato obtiene un descuento del 5% por ingresos familiares")

            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")
                print("El candidato tiene un puntaje de: ",puntajeExamen)
            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>4 :
            print("El candidato no obtiene ningun descuento por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        else: print ("La cantidad de ingresos familiares no esta definido")
        
    elif edad>=19 and edad<=21 :
        acumuladorDescuentoTotal = acumuladorDescuentoTotal + 15
        print("El candidato obtiene un descuento de 15% por edad")
        
        if salariosMensuales<=1 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
            print("El candidato obtiene un descuento del 30% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>1 and salariosMensuales<=2 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 20
            print("El candidato obtiene un descuento del 20% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>2 and salariosMensuales<=3 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 10
            print("El candidiato obtiene un descuento del 10% por ingresos familiares")

            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")
                print("El candidato tiene un puntaje de: ",puntajeExamen)
            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                input("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>3 and salariosMensuales<=4 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 5
            print("El candidato obtiene un descuento del 5% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>4 :
            print("El candidato no obtiene ningun descuento por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        else: print("La cantidad de ingresos familiares no esta definido")
        
    elif edad>=22 and edad<=25 :
        acumuladorDescuentoTotal = acumuladorDescuentoTotal + 10
        print("El candidato recibe un descuento de 10% por edad")

        if salariosMensuales<=1 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
            print("El candidato obtiene un descuento del 30% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>1 and salariosMensuales<=2 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 20
            print("El candidato obtiene un descuento del 20% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                input("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>2 and salariosMensuales<=3 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 10
            print("El candidiato obtiene un descuento del 10% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>3 and salariosMensuales<=4 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 5
            print("El candidato obtiene un descuento del 5% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                input("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>4 :
            print("El candidato no obtiene ningun descuento por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        else: input ("La cantidad de ingresos familiares no esta definido")
        
    elif edad>25 :
        print("La edad del candidato no aplica para ningun descuento")

        if salariosMensuales<=1 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
            print("El candidato obtiene un descuento del 30% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>1 and salariosMensuales<=2 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 20
            print("El candidato obtiene un descuento del 20% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                input("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>2 and salariosMensuales<=3 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 10
            print("El candidiato obtiene un descuento del 10% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>3 and salariosMensuales<=4 :
            acumuladorDescuentoTotal = acumuladorDescuentoTotal + 5
            print("El candidato obtiene un descuento del 5% por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        elif salariosMensuales>4 :
            print("El candidato no obtiene ningun descuento por ingresos familiares")
            print("El candidato tiene un puntaje de: ",puntajeExamen)
            if puntajeExamen<80 :
                print("Tu puntaje es bajo por lo que no recibes ningun descuento por examen")

            elif puntajeExamen>=80 and puntajeExamen<86 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 30
                print("El candidato recibe un descuento del 30% por el puntaje del examen")

            elif puntajeExamen>=86 and puntajeExamen<91 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 35
                print("El candidato recibe un descuento del 35% por el puntaje del examen")

            elif puntajeExamen>=91 and puntajeExamen<96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 40
                print("El candidato recibe un descuento del 40% por el puntaje del examen")

            elif puntajeExamen>=96 :
                acumuladorDescuentoTotal = acumuladorDescuentoTotal + 45
                print("El candidato recibe un descuento del 45% por el puntaje del examen")
            
        else: print ("La cantidad de ingresos familiares no esta definido")
        
    else: print("Por favor verifica la edad del candidato")
    print("El descuento total obtenido por el candidato es de: ",acumuladorDescuentoTotal,"%")
    if acumuladorDescuentoTotal == 100 :
        print("Felicidades el valor de tu matricula sera 0")
    reiniciar = input("Desea ingresar otro candidato s / n ")
    acumuladorDescuentoTotal = 0





























