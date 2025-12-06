from tkinter import *

ventana=Tk()
ventana.geometry("500x500")
ventana.title("CheckButton")

def mostrarEstado():
    if opcion.get()==1:
        resultado.config(text="Notificaciones Activadas")
    else:
        resultado.config(text="Notificaciones Desactivadas")

opcion=IntVar()
checkbox=Checkbutton(ventana,text="deseas recibir notificsciones?",variable=opcion,onvalue=1,offvalue=0)
checkbox.pack()

confirmar=Button(ventana,text="Confirmar",command=mostrarEstado)
confirmar.pack()

resultado=Label(ventana,text="")
resultado.pack(pady=10)



ventana.mainloop()