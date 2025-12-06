from tkinter import *

ventana=Tk()
ventana.title("Personalizar widgets")
ventana.geometry("800x500")
ventana.config(
    cursor="heart", bg="#FC00CE"
    )

def cambiar():
    nombre=texto1.get()
    lbl_result.config(
        text=f"Bienvenido al sistema, {nombre}", 
        font=("Times New Roman",30),
        relief=GROOVE,
        border=2,
        background="#00eeff"
    )

def reg():
    texto1.delete(0, END)
    texto2.delete(0,END)
    color_defecto=ventana.cget("bg")

et=Label(ventana,text="Acceso al sistema",bg="#00FC71")
et.config(
    fg="darkblue",
    width=50,
    height=4, 
    font=("Helvetica",20)
    )
et.pack(pady=10)

et2=Label(ventana)
et2.config(
    text="Nombre:",
    bg="#FC00CE",
    font=20
)
et2.pack(pady=10)

texto1=Entry(ventana,width=30)
texto1.pack(pady=10)

et3=Label(ventana)
et3.config(
    text="Contraseña:",
    bg="#FC00CE",
    font=20
)
et3.pack(pady=10)

texto2=Entry(ventana,width=30,show="+")
texto2.pack(pady=10)

boton=Button(ventana,text="Entrar",command=cambiar,cursor="star")
boton.pack(pady=10)

boton2=Button(ventana,text="Regresar",command=reg,cursor="star")
boton2.pack(pady=10)

lbl_result=Label(ventana,text="",bg="#FC00CE")
lbl_result.pack(pady=10)

ventana.mainloop()