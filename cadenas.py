"""
Fundamentos de Programacion
Programa que simula los metodos para manejo de cadenas
Universidad El Bosque - Min Tic 
"""
reiniciar = "s"
while reiniciar=="s": 
    print ("\n\t Universidad El Bosque - Min Tic ")
    print ("\n\t Aplicacion con Metodos de Cadenas")
    #Entradas
    cadena = input("\n\t Digite una secuencia de caracteres= ")
    tamaño = len(cadena)
    print ("\n\t tamaño de la Cadena",tamaño)
    #Imprima todas los elementos de la cadena posicion por posicion
    for contador in range (0, tamaño):
        letra= cadena[contador]    
        print ("\n\t Posicion[",contador,"]=",letra)
   
    for contador in cadena: 
        print ("\t" ,contador)

    print ("\t Imprimir los tres primeros datos de la cadena" ,cadena[0:3])
    print ("\t Imprimir los tres primeros datos de la cadena" ,cadena[:3])
    print ("\t Imprimir desde el quinto dato de la cadena hasta el final" ,cadena[5:])
    print ("\t Imprimir los ultimo tres caracteres de la cadena",cadena[tamaño-3:])
    print ("\t Imprimir los ultimo tres caracteres de la cadena",cadena[-3:])