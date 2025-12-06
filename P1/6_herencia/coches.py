class Coches:

    '''
    -.METODO CONSTRUCTOR
    Con este metodo se inicializa un objeto por primera vez cuando es creado con valores iniciales
    '''

    def __init__(jeff,marca,color,modelo,velocidad,caballaje,plazas):
        _marca=marca
        _color=color
        _modelo=modelo
        _velocidad=velocidad
        _caballaje=caballaje
        _plazas=plazas

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
        return jeff._marca

    @marca.setter
    def setMarca(jeff,marca):
        jeff._marca=marca

    @property
    def color(jeff):
        return jeff._color

    @color.setter
    def color(jeff,color):
        jeff._color=color

    @property
    def vel(Jeff):
        return Jeff._velocidad

    @vel.setter
    def vel(Jeff,velocidad):
        Jeff._velocidad=velocidad

    @property
    def modelo(Jeff):
        return Jeff._modelo

    @modelo.setter
    def modelo(Jeff,Modelo):
        Jeff._modelo=Modelo

    @property
    def cab(Jeff):
        return Jeff._caballaje

    @cab.setter
    def cab(Jeff,caballaje):
        Jeff._caballaje=caballaje
    
    @property
    def plaza(Jeff):
        return Jeff._plazas

    @plaza.setter
    def plazas(Jeff,plazas):
        Jeff._plazas=plazas

    def acelerar(jeff):
        pass  

    def frenar(jeff):
        pass 

#Ya con constructor


class Camiones(Coches):
    def __init__(jeff, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidad):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        jeff.__eje=eje
        jeff.__capacidad=capacidad

    @property
    def eje(jeff):
        return jeff.__eje
        
    @eje.setter
    def eje(jeff,eje):
        jeff.__eje=eje
        
    @property
    def capacidad(jeff):
        return jeff.__capacidad
        
    @capacidad.setter
    def capacidad(jeff,capacidad):
        jeff.__capacidad=capacidad   

    def cargar(jeff,tipo_carga):
        jeff.__tipo_carga=tipo_carga
        return jeff.__tipo_carga  


class Camionetas(Coches):
    def __init__(jeff, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        jeff.__traccion=traccion
        jeff.__cerrada=cerrada

    @property
    def traccion(jeff):
        return jeff.__traccion
    
    @traccion.setter
    def traccion(jeff,traccion):
        jeff.__traccion=traccion

    @property
    def cerrada(jeff):
        return jeff.__cerrada
    
    @traccion.setter
    def cerrada(jeff,cerrada):
        jeff.__cerrada=cerrada   

    #metodos


    def transportar(jeff,num_pasajeros):
        jeff.__num_pasajeros=num_pasajeros
        return jeff.__num_pasajeros

