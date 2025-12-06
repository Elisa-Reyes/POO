'''
Tk trabaja a traves de interfaces, es una biblioteca de python que permite crear aplicaciones de escritorio
'''

import tkinter as tk

ventana = tk.Tk() #Metodo que permite tener la ventana abierta mientras dure la app activa.
ventana.title("Holaaaaaa")
ventana.geometry("800x600")
ventana.mainloop() #abre la ventana