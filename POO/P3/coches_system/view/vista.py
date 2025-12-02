from tkinter import *

class View:
    def __init__(self,ventana):
        self.ventana=ventana

    #@staticmethod
    def borrarPantalla(self,ventana):
        for widget in ventana.wifo_children():
            widget.destroy()
    
    def menu_principal(self,ventana):
        self.borrarPantalla(self,ventana)
        Label(ventana,text="").pack(pady=5)

        autos=Button(ventana,text="Autos",command= lambda: self.menu_acciones(self,ventana,autos))
        autos.pack()
        camionetas=Button(ventana,text="camionetas",command=lambda: self.menu_acciones(self,ventana,camionetas))
        camionetas.pack()
        camiones=Button(ventana,text="camiones",command=lambda: self.menu_acciones(self,ventana,camiones))
        camiones.pack()

    def menu_acciones(self,ventana,tipo):
        self.borrarPantalla(self,ventana)
        text= Label(ventana, text=f"Acciones para el vehículo: {tipo}")
        text.pack()

        inser=Button(ventana, text="Insertar Vehículo", command= lambda: self.insertar_autos(self,ventana,tipo))
        inser.pack()
        con=Button(ventana, text="Ver Vehículos", command= lambda:self.consultar_autos(self,ventana,tipo))
        con.pack()
        cam=Button(ventana, text="Cambiar Vehículo", command= lambda:self.cambiar_autos(self,ventana,tipo))
        cam.pack()
        eli=Button(ventana, text="Eliminar Vehículo", command= lambda:self.borrar_autos(self,ventana,tipo))
        eli.pack()

    def insertar_autos(self,ventana,tipo):
        text= Label(ventana, text=f"Insertar Nuevo: {tipo}")
        text.pack()        

    def consultar_autos(self,ventana,tipo):
        text= Label(ventana, text=f"Consultar: {tipo}")
        text.pack()


    def cambiar_autos(self,ventana,tipo):
        text= Label(ventana, text=f"Cambiar: {tipo}")
        text.pack()

        text= Label(ventana, text=f"Id del {tipo} a cambiar:")
        text.pack()
        id=IntVar()
        ent=Entry(ventana,textvariable=id)

    def borrar_autos(self,ventana,tipo):
        text= Label(ventana, text=f"Acciones para el vehículo: {tipo}")
        text.pack()

        text= Label(ventana, text=f"Id del {tipo} a borrar:")
        text.pack()
        id=IntVar()
        ent=Entry(ventana,textvariable=id)