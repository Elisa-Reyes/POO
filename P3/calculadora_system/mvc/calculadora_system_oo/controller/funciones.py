from tkinter import *
from tkinter import messagebox
from model import operacion

class Controladores:
    @staticmethod
    def operaciones(n1,n2,op):
        if op=="+":
            resultado= n1+n2  
        elif op=="-":
            resultado= n1-n2
        elif op=="*":
            resultado= n1*n2
        elif op=="/":
            resultado= n1/n2
        result= messagebox.showinfo(message=f"{n1}{op}{n2}={resultado} \n quieres guardar la operacion en la base de datos?",icon="question")
        if result:
            operacion.Operaciones.insertar(n1,n2,op,resultado)
            Controladores.respuesta_sql("Registro",result)

    @staticmethod
    def eliminar(id):
        respuesta= operacion.Operaciones.eliminar(id)
        Controladores.respuesta_sql("Eliminar registro",respuesta)

    @staticmethod
    def cambiar(n1,n2,signo,resul,id):
        respuesta= operacion.Operaciones.actualizar(n1,n2,signo,resul,id)
        Controladores.respuesta_sql("Cambiar registro",respuesta)

    @staticmethod
    def consultar():
        registros=operacion.Operaciones.consultar()  

    @staticmethod
    def respuesta_sql(titulo,result):
        if result:
            messagebox.showinfo(icon="info",message="Accion realizada con exito",title=titulo)
        else:
            messagebox.showinfo(icon="info",message="No fue posible",title=titulo)