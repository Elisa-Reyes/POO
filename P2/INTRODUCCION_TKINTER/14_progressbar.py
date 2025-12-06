from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")

def progreso():
    barra['value']=0
    ventana.update
    for i in range(100):
        barra['value']=1
        ventana.update
        ventana.after(50)

barra=ttk.Progressbar(ventana,mode="determinate",length=200)
barra.pack(pady=10)

confirmar=Button(ventana,text="Mostrar Opcion", command=progreso)
confirmar.pack(pady=10)



ventana.mainloop()