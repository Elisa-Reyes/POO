from tkinter import *
from tkinter import messagebox
from view import vista
from model import model
class Controlador:
    @staticmethod
    def login(email,password):
        #registro=usuario.Usuario.iniciar_sesion(email,)
        pass

    @staticmethod
    def crear_nota(usuario_id,titulo,descripcion):
        respuesta=model.Nota.crear(usuario_id,titulo,descripcion)
        Controlador.respuesta_sql("Crear Nota",respuesta)

    @staticmethod
    def respuesta_sql(titulo,result):
        if result:
            messagebox.showinfo(icon="info",message="Accion realizada con exito",title=titulo)
        else:
            messagebox.showinfo(icon="info",message="No fue posible",title=titulo)