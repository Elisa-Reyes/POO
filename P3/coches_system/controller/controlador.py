from tkinter import *
from tkinter import messagebox
from model import modelo

class Auto:
    @staticmethod
    def eliminar(id):
        respuesta=modelo.Autos.eliminar(id)
        Auto.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def cambiar(marca,color,model,velocidad,potencia,plazas,id):
        respuesta= modelo.Autos.actualizar(marca,color,model,velocidad,potencia,plazas,id)
        Auto.respuesta_sql("Cambiar",respuesta)

    @staticmethod
    def insertar(marca,color,model,velocidad,potencia,plazas):
        respuesta= modelo.Autos.insertar(marca,color,model,velocidad,potencia,plazas)
        Auto.respuesta_sql("Insertar",respuesta)

    @staticmethod
    def consultar():
        registros=modelo.Autos.consultar()  

    @staticmethod
    def respuesta_sql(titulo,result):
        if result:
            messagebox.showinfo(icon="info",message="Accion realizada con exito",title=titulo)
        else:
            messagebox.showinfo(icon="info",message="No fue posible",title=titulo)

class Camion:
    @staticmethod
    def eliminar(id):
        respuesta=modelo.Camiones.eliminar(id)
        Auto.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def cambiar(marca,color,model,velocidad,potencia,plazas,traccion,cerrada,id):
        respuesta= modelo.Camiones.actualizar(marca,color,model,velocidad,potencia,plazas,traccion,cerrada,id)
        Auto.respuesta_sql("Cambiar",respuesta)

    @staticmethod
    def insertar(marca,color,model,velocidad,potencia,plazas,traccion,cerrada):
        respuesta= modelo.Camiones.insertar(marca,color,model,velocidad,potencia,plazas,traccion,cerrada)
        Auto.respuesta_sql("insertar",respuesta)

    @staticmethod
    def consultar():
        registros=modelo.Camiones.consultar()
        return registros

class Camioneta:
    @staticmethod
    def eliminar(id):
        respuesta=modelo.Camionetas.eliminar(id)
        Auto.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def cambiar(marca,color,model,velocidad,potencia,plazas,eje,capacidadCarga):
        respuesta= modelo.Camionetas.actualizar(marca,color,model,velocidad,potencia,plazas,eje,capacidadCarga)
        Auto.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def insertar(marca,color,model,velocidad,potencia,plazas,eje,capacidadCarga):
        respuesta= modelo.Camionetas.insertar(marca,color,model,velocidad,potencia,plazas,eje,capacidadCarga)
        Auto.respuesta_sql("Eliminar",respuesta)

    @staticmethod
    def consultar():
        registros=modelo.Camionetas.consultar()
        return registros