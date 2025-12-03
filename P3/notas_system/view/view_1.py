from tkinter import *
from tkinter import messagebox
from controller import controlador_1

class View:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Notas System")
        ventana.geometry("800x600")
        ventana.resizable(0, 0)
        self.menu_principal(ventana)

    @staticmethod
    def borrar_pantalla(ventana):
        for w in ventana.winfo_children():
            w.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Menu Principal", justify="center")
        lbl_titulo.pack(pady=10)

        btn_registro = Button(ventana, text="1.- Registro", command=lambda: View.registro(ventana))
        btn_registro.pack(pady=15)

        btn_login = Button(ventana, text="2.- Login", command=lambda: View.login(ventana))
        btn_login.pack(pady=15)

        btn_salir = Button(ventana, text="3.- Salir", command=ventana.quit)
        btn_salir.pack(pady=15)

    @staticmethod
    def registro(ventana):
        View.borrar_pantalla(ventana)
        lbl_titulo = Label(ventana, text="Registro de Notas", justify="center")
        lbl_titulo.pack(pady=10)

        lbl_nombre = Label(ventana, text="Cual es su nombre?:", justify="center")
        lbl_nombre.pack(pady=10)
        entry_nombre = Entry(ventana, textvariable=lbl_nombre, width=15, justify="center")
        entry_nombre.focus() 
        entry_nombre.pack(pady=10,anchor="center",side="top")

        lbl_apellidos = Label(ventana, text="Cuales son tus apellidos?:", justify="center")
        lbl_apellidos.pack(pady=10)
        entry_apellidos = Entry(ventana, textvariable=lbl_apellidos, width=15, justify="center")
        entry_apellidos.pack(pady=10,anchor="center",side="top")

        lbl_email = Label(ventana, text="Ingresa tu email:", justify="center")
        lbl_email.pack(pady=10)
        entry_email= Entry(ventana, textvariable=lbl_email, width=15, justify="center")
        entry_email.pack(pady=10,anchor="center",side="top")

        lbl_pass = Label(ventana, text="Ingresa tu contrasena:", justify="center")
        lbl_pass.pack(pady=10)
        entry_pass= Entry(ventana, textvariable=lbl_pass, width=15, justify="center", show="*")
        entry_pass.pack(pady=10,anchor="center",side="top")

        btn_registrar = Button(ventana, text="Registrar", command=lambda: {controlador_1.Controlador.registro(entry_nombre.get(),
                                                                    entry_apellidos.get(),entry_email.get(), entry_pass.get()),
                                                                    View.login(ventana)
                                                                    }
                                                                    )
        btn_registrar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def login(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Inicio de Sesion", justify="center")
        lbl_titulo.pack(pady=10)

        lbl_email = Label(ventana, text="Ingresa tu email:", justify="center")
        lbl_email.pack(pady=10)
        entry_email= Entry(ventana, textvariable=lbl_email, width=15, justify="center")
        entry_email.focus()
        entry_email.pack(pady=10,anchor="center",side="top")

        lbl_pass = Label(ventana, text="Ingresa tu contrasena:", justify="center")
        lbl_pass.pack(pady=10)
        entry_pass= Entry(ventana, textvariable=lbl_pass, width=15, justify="center", show="*")
        entry_pass.pack(pady=10,anchor="center",side="top")

        btn_entrar = Button(ventana, text="Entrar", command=lambda: controlador_1.Controlador.login(ventana, entry_email.get(), entry_pass.get()))
        btn_entrar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=15)

    @staticmethod
    def menu_notas(ventana, usuario_id, nombre, apellidos):
        View.borrar_pantalla(ventana)

        global id_user, nom_user, ape_user
        id_user = usuario_id
        nom_user = nombre
        ape_user = apellidos


        lbl_titulo = Label(ventana, text=f"Bienvenido {nombre} {apellidos}, has iniciado Sesion", justify="center")
        lbl_titulo.pack(pady=10)

        btn_crear= Button(ventana, text="1.- Crear", command=lambda: View.crear_nota(ventana, usuario_id, nombre, apellidos))
        btn_crear.pack(pady=15)

        btn_mostrar = Button(ventana, text="2.- Mostrar", command=lambda: View.mostrar_notas(ventana, usuario_id, nombre, apellidos))
        btn_mostrar.pack(pady=15)

        btn_cambiar = Button(ventana, text="3.- Cambiar", command=lambda: View.cambiar_notas(ventana, usuario_id, nombre, apellidos))
        btn_cambiar.pack(pady=15)

        btn_eliminar = Button(ventana, text="4.- Eliminar", command=lambda: View.eliminar_nota(ventana, usuario_id, nombre, apellidos))
        btn_eliminar.pack(pady=15)
        
        btn_regresar = Button(ventana, text="5.- Regresar", command=lambda: View.login(ventana))
        btn_regresar.pack(pady=15)

    @staticmethod
    def crear_nota(ventana, id_user, nom_user, ape_user):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f"Crear Nota", justify="center")
        lbl_titulo.pack(pady=10)

        lbl_titulo_2= Label(ventana, text=f"Titulo: ", justify="center")
        lbl_titulo_2.pack(pady=10)
        entry_titulo = Entry(ventana, textvariable=lbl_titulo_2, width=15, justify="center")
        entry_titulo.focus()
        entry_titulo.pack(pady=10,anchor="center",side="top")

        lbl_desc= Label(ventana, text=f"Descripcion: ", justify="center")
        lbl_desc.pack(pady=10)
        entry_desc = Entry(ventana, textvariable=lbl_desc, width=15, justify="center")
        entry_desc.pack(pady=10,anchor="center",side="top")

        btn_guardar = Button(ventana, text="Guardar", command=lambda: controlador_1.Controlador.crear_nota(id_user, entry_titulo.get(), entry_desc.get()))
        btn_guardar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=15)

    @staticmethod
    def mostrar_notas(ventana):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text=f"Usuario, tus notas son: ", justify="center")
        lbl_titulo.pack(pady=10)

        filas = ""
        registros = controlador_1.Controlador.mostrar_nota(id_user)
        if len(registros) < 0:
            messagebox.showerror(message="No existen notas para este usuario")
        for f in registros:
            filas += f"Nota: {f[0]}, ID: {1}, Titulo: {f[2]}, Descipcion: {f[3]}, Fecha: {f[-1]}"
        lbl_notas = Label(ventana, text=f"{filas}")
        lbl_notas.pack(pady=10)

        btn_volver = Button(ventana, text="Volver", command=lambda:View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=15)

    @staticmethod
    def cambiar_notas(ventana, usuario_id, nombre, apellidos):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Usuario, vamos a modificar una nota")
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la nota a cambiar: ")
        lbl_id.pack(pady=10)
        entry_id = Entry(ventana, textvariable=lbl_id, width=15, justify="center")
        entry_id.focus()
        entry_id.pack(pady=10, anchor="center", side="top")

        lbl_nuevo = Label(ventana, text="Nuevo Titulo: ")
        lbl_nuevo.pack(pady=10)
        entry_nuevo = Entry(ventana, textvariable=lbl_nuevo, width=15, justify="center")
        entry_nuevo.pack(pady=10, anchor="center", side="top")

        lbl_desc = Label(ventana, text="Nueva Descripcion: ")
        lbl_desc.pack(pady=10)
        entry_desc = Entry(ventana, textvariable=lbl_desc, width=15, justify="center")
        entry_desc.pack(pady=10, anchor="center", side="top")

        btn_guardar = Button(ventana, text="Guardar", command=lambda: View.menu_notas(ventana))
        btn_guardar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=15)

    @staticmethod
    def eliminar_nota(ventana, usuario_id, nombre, apellidos):
        View.borrar_pantalla(ventana)

        lbl_titulo = Label(ventana, text="Usuario, vamos a eliminar una Nota")
        lbl_titulo.pack(pady=10)

        lbl_id = Label(ventana, text="ID de la Nota a eliminar: ")
        lbl_id.pack(pady=10)
        entry_id = Entry(ventana, textvariable=lbl_id, width=15, justify="center")
        entry_id.pack(pady=10, anchor="center", side="top")

        btn_eliminar = Button(ventana, text="Eliminar", command=lambda: View.menu_notas(ventana))
        btn_eliminar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_notas(ventana, id_user, nom_user, ape_user))
        btn_volver.pack(pady=15)