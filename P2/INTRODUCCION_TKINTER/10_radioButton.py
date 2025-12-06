from tkinter import *

ventana=Tk()
ventana.geometry("500x500")
ventana.title("RadioButton")

def mostrarEstado():      
    resultado.config(text=f"Opcion seleccionada: {opcion.get()}")

opcion=StringVar()
op1=Radiobutton(ventana,text="Opción 1",variable=opcion,value="Opción 1")
op1.pack()

op2=Radiobutton(ventana,text="Opción 2",variable=opcion,value="Opción 2")
op2.pack()

op3=Radiobutton(ventana,text="Opción 3",variable=opcion,value="Opción 3")
op3.pack()

confirmar=Button(ventana,text="Mostrar Opcion",command=mostrarEstado)
confirmar.pack()

resultado=Label(ventana,text="")
resultado.pack(pady=10)



ventana.mainloop()