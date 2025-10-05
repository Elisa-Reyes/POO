class Coches:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0
    '''
    Crear los metodos setter y getters. Son importantes y necesarios en todas las clases para que el programador 
    interactue con los vlaoresde los atributos a traves de estos metodos. Es la manera mas adecuada y recomendada 
    para solicitar un valor (get) y/o para ingresar o cambiar un valr (set) a un atributo en particular de la clase a traves
    de un objeto.
    En teoría se debería de crear un metodo getters y setters por cada atributo que contenga la clase.
    Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves de un return.
    por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el vslor del atributo o propiedades en cuestión
    '''
    def acelerar(self):
        pass

    def frenar(self):
        pass

    def getMarca(self):
        return self.__marca

    def setMarca(self,marca):
        self.__marca=marca

    def getColor(self):
        return self.__color

    def setColor(self,color):
        self.__color=color

    def getVel(self):
        return self.__velocidad

    def setVel(self,velocidad):
        self.__velocidad=velocidad

    def getModelo(self):
        return self.__modelo

    def setModelo(self,Modelo):
        self.__modelo=Modelo

    def getCab(self):
        return self.__caballaje

    def setCab(self,caballaje):
        self.__caballaje=caballaje
    
    def getPlaza(self):
        return self.__plazas

    def setPlazas(self,plazas):
        self.__plazas=plazas

#coche1=Coches("WV","Blanco","2022",220,150,5)
#coche1=Coches("WV","Azul","2020",180,150,6)

#MULTIPLES OBJETOS

coche1=Coches()
coche2=Coches()

coche1.setMarca("wv")
coche1.setColor("Blanco")
coche1.setModelo("2020")
coche1.setVel(220)
coche1.setCab(180)
coche1.setPlazas(5)
coche1.num_serie="AAAAAAAAAA" #Pueden no tener la misma cantidad de atributos

coche2.setMarca("wv")
coche2.setColor("Azul")
coche2.setModelo("2022")
coche2.setVel(180)
coche2.setCab(150)
coche2.setPlazas(6)

#print(coche1.acelerar(50))

print(f"Coche 1 \nColor: {coche1.getColor} \n{coche1.getMarca}\n{coche1.getCab}\n{coche1.getModelo}\n{coche1.getPlaza}\n{coche1.getVel}")
