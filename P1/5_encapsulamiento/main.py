import coches
#from coches import *
#from coches import Coches

#Instanciar objetos para implementarlos
num_coches=int(input("cuantos coches tienes?"))

for i in range(0,num_coches):
    print(f"Datos del coche {i+1}")
    marca=input("marca: ")
    color=input("color: ")
    modelo=input("modelo:")
    velocidad=int(input("velocidad: "))
    potencia=int(input("potencia: "))
    plazas=int(input("plazas: "))

    coche1=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"datos del vehiculo: {coche1.__marca}")

#coche1=coches.Coches("WV","Azul","2020",180,150,6)
#coche3=coches.Coches("Honda")

#MULTIPLES OBJETOS

#coche1=Coches()
#coche2=Coches()

'''
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
'''

