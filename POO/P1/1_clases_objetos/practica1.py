""""
Practica #1 Implementar paradgima estructurado VS OO
Crear un programa que obtenga el area de un rectangulo 
"""
import os
os.system

#1.-Estructurado
def areaRectangulo():
   base = 9 #variable, expresion de asignasion asignasion 
   altura = 5 
   area = base * altura #Expresion aritmetica
   print(f"El area de tu rectangulo es: {area}")

areaRectangulo()

#2.- OO
class AreaRectangulo:
   def areaRectangulo(self, base, altura):
     area = base * altura 
     return area
   
rectangulo1 = AreaRectangulo() #instanciar un objeto de la clase "AreaRectangulo"

print(f"El area de tu rectangulo es: {rectangulo1.areaRectangulo(9,5)}")


class AreaRectangulo:
   def __init__(self, base, altura):
      self.base =  base
      self.altura = altura

   def areaRectangulo(self):
     area = self.base * self.altura 
     return area
   
rectangulo1 = AreaRectangulo(9,5) #instanciar un objeto de la clase "AreaRectangulo"

print(f"El area de tu rectangulo es: {rectangulo1.areaRectangulo()}")