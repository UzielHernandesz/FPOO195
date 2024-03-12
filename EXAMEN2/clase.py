import sys
#Creamos la clase
class alumno:
    
    def __init__(self,apellidoM,nombreS,apellidoP,carrerA,añonamientO ):
        self.nombre= nombreS
        self.apellip= apellidoP
        self.apellim= apellidoM
        self.añonacimi= añonamientO
        self.carre=carrerA

#solicitar datos
#print("===============Datos del Alumno==============")
#nombreS= input("Escribe el nombre : ")
#apellidoP= input("Escribe el apellido Paterno: ")
#apellidoM= input("Escribe el apellido Materno: ")
#añonamientO= int(input("Escribe el año de nacimiento: "))
#carrerA= input("Escribe en que carrera estas: ")
#print("==============Datos del Alumno===============")



#creamos nuestra instancia
alumno= alumno(nombreS,apellidoP,apellidoM,añonamientO,carrerA)


#usamos los atributos del alumno
print("============Informacion del alumno es: ==========")
print(nombreS)
print(apellidoP)
print(apellidoM)
print(añonamientO)
print(carrerA)
print("")