from view import view_1
from tkinter import *

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        view = view_1.View(ventana)
        


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()