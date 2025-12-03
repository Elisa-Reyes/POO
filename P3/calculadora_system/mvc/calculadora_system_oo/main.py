'''
Crear una calculadora
1.- Dps campos de Texto
2.- 4 botones para las operaciones
3.- Mostrar resultados en alerta
5.- estructurada
6.-MVC
'''
from view import interfaz
from tkinter import *

class App:
    def __init__(self,ventana):
        view=interfaz.Vistas(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()