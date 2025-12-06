<<<<<<< HEAD
'''
1er Diciembre
    1) Implememntar mvc
    2) POO
    3) Interfaces:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()
    Entregables:
    **Estructura principal del proyecto en MVC
    **Módulo principal Main
    **Nombre del commit: commit_01_12_25

3ero Diciembre
    1) Interfaces:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()

'''

from view import vista
from tkinter import *

class App:
    def __init__(self,ventana):
        view=vista.View(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
=======
'''
1er Diciembre
    1) Implememntar mvc
    2) POO
    3) Interfaces:
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()
    Entregables:
    **Estructura principal del proyecto en MVC
    **Módulo principal Main
    **Nombre del commit: commit_01_12_25

3ero Diciembre
    1) Interfaces:
        1.1 insertar_camionetas()
        1.2 consultar_camionetas()
        1.3 cambiar_camionetas()
        1.4 borrar_camionetas()
        2.1 insertar_camiones()
        2.2 consultar_camiones()
        2.3 cambiar_camiones()
        2.4 borrar_camiones()

4to Diciembre
    1) Controlador
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_autos()
        3.4 consultar_autos()
        3.5 cambiar_autos()
        3.6 borrar_autos()

5to Diciembre
    1) Controlador
        3.1 menu_principal()
        3.2 menu_acciones()
        3.3 insertar_camionetas()
        3.4 consultar_camionetas()
        3.5 cambiar_camionetas()
        3.6 borrar_camionetas()
'''

from view import vista
from tkinter import *

class App:
    def __init__(self,ventana):
        view=vista.View(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
>>>>>>> master
    ventana.mainloop()