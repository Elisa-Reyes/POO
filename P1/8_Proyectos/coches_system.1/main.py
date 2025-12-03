#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD
import os

def borrarPantalla():
   os.system("cls") 

def esperaTecla():
    input("\n\t... Oprima una tecla para continuar ...")   

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def respuesta_resultados(respuesta):
    if respuesta:
        print("Registro insertado correctamente")
    else:
        print("No fue posible insertar el registro, intenta lo nuevamente ...")

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def menu_acciones(tipo):
    print(f"\n\t\tMenú de {tipo}\n\t1.- Insertar \n\t2.-consultar \n\t3.- Actualizar \n\t4.- Eliminar \n\t Regresar")
    op=input("Elige una opcion...").upper().strip()
    return op


def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    #Agregar en la BD
    auto=cochesBD.Autos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    respuesta=auto.insertar()
    respuesta_resultados(respuesta)

            
def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")

    respuesta=cochesBD.Camionetas.insertar(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.cerrada,coche.traccion)
    respuesta_resultados(respuesta)

def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")

    respuesta=cochesBD.Camionetas.insertar(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga)
    respuesta_resultados(respuesta)

def main():
   opcion=True
   while opcion:
    os.system("clear")
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            autos()
            esperaTecla()
        case "2":
            camionetas()
            esperaTecla()  
        case "3":
            camiones()
            esperaTecla()
        case "4":
            borrarPantalla()
            input("\n\t\tSalir del Sistema")
            opcion=False   
        case _:
            input("\n\tOpcion invalidad ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    main()

