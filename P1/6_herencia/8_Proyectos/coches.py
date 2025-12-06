class Coches:

    '''
    -.METODO CONSTRUCTOR
    Con este metodo se inicializa un objeto por primera vez cuando es creado con valores iniciales
    '''
    def __init__(jeff):
        __marca=""
        __color=""
        __modelo=""
        __velocidad=0
        __caballaje=0
        __plazas=0

    def __init__(jeff,marca,color,modelo,velocidad,caballaje,plazas):
        __marca=marca
        __color=color
        __modelo=modelo
        __velocidad=velocidad
        __caballaje=caballaje
        __plazas=plazas

    '''
    Crear los metodos setter y getters. Son importantes y necesarios en todas las clases para que el programador 
    interactue con los vlaoresde los atributos a traves de estos metodos. Es la manera mas adecuada y recomendada 
    para solicitar un valor (get) y/o para ingresar o cambiar un valr (set) a un atributo en particular de la clase a traves
    de un objeto.
    En teoría se debería de crear un metodo getters y setters por cada atributo que contenga la clase.
    Los metodos get siempre regresan valor, es decir, el valor de la propiedad a traves de un return.
    por otro lado, el metodo set siempre recibe parametros para cambiar o modificar el vslor del atributo o propiedades en cuestión
    '''
    def acelerar(jeff):
        return "estoy acelerando el coche"

    def frenar(jeff):
        return "estoy frenandooooo"

    @property
    def marca(jeff):
        return jeff.__marca

    @marca.setter
    def setMarca(jeff,marca):
        jeff.__marca=marca

    def getColor(jeff):
        return jeff.__color

    def setColor(jeff,color):
        jeff.__color=color

    def getVel(Jeff):
        return Jeff.__velocidad

    def setVel(Jeff,velocidad):
        Jeff.__velocidad=velocidad

    def getModelo(Jeff):
        return Jeff.__modelo

    def setModelo(Jeff,Modelo):
        Jeff.__modelo=Modelo

    def getCab(Jeff):
        return Jeff.__caballaje

    def setCab(Jeff,caballaje):
        Jeff.__caballaje=caballaje
    
    def getPlaza(Jeff):
        return Jeff.__plazas

    def setPlazas(Jeff,plazas):
        Jeff.__plazas=plazas

#Ya con constructor



#print(coche1.acelerar(50))


