from tkinter import *

ventana=Tk()
ventana.geometry("500x500")
ventana.title("RadioButton")

def mostrarEstado():      
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

valor=IntVar
bar=Scale(ventana, from_=0,to=100,orient=HORIZONTAL,relief=FLAT,variable=valor)
bar.pack(pady=10)

confirmar=Button(ventana,text="Mostrar Opcion",command=mostrarEstado)
confirmar.pack()

resultado=Label(ventana,text="")
resultado.pack(pady=10)



ventana.mainloop()