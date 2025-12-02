from tkinter import messagebox
from model import usuario, nota
from view import view_1

class Controlador:

    #Usuarios
    @staticmethod
    def registro(nombre, apellidos, email, password):
        resultado = usuario.Usuario.registrar(nombre, apellidos, email, password)
        if resultado:
            messagebox.showinfo(message=f"{nombre} {apellidos}, se registro correctamente, con el email: {email}",
                                title="Registro")
        else:
            messagebox.showerror(message="No se pudo registrar el usuario correctamente, intente de nuevo mas tarde",
                                 title="Registro")

    @staticmethod
    def login(ventana, email, password):
        registro = usuario.Usuario.iniciar_sesion(email, password)
        if registro:
            messagebox.showinfo(message=f"{registro[1]} {registro[2]} has iniciado sesion correctamente!",
                                title="Inicio sesion")
            view_1.View.menu_notas(ventana, registro[0], registro[1], registro[2])
        else:
            messagebox.showwarning(message="Usuario y/o contraseña incorrectas. Por favor, intente de nuevo",
                                 title="Registro")

    #Notas
    @staticmethod
    def crear_nota(usuario_id, titulo, descripcion):
        respuesta = nota.Nota.crear(usuario_id, titulo, descripcion)
        Controlador.respuesta_sql( "Crear", respuesta)

    @staticmethod
    def mostrar_nota(usuario_id):
        registros = nota.Nota.mostrar(usuario_id)

        return registros
    
            
    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo,message=f"Accion realizada exitosamente")
        else:
            messagebox.showerror(title=titulo,message=f"Fallo al realizar la accion")

    
                 