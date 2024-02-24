
#Creamos la clase
class personaje:
    
    # Creamos nuestros atributos
    especie= "Humano"
    nombre= "John"
    altura= 2.18 #No va entre comillas por que queremos que sea flotante float
    
    
    
    #Creamos los metodos del personaje
    
    def correr(self,estado):
        if(estado): 
            print("El personaje "+ self.nombre+ " esta corriendo")
        else:
            print("El personaje "+ self.nombre + " esta muerto")
            
            #self para llamar los propios atributos
            
    def lanzar_Granada(self):
        print(self.nombre + " pego una buena granada")
        
    

