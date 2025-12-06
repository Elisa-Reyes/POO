class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    #metodos
    def inscribirse(self):
        print("El alumno se inscribió")

    def estudiar(self):
        print("El alumno estudió")

    #setters y asi
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad=edad

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula=matricula

class Profesores:
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor

    #metodos
    def impartir(self):
        print("El profesor impartió la clase")

    def evaluar(self):
        print("El profesor evaluo a los alumnos")

    #setters y asi
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def experiencia(self):
        return self.__experiencia
    
    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia=experiencia

    @property
    def num_profesor(self):
        return self.__num_profesor
    
    @num_profesor.setter
    def num_profesor(self, num):
        self.__num_profesor=num

class Cursos:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    #metodos
    def asignar(self):
        print("Se asignó el curso")

    #setters y asi
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo=codigo

    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self, creditos):
        self.__creditos=creditos

alumno1=Alumnos()
alumno1.nombre="Juan"
alumno1.edad=15
alumno1.matricula=123

alumno2=Alumnos()
alumno2.nombre="Yoko"
alumno2.edad=10
alumno2.matricula=124

profe1=Profesores()
profe1.nombre="Juan"
profe1.experiencia=15
profe1.num_profesor=4

profe2=Profesores()
profe2.nombre="Juan2"
profe2.experiencia=16
profe2.num_profesor=5

curso1=Cursos()
curso1.nombre="mate"
curso1.codigo=2
curso1.creditos=30

curso2=Cursos()
curso2.nombre="calculo"
curso2.codigo=3
curso2.creditos=40