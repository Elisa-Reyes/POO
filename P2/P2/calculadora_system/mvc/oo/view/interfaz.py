from tkinter import *
from controller import funciones
import os
from model import operacion
from tkinter import messagebox


class Vistas:
    def __init__(self,ventana):
        ventana.title("Calculadora")
        # ventana.geometry("1024x768")
        ventana.geometry("800x400")
        ventana.config(bg="#f7a9ee")
        self.interfaz(ventana)
        
    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        texto=Label(ventana, text="Número 1:",font=30,bg="#f7a9ee")
        texto.pack()

        n1=IntVar()
        num1=Entry(ventana,width=10,justify=RIGHT,textvariable=n1)
        num1.focus()
        num1.pack(pady=10)

        #texto 2

        texto2=Label(ventana, text="Número 2:",font=30,bg="#f7a9ee")
        texto2.pack(pady=10)

        n2=IntVar()
        num2=Entry(ventana,width=10,justify=RIGHT,textvariable=n2)
        num2.focus()
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
    
    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
        
    def borrarInt(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        lab=Label(ventana,text="Borrar una Operacion", font=20)
        lab.pack(pady=10)
        lab2=Label(ventana,text="ID de la Operacion:")
        lab2.pack(pady=10)

        id=IntVar()
        ent=Entry(ventana, width=30,textvariable=id)
        ent.focus()
        ent.pack(pady=10)
        elim=Button(ventana,text="Eliminar",command=lambda: funciones.Controladores.eliminar(ent.get()))
        elim.pack(pady=10)
        volver=Button(ventana,text="Volver",command=lambda: self.interfaz(ventana))
        volver.pack(pady=10)


    def consultarInt(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        texto=operacion.Operaciones.consultar()
        lab=Label(ventana, text="CONSULTAR OPERACIONES")
        lab.pack(pady=10)

        filas=""
        if len(texto)>0:
            num_operaciones=1
            for fila in texto:
                filas=f"\n Operacion: {num_operaciones} ID: {fila[0]} Fecha: {fila[1]}\n Operacion: {fila[2]}{fila[4]}{fila[3]}={fila[5]}"
                num_operaciones=+1
                Label(ventana, text=filas).pack(pady=5)

            funciones.Controladores.consultar()
        else:
            messagebox.showwarning(message="No hay operaciones guardads...")

        volver=Button(ventana,text="Volver",command=lambda: self.interfaz(ventana))
        volver.pack(pady=10)

    def cambiarInt(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)

        titulo=Label(ventana,text="CAMBIAR DE OPERACION",font=20).pack(pady=10)

        op=Label(ventana,text="ID de la Operación:")
        op.pack(pady=10)
        n=IntVar()
        num=Entry(ventana,textvariable=n)
        num.pack(pady=10)

        texto=Label(ventana, text="Nuevo Número 1:",font=30,bg="#f7a9ee")
        texto.pack(pady=10)

        n1=IntVar()
        num1=Entry(ventana,width=10,justify=RIGHT,textvariable=n1)
        num1.focus()
        num1.pack(pady=10)

        texto2=Label(ventana, text="Nuevo Número 2:",font=30,bg="#f7a9ee")
        texto2.pack(pady=10)

        n2=IntVar()
        num2=Entry(ventana,width=10,justify=RIGHT,textvariable=n2)
        num2.focus()
        num2.pack(pady=10)

        texto3=Label(ventana, text="Nuevo Signo:",font=30,bg="#f7a9ee")
        texto3.pack(pady=10)
        signo=Entry(ventana,width=10)
        signo.pack(pady=10)

        texto4=Label(ventana, text="Nuevo Resultado:",font=30,bg="#f7a9ee")
        texto4.pack(pady=10)
        result=Entry(ventana,width=10)
        result.pack(pady=10)

        guardar=Button(ventana,text="Guardar",command=lambda: funciones.Controladores.cambiar(num1.get(),num2.get(),signo.get(),result.get(),num.get()))
        guardar.pack(pady=10)

        volver=Button(ventana,text="Volver",command=lambda: self.interfaz(ventana))
        volver.pack(pady=10)

    def menuPrincipal(self,ventana):

        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)
        operacionesMenu=Menu(menuBar, tearoff=False)

        menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar", command=lambda: self.interfaz(ventana))
        operacionesMenu.add_command(label="Consultar", command=lambda: self.consultarInt(ventana))
        operacionesMenu.add_command(label="Cambiar", command=lambda: self.cambiarInt(ventana))
        operacionesMenu.add_command(label="Borrar", command=lambda: self.borrarInt(ventana))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir", command=ventana.quit)

                