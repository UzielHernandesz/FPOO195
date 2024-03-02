from Personaje import *  
from Armas import *
# esta es una buena importacion 
# a la clase ponerle el mismo nombre del archivo
#import personaje no se puede hacer esta importacion

#solicitar datos
print("===============Datos del Heroe==============")
nombreS= input("Escribe el nombre de tu Spartan: ")
especieS= input("Escribe la especie de tu Spartan: ")
alturaS= float (input("Escribe la altura de tu Spartan: "))
print("==============Datos del Nemesis===============")
#solicitar datos
print("==============Datos del Nemesis===============")
nombreN= input("Escribe el nombre de tu Nemesis: ")
especieN= input("Escribe la especie de tu Nemesis: ")
alturaN= float (input("Escribe la altura de tu Nemesis: "))
print("==============Datos del Nemesis===============")
#DOS OBJETOS CON CARACTERISTICAS DIFERENTES


#creamos nuestra instancia
spartan= Personaje(especieS,nombreS,alturaS)
Nemesis= Personaje(especieN,nombreN,alturaN)

Arma= Armas()  
# creamos el objeto de la clase personaje   
spartan = Personaje(especieS,nombreS,alturaS)
nemesis = Personaje(especieN,nombreN,alturaN)

#usamos los atributos del spartan
print("============El objeto spartan contiene==========")
print(spartan.get__nombre())
print(spartan.get__especie())
print(spartan.get__altura())
print("")

#usamos los atributos del nemesis
print("============El objeto nemesis contiene==========")
print(nemesis.get__nombre())
print(nemesis.get__especie())
print(nemesis.get__altura())


#Usamos los metodos del spartan
print("============ METODOS DEL OBJETO SPARTAN =============")
spartan.correr(False)
spartan.lanzar_Granada()
print("")

print("============ METODOS DEL OBJETO NEMESIS =============")
nemesis.correr(True)
nemesis.lanzar_Granada()
print("")



#Usamos los metodos del arma
print("=====================SPARTAN===============")
Arma.seleccionar_arma(spartan.get__nombre)
Arma.Recargar_Arma(65)
print("")


print("=====================NEMESIS===============")
Arma.seleccionar_arma(nemesis.get__nombre)
Arma.Recargar_Arma(65)
print("")