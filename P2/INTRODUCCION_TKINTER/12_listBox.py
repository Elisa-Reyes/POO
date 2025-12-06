from tkinter import *

ventana=Tk()
ventana.title("listBox")
ventana.geometry("500x500")


def mostrarEstado():    
    seleccion=lista.get(lista.curselection())  
    resultado.config(text=f"Valor/es seleccionado por el usuario: {seleccion}")

lista=Listbox(ventana,width=10,height=5,selectmode=SINGLE)
lista.pack()

confirmar=Button(ventana,text="Mostrar Opcion",command=mostrarEstado)
confirmar.pack()
opciones=['Amarillo','Azul','Rojo','Morado','Rosa']

for i in opciones:
    lista.insert(END,i)

resultado=Label(ventana,text="")
resultado.pack(pady=10)

ventana.mainloop()