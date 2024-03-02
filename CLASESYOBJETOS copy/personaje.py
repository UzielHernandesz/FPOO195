
#Creamos la clase
class Personaje:
    
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
        #_ despues del punto es para hacerlo privado 
    #No va entre comillas por que queremos que sea flotante float
    #_ ANTES DEL NOMBRE Y YA LOS HACEMOS PRIVADOS
    #Getters (metodos Get)
    
    def get__especie(self):
        return self.__especie
    
    def get__nombre(self):
        return self.__nombre
    
    def get__altura(self):
        return self.__altura
    
    #Setters ( metodos Set)
    
    def set__especie(self, __especie):
        self.__especie = __especie
    
    def set__nombre(self, __nombre):
        self.__nombre = __nombre
    
    def set__altura(self, __altura):
        self.__altura= __altura
        
    #PONER OTRA VARIABLE AL SET
    
    #Creamos los metodos del personaje
    
    def correr(self,__estado):
        if(__estado): 
            print("El personaje " + self.__nombre + "esta corriendo")
        else:
            print("El personaje " + self.__nombre + "esta muerto")
            
            #self para llamar los propios atributos
            
    def lanzar_Granada(self):
        print(self.__nombre + " pego una buena granada ")
    
    
    #def __pensar(self):
        #print("El personaje" + str(self.__nombre) + " esta pensando")
