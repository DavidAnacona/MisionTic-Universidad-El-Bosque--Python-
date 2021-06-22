"""
Fundamentos de Programacion
Universidad El Bosque - Min Tic 
Programa que guarda los productos de una tienda en un archivo .txt
"""
import io
import os 

print("Universidad El Bosque - MisionTic")
print("Productos Tienda Melo")

reiniciar = 's'

while reiniciar == 's':

    print('Tienda Las chicherias')
    #Entradas
    codigo = int(input('Digite el codigo del producto '))
    nombre = input('Digite el nombre del producto ')
    precio = float(input('Digite el precio del producto '))
    cantidad = int(input('Digite la cantidad de producto en el local '))

    subtotal = precio * cantidad

    #Salidas
    print('Codigo producto: ',codigo)
    print('nombre producto: ',nombre)
    print('precio producto: ',precio)
    print('cantidad a comprar: ',cantidad)

    reiniciar = input('Desea comprar otro producto: s/n ')

    producto = "\n" + str(codigo) + "\n" + nombre + "\n" + str(precio) + "\n" + str(cantidad) + "\n"
    file = open("productos.txt","a")
    file.write(producto)
    file.close()
