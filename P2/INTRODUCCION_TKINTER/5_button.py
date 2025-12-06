import tkinter as tk
from tkinter import *

def cambiar_texto():
    nombre.config(text="Elisa Desiree Reyes Perez")
    contrasena.config(text="hola1234")

def regresar_texto():
    nombre.config(text="Nombre: ")
    contrasena.config(text="Contraseña: ")

ventana= tk.Tk()
ventana.title("Bot0nes, marcos, etiquetas")
ventana.geometry("800x600")
ventana.resizable(False,False)

frame_principal=Frame(ventana)
frame_principal.config(
    width=800,
    height=100,
    bg="#B6B0F3",
    border=2,
    relief=SOLID,
    bd=2
)

frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)


titulo=Label(frame_principal)
titulo.config(
    text="Inicio de Sesion",
    bg="#B6B0F3",
    font=50
)
titulo.pack()
nombre=Label(ventana,text="Nombre: ")
nombre.pack(pady=10)
contrasena=Label(ventana,text="Contraseña: ")
contrasena.pack(pady=10)

buttom_acceptar=Button(ventana,text="Aceptar",command=cambiar_texto)
buttom_acceptar.pack(pady=10)
boton_regresar=Button(ventana,text="Regresar",command=regresar_texto)
boton_regresar.pack(pady=10)


ventana.mainloop()