
#Creamos la clase
class Personaje:
    
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
        
    #No va entre comillas por que queremos que sea flotante float
    #_ ANTES DEL NOMBRE Y YA LOS HACEMOS PRIVADOS
    
    
    #Creamos los metodos del personaje
    
    def correr(self,estado):
        if(estado): 
            print("El personaje"+ self.nombre+ "esta corriendo")
        else:
            print("El personaje"+ self.nombre + "esta muerto")
            
            #self para llamar los propios atributos
            
    def lanzar_Granada(self):
        print(self.nombre+ "pego una buena granada")
        




