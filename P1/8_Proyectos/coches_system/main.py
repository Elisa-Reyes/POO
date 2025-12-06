from model import coches,cochesBD
import os

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\n \t \tOprima tecla para continuar... ")

    def datos_autos(self,tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresa los siguientes datos del vehículo de tipo: '{tipo}' ...")
        marca=input("Marca: ").upper()
        color=input("Color: ").upper()
        modelo=input("Modelo: ").upper()
        velocidad=int(input("Velocidad: "))
        potencia=int(input("Potencia: "))
        plazas=int(input("Plazas: "))
        return marca,color,modelo,velocidad,potencia,plazas

    def imprimir_datos_vehiculo(self,marca,color,modelo,velocidad,potencia,plazas):
        print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n Color: {color} \n Modelo: {modelo} \n Velocidad: {velocidad} \n Caballaje: {potencia} \n Plazas: {plazas}")

    def respuesta_sql(self,respuesta):
        if respuesta:
            print("\n\t... ¡ Accion realizada con Éxito !...")
        else:
            print("\n\t... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...") 

    def autos(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Auto")
        coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
        self.borrarPantalla()
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas
        
    def camionetas(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camioneta")
        traccion=input("Traccion: ").upper().strip()
        cerrada=input("Cerrada (SI/NO): ").upper().strip()
        if cerrada=="SI":
            cerrada=True
        else:
            cerrada=False    
        coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
        self.borrarPantalla()
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f" Traccion: {coche.traccion}\n Cerrada: {coche.cerrada}")
        return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada 

    def camiones(self):
        marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camión")
        eje=int(input("No.de ejes: "))
        capacidadCarga=int(input("Capacidad de carga: "))
        coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
        self.borrarPantalla()
        self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
        print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
        return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga

    def menu_acciones(self,tipo):
        print(f"\n\t\t.::  Menu de {tipo} ::.\n\t1.- Insertar \n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar ")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion

    def menu_autos(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Autos")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla()
                marca,color,modelo,velocidad,caballaje,plazas=self.autos()
                #Agregar a BD
                auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
                respuesta=auto.insertar()
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla()  
                registros=cochesBD.Autos.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}") 
                        num_autos+=1    
                        self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                print(f"\n \t .:: Actualizar Auto ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas=self.autos() 
                respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla()
                print(f"\n \t .:: Eliminar Auto ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Autos.eliminar(id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def menu_camionetas(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Camionetas")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla()
                marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                respuesta=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla()  
                registros=cochesBD.Camionetas.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nCamioneta #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}\nTracción: {fila[7]}\nCerrada: {fila[8]}") 
                        num_autos+=1    
                        self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                print(f"\n \t .:: Actualizar Camioneta ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                respuesta=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
                self.respuesta_sql(respuesta)
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla()
                print(f"\n \t .:: Eliminar Camioneta ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Camionetas.eliminar(id)
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def menu_camiones(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Camiones")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla()
                marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=self.camiones()
                respuesta=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
                self.respuesta_sql(respuesta)
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla()  
                registros=cochesBD.Camiones.consultar()
                if len(registros)>0:
                    num_autos=1
                    for fila in registros:
                        print(f"\nCamion # {num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}\nNo. ejes: {fila[7]}\nCapacidad de Carga: {fila[8]}") 
                        num_autos+=1    
                        self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                print(f"\n \t .:: Actualizar Camion ::. \n")
                id=input("\nID: ")
                marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=self.camiones()
                #Actualizar BD
                respuesta=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
                self.respuesta_sql(respuesta)
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla()
                print(f"\n \t .:: Eliminar Camion ::. \n")
                id=input("\nID: ")
                respuesta=cochesBD.Camiones.eliminar(id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def main(self):
        opcion=1
        while opcion!="4":
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.-Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_autos() 
                case "2":
                    self.menu_camionetas() 
                case "3":
                    self.menu_camiones()
                case "4":
                    self.borrarPantalla()
                    print("\n\t\t¡Gracias por utilizar el sistema!")
                    self.esperarTecla()    
                case _:
                    input("\nOpcion invalidad ... vuelva a intertarlo ... ") 
        
if __name__ == "__main__":
  app=App()
