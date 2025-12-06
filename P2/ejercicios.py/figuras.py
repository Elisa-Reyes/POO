class Figuras:
    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible

    #checaaaaar
    def estaVisible(self):
        if self.visible==False:
            respuesta="no visible"
        else:
            respuesta="visible"
        return respuesta
    
    def mostrar(self):
        return self.x,self.y
    
    def ocultar(self):
        import os
        os.system("cls")

    def mover(self, nuevox, nuevoy):
        self.x=nuevox
        self.y=nuevoy
        return self.x,self.y
    
    def calcularArea(self):
        area=self.x*self.y
        return f"{area}"
    

figura1= Figuras(15,10,True)
print(Figuras.mostrar())
print(Figuras.calcularArea())
