from personaje import *  
from Armas import *
# esta es una buena importacion 
# a la clase ponerle el mismo nombre del archivo
#import personaje no se puede hacer esta importacion

#creamos nuestra instancia
spartan= personaje()
Arma= Armas()       

# el de arriba es el objeto
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#Usamos los metodos del spartan
spartan.correr(False)
spartan.lanzar_Granada()



#Usamos los metodos del arma

Arma.seleccionar_arma(spartan.nombre)
Arma.Recargar_Arma(65)


