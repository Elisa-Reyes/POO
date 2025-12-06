from tkinter import *
from tkinter import ttk
import os

ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")

def mensaje(tipo):
    resultado.config(text=f"{tipo}")

# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base,"logo.png")

#primera forma
#PhotoImage, puro .png, .gif y pgm o ppm
if not os.path.exists(ruta_imagen):
    print(f"Error: No se encontró la imagen en {ruta_imagen}")
else:
    print(f"Imagen encontrada en: {ruta_imagen}")

# SOLUCIÓN: Guardar la referencia como atributo de la ventana
ventana.imagen = PhotoImage(file=ruta_imagen)

# Mostrar la imagen dentro de un label y button
etiqueta = Label(ventana, image=ventana.imagen)
etiqueta.pack()

boton = Button(ventana, image=ventana.imagen, command=lambda: mensaje("Hola Mundo"))
boton.pack(pady=10)

resultado = Label(ventana, text="")
resultado.pack(pady=10)

ventana.mainloop()