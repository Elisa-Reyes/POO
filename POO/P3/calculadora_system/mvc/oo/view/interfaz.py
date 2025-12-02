from tkinter import *
from controller import funciones
#texto 1

class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        ventana.geometry("1024x768")
        ventana.config(bg="#f7a9ee")
        self.interfaz(ventana)

    def interfaz(self,ventana):

        texto=Label(ventana, text="Número 1:",font=30,bg="#f7a9ee")
        texto.pack()

        n1=IntVar()
        num1=Entry(ventana,width=10,justify=RIGHT,textvariable=n1)
        num1.pack(pady=10)

        #texto 2

        texto2=Label(ventana, text="Número 2:",font=30,bg="#f7a9ee")
        texto2.pack(pady=10)

        n2=IntVar()
        num2=Entry(ventana,width=10,justify=RIGHT,textvariable=n2)
        num2.pack(pady=10)

        #botones
        frame = Frame(ventana,bg="#f7a9ee") 
        frame.pack(pady=10)
        suma=Button(frame,command=lambda: funciones.Controladores.operaciones(n1.get(),n2.get(),"+"), text="+")
        
        resta=Button(frame,command=lambda: funciones.Controladores.operaciones(n1.get(),n2.get(),"-"), text="-")
        
        mult=Button(frame,command=lambda: funciones.Controladores.operaciones(n1.get(),n2.get(),"*"), text="*")
        
        div=Button(frame,command=lambda: funciones.Controladores.operaciones(n1.get(),n2.get(),"/"), text="/")
        
        suma.grid(row=5, column=0,padx=5) 
        resta.grid(row=5, column=1,padx=5)
        mult.grid(row=5, column=2,padx=5)
        div.grid(row=5, column=3,padx=5)

        salir=Button(ventana,text="Salir",command=ventana.quit,bg="#34edb9")
        salir.pack()

        def menuPrincipal(self,ventana):

            menuBar=Menu(ventana)
            ventana.config(menu=menuBar)
            operacionesMenu=Menu(menuBar, tearoff=False)

            menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)
            operacionesMenu.add_command(label="Agregar", command=lambda: "")
            operacionesMenu.add_command(label="Consultar", command=lambda: "")
            operacionesMenu.add_command(label="Cambiar", command=lambda: "")
            operacionesMenu.add_command(label="Borrar", command=lambda: "")
            operacionesMenu.add_separator()
            operacionesMenu.add_command(label="Salir", command=ventana.quit)

                