'''
Ejercicio #2 Modelar y diagramar en POO
'''
#clase de coches
class Coches:
    #metodo constructor que inicializa los valores cuando se instancia un objeto de la clase Coches

    def __init__(self,color,marca,velocidad): 
        self.__color=color #atributos del objeto
        self.__marca=marca
        self.__velocidad=velocidad

    #metodos del objeto
    def acelerar(self,incremento):
        self.__velocidad=incremento+self.__velocidad
        return self.__velocidad
    
    def frenar(self,decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    
    def tocar_claxon(self):
        print("pIIIIIIIIIIIIIIII1111111")
    
#instanciar o crear objetos de la clase Coches
coche1=Coches("blanco","marca",220)
coche2=Coches("Amarillo","Nissan",180)

#Pero se pueden usar los metodos
print(coche1.acelerar(90))
print(coche2.tocar_claxon)
print(coche2.frenar(100))

#aqui no se pueden usar losatributos porque son privados. Cuando solo usas un guion bajo esta protejido pero se puede usar. 
#Pero solo se proteje si se van a heredar atributos.
#print(f"Los valores del objeto 1 son: {coche1.__marca},{coche1.__color},{coche1.__velocidad}")
#print(f"Coche 1 acelero de {coche1.__velocidad} a {coche1.acelerar(50)}")
#en lugar de hacer eso puedes poner directamente coche1.acelerar(50) en lugar de velocidad en el segundo corchete.
#print(f"Los valores del objeto 2 son: {coche2.__marca},{coche2.__color},{coche2.__velocidad}")
#print(f"Coche 2 freno de {coche2.__velocidad} a {coche2.frenar(50)}")
    #se puede llamar de cualquier manera la self, pero lo llamaremos jeff. 
    #Self es para usarlo fuera de los metodos y sea global en la clase
    #Se pueden poner las cosas directamente, sin el def init y con valores ya definidos, 
    #pero se asignan hasta que se invocan, pero al segundo objeto tmb le pone lo mismo. Se puede sobreescribir tho.
    #Al ponerle self.__atributo, se hace privado, sin __ es publico