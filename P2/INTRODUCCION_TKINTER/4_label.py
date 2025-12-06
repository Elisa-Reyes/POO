import tkinter as tk
from tkinter import *

ventana= tk.Tk()
ventana.title("Etiquetas")
ventana.geometry("600x400")
ventana.resizable(False,False)

marco1=Frame(ventana,width=300,height=100,bg="#B6B0F3",border=2,relief=GROOVE,bd=2)
marco1.pack_propagate(False)
marco1.pack()

marco2=Frame(ventana,width=300,height=100,bg="#CF10F5",border=2,relief=FLAT,bd=2)
marco2.pack_propagate(False)
marco2.pack()

marco3=Frame(ventana,width=300,height=100,bg="#F510CB",border=2,relief=FLAT,bd=2)
marco3.pack_propagate(False)
marco3.pack()

#marco4=Frame(ventana,width=300,height=100,bg="#F510CB",border=2,relief=FLAT,bd=2)
#marco4.pack_propagate(False)
#marco4.pack()

#Etiquetas

etiqueta1=Label(marco1,text="Reyes Perex Elisa Desiree",bg="#B6B0F3").pack(pady=10)
etiqueta2=Label(marco2,text="Universidad Tecnológica de Durango",bg="#CF10F5").pack(pady=10)
etiqueta3=Label(marco3,text="Tecnologías de la Información",bg="#F510CB").pack(pady=10)
ventana.mainloop()