from tkinter import *

ventana=Tk()
ventana.title("Personalizar widgets")
ventana.geometry("500x500")

def cambio():
    etiqueta.config(
        text="POO con python!",
        bg="pink",
        fg="purple",
        state=DISABLED
    )

def regresar():
    etiqueta.config(
        text="Bienvenidos a Tkinter",
        bg="Lightblue",
        fg="darkblue",
    )

etiqueta=Label(ventana)
etiqueta.config(
    text="Bienvenidos a Tkinter",
    bg="Lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=SOLID,
    cursor="heart"
)
etiqueta.pack(pady=25)

btn1=Button(ventana,text="Click Aquí",command=cambio)
btn1.config(
    bg="blue",
    fg="white",
    #width=50,
    #height=4,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="pink",
    activebackground="red",
    cursor="star"
)
btn1.pack(pady=20)

btn2=Button(ventana,text="Regresar",command=regresar)
btn2.config(
    bg="Purple",
    fg="Pink",
    #width=50,
    #height=4,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activeforeground="pink",
    activebackground="lightblue"
)
btn2.pack(pady=20)

ventana.mainloop()