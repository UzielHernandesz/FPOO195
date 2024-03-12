import sys
from interfaz import interfaz 
from Persona import Persona

#Creamos la clase
class alumno:
    
    def __init__(self,esp,nom,apellidoP):
        self.__especie= esp
        self.__nombre= nom
        self.__apellip= apellidoP
        #_ despues del punto es para hacerlo privado 
    #No va entre comillas por que queremos que sea flotante float
    #_ ANTES DEL NOMBRE Y YA LOS HACEMOS PRIVADOS
    #Getters (metodos Get)
    
    def get__especie(self):
        return self.__especie
    
    def get__nombre(self):
        return self.__nombre
    
    def get__apellip(self):
        return self.__altura
    
    #Setters ( metodos Set)
    
    def set__especie(self, __especie):
        self.__especie = __especie
    
    def set__nombre(self, __nombre):
        self.__nombre = __nombre
    
    def set__apellip(self, __altura):
        self.__altura= __altura

#solicitar datos
print("===============Datos del Alumno==============")
nombreS= input("Escribe el nombre : ")
apellidoP= input("Escribe el apellido Paterno: ")
apellidoM= input (input("Escribe el apellido Materno: "))
añonamientO= float(input("Escribe el año de nacimiento: "))
carrerA= input("Escribe en que carrera estas: ")
print("==============Datos del Alumno===============")



#creamos nuestra instancia
alumno= alumno(nombreS,apellidoP,apellidoM,añonamientO,carrerA)


#usamos los atributos del spartan
print("============Informacion del alumno es: ==========")
print(alumno.get__nombre())
print(alumno.get__apellido_paterno())
print(alumno.get__altura())
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