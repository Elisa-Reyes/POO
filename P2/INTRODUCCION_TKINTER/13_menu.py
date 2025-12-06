from tkinter import *

ventana=Tk()
ventana.title("Menu")
ventana.geometry("500x500")

def mostrarEstado(seleccion):  
    if seleccion:
        resultado.config(text=f"{seleccion}")

menuBar=Menu(ventana)
ventana.config(menu=menuBar)

resultado=Label(ventana,text="")
resultado.pack(pady=10)


archivoMenu=Menu(menuBar, tearoff=False)

menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo", command=lambda: mostrarEstado("Nuevo archivo"))
archivoMenu.add_command(label="Guardar archivo", command=lambda: mostrarEstado("Guardar archivo"))
archivoMenu.add_command(label="Abrir archivo", command=lambda: mostrarEstado("Abrir archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)

editarMenu=Menu(menuBar, tearoff=False)

menuBar.add_cascade(label="Editar", menu=editarMenu)
editarMenu.add_command(label="copiar", command=lambda: mostrarEstado("copiado"))
editarMenu.add_command(label="recortar", command=lambda: mostrarEstado("recortado"))
editarMenu.add_separator()
editarMenu.add_command(label="Salir", command=ventana.quit)

ventana.mainloop()