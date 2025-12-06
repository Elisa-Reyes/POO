import tkinter as tk

ventana = tk.Tk()

ventana.title("google")
ventana.geometry("600x300")
#icono = PhotoImage(file='imagen.png')
#ventana.iconphoto(True,icono)

saludo = tk.Label(text="Holaaaaa")
saludo.pack()

ventana.config(background="#6C91B9")

ventana.mainloop()

