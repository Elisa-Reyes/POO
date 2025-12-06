from tkinter import *
from controller import funciones
#texto 1

def interfaz():
    ventana=Tk()
    ventana.title("Calculadora")
    ventana.geometry("800x600")
    ventana.config(bg="#ff00e1")

    texto=Label(ventana, text="Número 1:",font=30,bg="#ff00e1")
    texto.pack()

    n1=IntVar()
    num1=Entry(ventana,width=10,justify=RIGHT,textvariable=n1)
    num1.pack(pady=10)

    #texto 2

    texto2=Label(ventana, text="Número 2:",font=30,bg="#ff00e1")
    texto2.pack(pady=10)

    n2=IntVar()
    num2=Entry(ventana,width=10,justify=RIGHT,textvariable=n2)
    num2.pack(pady=10)

    #botones
    frame = Frame(ventana,bg="#ff00e1") 
    frame.pack(pady=10)
    suma=Button(frame,command=lambda: funciones.operaciones(n1.get(),n2.get(),"+"), text="+")
    #suma.pack()
    resta=Button(frame,command=lambda: funciones.operaciones(n1.get(),n2.get(),"-"), text="-")
    #resta.pack()
    mult=Button(frame,command=lambda: funciones.operaciones(n1.get(),n2.get(),"*"), text="*")
    #mult.pack()
    div=Button(frame,command=lambda: funciones.operaciones(n1.get(),n2.get(),"/"), text="/")
    #div.pack()
    suma.grid(row=5, column=0,padx=5) 
    resta.grid(row=5, column=1,padx=5)
    mult.grid(row=5, column=2,padx=5)
    div.grid(row=5, column=3,padx=5)

    salir=Button(ventana,text="Salir",command=ventana.quit)
    salir.pack()
    ventana.mainloop()