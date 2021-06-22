'''
Se trata de escribir el algoritmo que permita
emitir la factura correspondiente a una compra de un artículo determinado,
del que se adquieren una o varias unidades. El IVA a aplicar es del 15 por 100
'''

from os import system
reiniciar = "s"
precioTotal = 0

while reiniciar == "s":
    print('Universidad El Bosque - minTic')
    print('factura de tienda Melo.S.A.S')

    #Entrada
    nombre =  input('Digite el nombre del articulo ')
    precio = float(input('Digite el precio del producto '))
    cantidad = int(input('Digite la cantidad del producto a comprar '))

    subtotal = precio * cantidad

    #Salidas

    print('nombre: ',nombre)
    print('precio: ',precio)
    print('cantidad: ',cantidad)
    print('El precio de este articulo es asi: ', subtotal)

    reiniciar = input('Desea comprar otro articulo s/n : ')
    precioTotal = precioTotal + subtotal

iva = subtotal *0.15
totalCompra = precioTotal  + iva
system("cls")
print('Subtotal: ',precioTotal)
print('iva: ',iva)
print('total compra: ',totalCompra)

                  
    
