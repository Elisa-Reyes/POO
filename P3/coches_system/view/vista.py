from tkinter import *

class View:
    def __init__(self,ventana):
        ventana.title("Coches")
        # ventana.geometry("1024x768")
        ventana.geometry("800x400")
        ventana.config(bg="#bea9f7")
        self.menu_principal(ventana)

    #@staticmethod
    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def regresar(self,ventana,tipo):
        regresar=Button(ventana,text="regresar", command= lambda: self.menu_acciones(ventana,tipo))
        regresar.pack(pady=10)
    
    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        Label(ventana,text="VEHÍCULOS!!!1!!1",font=("Times New Roman", 30),bg="#bea9f7").pack(pady=10)

        autos=Button(ventana,text="Autos",command= lambda: self.menu_acciones(ventana,"autos"))
        autos.pack(pady=10)
        camionetas=Button(ventana,text="camionetas",command=lambda: self.menu_acciones(ventana,"camionetas"))
        camionetas.pack(pady=10)
        camiones=Button(ventana,text="camiones",command=lambda: self.menu_acciones(ventana,"camiones"))
        camiones.pack(pady=10)
        salir=Button(ventana,text="Salir",command=ventana.quit,bg="#34edb9")
        salir.pack(pady=10)

    def menu_acciones(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"Acciones para: {tipo}",font=("Times New Roman", 30),bg="#bea9f7")
        text.pack(pady=10)

        inser=Button(ventana, text="Insertar Vehículo", command= lambda: self.insertar_vehiculos(ventana,tipo))
        inser.pack(pady=10)
        con=Button(ventana, text="Ver Vehículos", command= lambda:self.consultar_vehiculos(ventana,tipo))
        con.pack(pady=10)
        cam=Button(ventana, text="Cambiar Vehículo", command= lambda:self.cambiar_vehiculos(ventana,tipo))
        cam.pack(pady=10)
        eli=Button(ventana, text="Eliminar Vehículo", command= lambda:self.borrar_vehiculos(ventana,tipo))
        eli.pack(pady=10)
        reg=Button(ventana,text="regresar", command= lambda: self.menu_principal(ventana))
        reg.pack()

    def insertar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"Insertar Nuevo: {tipo}",font=("Times New Roman", 30),bg="#bea9f7")
        text.pack(pady=10)  
        self.regresar(ventana)      

    def consultar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"Consultar: {tipo}",font=("Times New Roman", 30),bg="#bea9f7")
        text.pack(pady=10)
        self.regresar(ventana,tipo)


    def cambiar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"Cambiar: {tipo}",font=("Times New Roman", 30),bg="#bea9f7")
        text.pack(pady=10)

        text= Label(ventana, text=f"Id del vehículo a cambiar:")
        text.pack(pady=10)
        id=IntVar()
        ent=Entry(ventana,textvariable=id)
        ent.pack(pady=10)
        self.regresar(ventana,tipo)

    def borrar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"Borrar {tipo}",font=("Times New Roman", 30),bg="#bea9f7")
        text.pack(pady=10)

        text= Label(ventana, text=f"Id a borrar:")
        text.pack(pady=10)
        id=IntVar()
        ent=Entry(ventana,textvariable=id)
        ent.pack(pady=10)
        self.regresar(ventana,tipo)