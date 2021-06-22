"""
Universidad El Bosque - MisionTic
Reto 5: realizar una agenda de beneficiarios
"""

import io
import os 

fileName = "agenda.txt"

def data():
    global name,identification,phone

    name = input()
    identification = int(input())
    phone = int(input())

    user = "\n"+name+"\n"+str(identification)+"\n"+str(phone)
    return user


def saveData(user):
  
    if seekIdentification(identification) == False:
        file = open(fileName,"a")
        file.write(user)
        file.close()
        print("El beneficiario ha sido agregado")
    

      
         
            
def listData():

    file = open(fileName,"r")
    data = file.read().strip("\n")
    file.close()
    print(data)

    
def seekIdentification(identification):

    if os.path.exists(fileName) == False:
        seek=False
    else:
        file = open(fileName,"r")
        data = file.readlines()
        file.close()
        seek = False
        for i in range(len(data)):
            if str(identification) in data[i]:
                seek = True
                print("Ya se encuentra un usuario con la cedula ingresada")
    
    return seek
            
def seekPhone():

    print("Digite el nombre y apellido del beneficiario a buscar:")
    nameSeek = input()

    file = open(fileName,"r")
    data = file.readlines()
    file.close()
    seek = False

    for i in range(len(data)):
        if nameSeek in data[i]:
            seek = True
            print(data[i].strip("\n"))
            print(data[i+1].strip("\n"))
            print(data[i+2].strip("\n"))          
            break
    
    if seek == False:
        print("No se encuentra ningun usuario con el nombre ingresado")


def delete():

    print("Digite la cedula del beneficiario a borrar:")
    identificationSeek = int(input())

    file = open(fileName,"r")
    data = file.readlines()
    file.close()

    for i in range(len(data)):
        if str(identificationSeek) in data[i]:
            
            deleteIdent = data[i]
            deletePhone = data[i + 1]
            deleteName = data[i-1]
            break
    
    deleteUser(deleteIdent, deleteName , deletePhone, data)


def deleteUser(deleteIdent, deleteName, deletePhone, data):

    data.remove(deleteIdent)
    data.remove(deleteName)
    data.remove(deletePhone)
    print("El usuario ha sido eliminado del listado")
    fileNew = open(fileName,'w')
    for i in range(len(data)):
        fileNew.write(data[i])
    fileNew.close()
    

def seekNameData():

    letter = input("Digite la letra por la que empiezan los beneficiarios:")
    file = open(fileName,"r")
    print("\n"+"Listado filtrado de beneficiarios: ")
    for linea in file:
        if(linea.startswith(letter)):
            print(linea.strip("\n"))
            print(file.readline().strip("\n"))
            print(file.readline().strip("\n"))
    file.close()
 
    
reiniciar = "s"
while reiniciar=="s":

    
    print("Menu principal")
    print("1. Ver listado")
    print("2. Ver listado filtrado")
    print("3. Agregar beneficiario")
    print("4. Buscar beneficiario")
    print("5. Borrar beneficiario")
    print("6. Salir")

    option = int(input())

    if option == 1:
        print("Listado de beneficiarios")
        listData()
    if option == 2:
        seekNameData()         
    if option == 3:
        print("Digite la información del beneficiario a agregar:")
        saveData(data()) 
    if option == 4:
        seekPhone()    
    if option == 5:
        delete()
    if option == 6:
        print("Hasta pronto")
        break