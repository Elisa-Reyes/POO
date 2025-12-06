import tkinter as tk
from tkinter import *

ventana= tk.Tk()
ventana.title("Marcos o Frame en Tk")
ventana.geometry("850x650")
ventana.resizable(False,False) #no se pueda modificar el tamaño de la ventana

marco1 = Frame(ventana, width=600, height=400, bg="blue")
marco1.pack_propagate(False)#para que no se cambie todoo
marco1.pack(pady=5)
#para que se muestre dentro de la ventana

marco2 = Frame(marco1, width=300, height=150, bg="silver", bd=5, relief=SOLID)
marco2.pack(pady=5)

ventana.mainloop()

