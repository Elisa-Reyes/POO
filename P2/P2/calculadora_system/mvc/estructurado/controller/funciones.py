from tkinter import *
from tkinter import messagebox

#Controlador
def operaciones(n1,n2,op):
    if op=="+":
        resultado= n1+n2  
    elif op=="-":
        resultado= n1-n2
    elif op=="*":
        resultado= n1*n2
    elif op=="/":
        resultado= n1/n2
    messagebox.showinfo(message=f"{resultado}")