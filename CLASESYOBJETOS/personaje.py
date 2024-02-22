
#Creamos la clase
class Personaje:
    
    # Creamos nuestros atributos
    especie= "Humano"
    nombre= "John"
    altura= 2.18 #No va entre comillas por que queremos que sea flotante float
    
    
    
    #Creamos los metodos del personaje
    
    def correr(self,estado):
        if(estado): 
            print("El personaje"+ self.nombre+ "esta corriendo")
        else:
            print("El personaje"+ self.nombre + "esta muerto")
            
            #self para llamar los propios atributos
            
    def lanzar_Granada(self):
        print(self.nombre+ "pego una buena granada")
        
    
    def Recargar_Arma(self, municion):
        cargador= 25
        cargador= cargador + municion
        print("Arma recargada al" + str(cargador) + "%")
        #% para que se vea el porcentaje
        #str por defaul por que estamos hablando de algo numerico
        
#creamos nuestra instancia
spartan= Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)