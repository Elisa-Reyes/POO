import tkinter as tk
from tkinter import *

ventana= tk.Tk()
ventana.title("Uso del mainloop")
ventana.geometry("600x400")

marco1=Frame(ventana,width=600,height=50,bg="#e80606",border=2,relief=RAISED).pack()
marco2=Frame(ventana,width=600,height=50,bg="#F59610",border=2,relief=RAISED).pack()
marco3=Frame(ventana,width=600,height=50,bg="#E6F510",border=2,relief=RAISED).pack()
marco4=Frame(ventana,width=600,height=50,bg="#10F542",border=2,relief=RAISED).pack()
marco5=Frame(ventana,width=600,height=50,bg="#2310F5",border=2,relief=RAISED).pack()
marco6=Frame(ventana,width=600,height=50,bg="#CF10F5",border=2,relief=RAISED).pack()


ventana.mainloop()