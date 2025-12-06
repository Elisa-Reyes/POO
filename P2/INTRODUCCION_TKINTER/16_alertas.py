from tkinter import *
from tkinter import messagebox


ventana=Tk()
ventana.title("Alertas")
ventana.geometry("800x600")


def alerta1():
    nombreObtenido=cadena.get()
    etiqueta.config(text=f"{nombreObtenido}")
    resultado=messagebox.showinfo(message=f"{nombreObtenido}",icon="info")

def alerta2():
    resultado=messagebox.askquestion(message="¿Quires continuar ejecutando la aplicación?",icon="question")
    if resultado!="yes":
        ventana.destroy()
    
   

cadena=StringVar()
caja1=Entry(ventana, textvariable=cadena)
caja1.pack()

boton1=Button(ventana, text="Alerta", command=alerta1)
boton1.pack()


boton2=Button(ventana, text="Otra Alerta", command=alerta2)
boton2.pack()

etiqueta=Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()