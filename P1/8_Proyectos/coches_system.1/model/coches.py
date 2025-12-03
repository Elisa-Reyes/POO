import os
os.system("clear")

class Coches:

    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
      self._marca=marca
      self._color=color
      self._modelo=modelo
      self._velocidad=velocidad
      self._caballaje=caballaje
      self._plazas=plazas

    #metodos Set y Get
    @property
    def marca(self):
       return self._marca
    
    @marca.setter
    def marca(self,marca):
       self._marca=marca

    @property
    def color(self):
       return self._color
    
    @color.setter
    def color(self,color):
       self._color=color

    @property
    def modelo(self):
       return self._modelo
    
    @modelo.setter
    def modelo(self,modelo):
       self._modelo=modelo

    @property
    def velocidad(self):
       return self._velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
       self._velocidad=velocidad

    @property
    def caballaje(self):
       return self._caballaje
    
    @caballaje.setter
    def caballaje(self,caballaje):
       self._caballaje=caballaje 

    @property
    def plazas(self):
       return self._plazas
    
    @plazas.setter
    def plazas(self,plazas):
       self._plazas=plazas        
    

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
      return "Estoy acelerando el coche"

    def frenar(self):
      return "Estoy frenando el coche"  

class Camiones(Coches):
      def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

      #metodos set y get
      @property
      def eje(self):
         return self.__eje
      
      @eje.setter
      def eje(self,eje):
        self.__eje=eje 

      @property
      def capacidadCarga(self):
         return self.__capacidadCarga
      
      @capacidadCarga.setter
      def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga 

      #metodos

      def cargar(self,tipo_carga):
         self.__tipo_carga=tipo_carga
         return self.__tipo_carga
      
      def acelerar(self):
       return "Estoy acelerando el camion"

      def frenar(self):
       return "Estoy frenando el camion"  

class Camionetas(Coches):
      def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

      #metodos set y get
      @property
      def traccion(self):
         return self.__traccion
      
      @traccion.setter
      def traccion(self,traccion):
        self.__traccion=traccion 

      @property
      def cerrada(self):
         return self.__cerrada
      
      @cerrada.setter
      def cerrada(self,cerrada):
        self.__cerrada=cerrada 

      #metodos

      def transportar(self,num_pasajeros):
         self.__num_pasajeros=num_pasajeros
         return self.__num_pasajeros
      
      def acelerar(self):
       return "Estoy acelerando la camioneta"

      def frenar(self):
       return "Estoy frenando la camioneta" 




