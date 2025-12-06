class Calculadora:
    def __init__(self): #las cosas de adentro no se ponen ahí, nmms
        self._num1=0 #eso ahí está bien
        self._num2=0
    
    def multi(self):
        resp=self._num1*self._num2
        return resp
    
    def divi(self):
        resp=self._num1/self._num2
        return resp
    
    def sum(self):
        resp=self._num1+self._num2
        return resp
    
    def res(self):
        resp=self._num1-self._num2
        return resp  

    #Setters y getters
    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1 (self, num1):
        self._num1=num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2 (self, num2):
        self._num2=num2
    
numeros=Calculadora()
numeros.num1=int(input("numero 1: "))
numeros.num2=int(input("numero 2: "))

print(f"multiplicacion= {numeros.multi()}")
print(f"Division= {numeros.divi()}")
print(f"suma= {numeros.sum()}")
print(f"resta= {numeros.res()}")

'''
Más o menos está bien todo, solo que en los constructores no puedes poner los atributos que vas
a definir. SOLO ERA ESOOOOOOOO WOOOOOOOOO 

class Calculadora:
    def __init__(self,num1,num2): las cosas de adentro no se ponen ahí, nmms
        self.num1=0 
        delf.num2=0


(Solo eso y funciona, pero obviamente hay mejores formas de hacer eso)

-No era pauta peeeeeeeero se tienen que proteger los atributos.
-Puedes poner la pregunta directamente en el constructor
class Calculadora:
    def __init__(self): 
        self.num1=int(input("numero 1: "))
        delf.num2=int(input("numero 2: "))

- Puedes ahorrarte eso:
    def res(self):
        resp=self.num1-self.num2
        return resp   

--Y poner:
    def res(self):
        return self.num1-self.num2 

_ Tienes que poner getters y setters también
'''