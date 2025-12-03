from tkinter import *

v=Tk()

# <Button>- Se hizo clic en el elemento
# <Double-Button>- Se hizo doble clic en el elemento
# <Triple-Button>- Se hizo triple clic en el elemento
# <ButtonPress>- Se ha iniciado un clic en el elemento
# <ButtonRelease>- Se activó un clic en el elemento
# <Button-1>	Se hizo clic con el botón primario (izquierdo).
# <Button-2>	Se hizo clic con el botón central (generalmente la rueda).
# <Button-3>	Se hizo clic con el botón secundario (derecho).
# <ButtonPress-1>	Se ha iniciado un clic (se presionó) con el botón primario.
# <ButtonRelease-1>	Se completó un clic (se soltó) con el botón primario.
# <Motion>	El puntero se ha movido (a veces usado para arrastrar o "drag").
# <Enter>	El puntero del ratón ha entrado en el área del elemento.
# <Leave>	El puntero del ratón ha salido del área del elemento.
# <Double-Button-1>	Se hizo doble clic con el botón primario.
# <Triple-Button-1>	Se hizo triple clic con el botón primario.
# <MouseWheel>	Se movió la rueda del ratón (hacia arriba o abajo).


def accion(event):
    mensaje.config(text="holaaa")

v.bind("<Button-1>",accion)

mensaje=Label(v,text="interactua")
mensaje.pack()

v.mainloop()