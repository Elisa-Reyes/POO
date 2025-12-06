<<<<<<< HEAD
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
=======
from tkinter import *
from controller import controlador

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
        camionetas=Button(ventana,text="Camionetas",command=lambda: self.menu_acciones(ventana,"camionetas"))
        camionetas.pack(pady=10)
        camiones=Button(ventana,text="Camiones",command=lambda: self.menu_acciones(ventana,"camiones"))
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
        #marca,color,modelo,velocidad,potencia,plazas
        marca=Label(ventana,text="marca:")
        marca.pack(pady=10)
        marca=Entry(ventana)
        marca.pack(pady=10)
        Label(ventana,text="color:").pack()
        color=Entry(ventana)
        color.pack(pady=10)
        Label(ventana,text="modelo:").pack()
        modelo=Entry(ventana)
        modelo.pack(pady=10)
        Label(ventana,text="velocidad:").pack()
        velocidad=Entry(ventana)
        velocidad.pack(pady=10)
        Label(ventana,text="potencia:").pack()
        potencia=Entry(ventana)
        potencia.pack(pady=10)
        Label(ventana,text="plazas:").pack()
        plazas=Entry(ventana)
        plazas.pack(pady=10)

        if tipo=="camiones":
            Label(ventana,text="tracción:").pack()
            traccion=Entry(ventana)
            traccion.pack(pady=10)  
            Label(ventana,text="cerrada o abierto: ").pack() 
            cerrada=Entry(ventana)
            cerrada.pack(pady=10) 
        elif tipo=="camionetas":
            Label(ventana,text="eje:").pack()
            eje=Entry(ventana)
            eje.pack(pady=10)
            Label(ventana,text="capacidad de carga:").pack()
            capacidadCarga=Entry(ventana)
            capacidadCarga.pack(pady=10)

        ok=Button(ventana,text="guardar")
        ok.pack()

        if tipo=="camiones":
            ok.config(command=lambda: controlador.Camion.insertar(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada))
        elif tipo=="camionetas":
            ok.config(command= lambda: controlador.Camioneta.insertar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga))
        else:
            ok.config(command=lambda: controlador.Auto.insertar(marca,color,modelo,velocidad,potencia,plazas))

        self.regresar(ventana,tipo)      

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
        buscar=Button(ventana,text="Buscar",command= lambda:"")
        buscar.pack()

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
        confirmar=Button(ventana,text="Borrar",command= lambda:"")
        confirmar.pack()
>>>>>>> master
        self.regresar(ventana,tipo)