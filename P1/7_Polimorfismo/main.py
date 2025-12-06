import coches
import os
#from coches import *
#from coches import Coches

def datos_generales(tipo):
    print(f"\tIngresar datos del {tipo}")
    marca=input("marca: ")
    color=input("color: ")
    modelo=input("modelo:")
    velocidad=int(input("velocidad: "))
    potencia=int(input("potencia: "))
    plazas=int(input("plazas: "))
    return marca, color, modelo, velocidad, potencia, plazas

def borrarPant():
    os.system("cls")

def espereTecla():
    input("Espere tecla...")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_generales("Auto")

    coche1=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"datos del vehiculo: {coche1.marca}")

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_generales("Camion")
    eje=input("ejes: ")
    capacidad=input("capacidad: ")

    camion=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidad)
    print(f"datos del vehiculo: {camion.marca}")

def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_generales("Camioneta")
    traccion=input("Traccion: ")
    cerrada=input("cerrada? si/no ").lower().strip()
    if cerrada=="si":
        cerrada=True
    else:
        cerrada=False

    camioneta=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    print(f"datos del vehiculo: {camioneta.marca}")

def main():
    option=True
    while option:
        print("\t\tCARROS Y OTRO TIPO Y ASI \n1. Autos\n2. Camionetas \n3. Camiones \n4. Salir")
        opcion=input("\t\tQué deseas hacer? ")
    
        match opcion:
            case "1":
                autos()
                input("Tecla para continuar...")
            case "2":
                camionetas()
                input("Tecla para continuar...")
            case "3":
                camiones()
                input("Tecla para continuar...")
            case "4":
                option=False
            case _:
                input("Opcion invalida...")

if __name__=="__main__":
    main()
