from tkinter import *
from tkinter import messagebox
from model import operacion

class Controladores:
    @staticmethod
    def operaciones(n1,n2,op):
        if op=="+":
            resultado= n1+n2  
        elif op=="-":
            resultado= n1-n2
        elif op=="*":
            resultado= n1*n2
        elif op=="/":
            resultado= n1/n2
        result= messagebox.showinfo(message=f"{n1}{op}{n2}={resultado} \n quieres guardar la operacion en la base de datos?",icon="question")
        if result=="yes":
            operacion.Operaciones.insertar(n1,n2,op,resultado)
    

# Controladores.operaciones(5,6,"+")