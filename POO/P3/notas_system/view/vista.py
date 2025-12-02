from tkinter import *

class View:
    def __init__(self,ventana):
        self.ventana=ventana

    @staticmethod
    def borrarPantalla(self,ventana):
        for widget in ventana.wifo_children():
            widget.destroy()

    @staticmethod
    def menu(self,ventana):
        self.borrarPantalla
        lab=Label(ventana, text="Menu Principal")
        lab.pack(pady=10)
        reg=Button(ventana,text="Registrarse", command= lambda: self.registro(ventana))
        reg.pack(pady=10)
        log=Button(ventana,text="Iniciar Sesión", command= lambda: self.login(ventana))
        log.pack
        salir=Button(ventana,text="Salir",command=ventana.quit)
        salir.pack(pady=10)

    @staticmethod
    def registro(self,ventana):
        self.borrarPantalla()
        lbl=Label(ventana,text="Registro")
        lbl.pack(pady=10)
        nombre=Label(ventana,text="Nombre:")
        nombre.pack(pady=10)
        name=Entry(ventana)
        name.pack(pady=10)
        apellido=Label(ventana,text="Apellido:")
        apellido.pack(pady=10)
        ape=Entry(ventana)
        ape.pack(pady=10)
        email=Label(ventana,text="E-mail:")
        email.pack(pady=10)
        em=Entry(ventana)
        em.pack(pady=10)
        contraseña=Label(ventana,text="Contraseña:")
        contraseña.pack(pady=10)
        passw=Entry(ventana)
        passw.pack(pady=10)
        reg=Button(ventana,text="Registrarse",command=lambda:self.menu_notas(ventana))
        reg.pack(pady=10)
        volver=Button(ventana,text="volver",command=lambda:self.menu(ventana))
        volver.pack(pady=10)

    
    @staticmethod
    def login(self,ventana):
        self.borrarPantalla
        lab=Label(ventana,text="Iniciar Sesión").pack()
        email=Label(ventana,text="E-mail:")
        email.pack(pady=10)
        em=Entry(ventana)
        em.pack(pady=10)
        contraseña=Label(ventana,text="Contraseña:")
        contraseña.pack(pady=10)
        reg=Button(ventana,text="Registrarse",command=lambda:self.menu_notas(ventana))
        reg.pack(pady=10)

    @staticmethod
    def menu_notas(self,ventana):

        labl=Label(ventana,text="Notas")
        labl.pack(pady=10)
        crear=Button(ventana,text="Crear")
        crear.pack(pady=10)
        mostrar=Button(ventana,text="mostrar")
        mostrar.pack(pady=10)
        cambiar=Button(ventana,text="cambiar")
        cambiar.pack(pady=10)  
        eliminar=Button(ventana,text="eliminar")
        eliminar.pack(pady=10) 
        regresar=Button(ventana,text="regresar",command=lambda:self.menu(ventana))
        regresar.pack(pady=10)  
           

    @staticmethod
    def mostrar(self,ventana):
        self.borrarPantalla(ventana)

    @staticmethod
    def borrar(self,ventana):
        self.borrarPantalla(ventana)
        