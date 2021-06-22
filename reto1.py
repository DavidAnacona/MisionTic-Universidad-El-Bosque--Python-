'''
Reto 1 Semana 1 y 2

El dueño de una tienda de artículos de ropa le ha solicitado a usted como programador, que le 
desarrolle un algoritmo (diagrama de flujo o pseudocódigo) que le permita calcular el valor a 
pagar de cada cliente que hace compras en su tienda. Como él ha sido muy bien asesorado por 
la Universidad El Bosque, además quiere obtener el máximo provecho de esta tarea, le solicita 
específicamente lo siguiente, en ese orden

Caso 1: el cliente compra 1 pantalón de hombre código 123 por valor de $45000, una 
camisa manga corta código 345 por valor de $35000 y por último una camiseta Polo 
código 456 por valor de $27000.
- Caso 2: el cliente compra 3 camisetas cuello redondo por valor de $12000 cada una, 
2 pares de medias tobilleras por valor de $3000 cada par.Reto 1 – Semana 1 y 2 [2] Semana 1 
En caso de encontrar errores en las pruebas debe retornar al segundo paso y hacer las 
correcciones respectivas.
'''
print('Bienvenidos Universidad El Bosque -- MisionTic')
print('realizaremos el reto de la semana 1 y 2')

reiniciar = 's'
precioTotal = 0

while reiniciar == 's':

    print('Tienda Las chicherias')
    #Entradas
    codigo = int(input('Digite el codigo del producto '))
    nombre = input('Digite el nombre del producto ')
    precio = float(input('Digite el precio del producto '))
    cantidad = int(input('Digite la cantidad del producto a comprar '))

    subtotal = precio * cantidad

    #Salidas
    print('Codigo producto: ',codigo)
    print('nombre producto: ',nombre)
    print('precio producto: ',precio)
    print('cantidad a comprar: ',cantidad)

    reiniciar = input('Desea comprar otro producto: s/n ')
    precioTotal = precioTotal + subtotal

iva = subtotal * 0.19
totalCompra = precioTotal + iva
print('Subtotal: ',precioTotal)
print('Iva: ',iva)
print('Total compra: ',totalCompra)


    
