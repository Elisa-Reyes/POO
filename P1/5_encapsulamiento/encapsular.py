'''
Encapsular.- pilar de la POO que permite indicar cual es la manera de como poder usar los atributos y metodos de una clase 
a la hora de usar en onjetos o en herencia.
'''

import os
os.system("cls")

class Clase:
    atributo_publico="soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"
    #_valor=__atributo_privado para acceder a los valores (opcion 1)

    def __init__(self,color,tamaño):
        self.__color=color
        self.__tamaño=tamaño

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self,tamano):
        self.__tamano=tamano

    @property
    def publico(self):
        return self.atributo_publico
    
    @publico.setter
    def publico(self,public):
        self.atributo_publico=public

    @property
    def protegido(self):
        return self._atributo_protegido
    
    @protegido.setter
    def publico(self,protected):
        self._atributo_protegido=protected   

    @property
    def privado(self):
        return self.__atributo_privado
    
    @privado.setter
    def publico(self,private):
        self.__atributo_privado=private   

    #Opcion 2, con metodos
    def getAtributoPrivado(self):
        return self.__atributo_privado
    

#Utilizar clase (pero es mala practicaaaa, es más recomendable usar metodos)
objeto=Clase("Blanco","Grande")
#print(objeto.atributo_publico)
#print(objeto._atributo_protegido)

print(objeto.privado)
print(objeto.protegido)
print(objeto.publico)
#Da error porque los atributos privados no pueden ser accesibles desde afuera, no sabe qué hace
#print(objeto.__atributo_privado)

objeto.color="Azul"