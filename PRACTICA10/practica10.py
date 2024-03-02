class usuario:
    def __init__(self,id,nom,apep,apem,corr,contr):
        self.__id= id
        self.__nombre= nom
        self.__apellp= apep
        self.__apellm = apem
        self.__correo = corr
        self.__contraseña = contr
        
        
        #getters
    def getid(self):
        return self.__id
    
    def getnombre(self):
        return self.__nombre
    
    def getapellm(self):
        return self.__apellm
    
    def getapellp(self):
        return self.__apellp
    
    def getcorreo(self):
        return self.__correo
    
    def getcontraseña(self):
        return self.__contraseña
    
    #setters
    
    def setid(self, identif):
        self.__id = identif
        
    def setnombre(self,name):
        self.__nombre = name
        
    def setapellm(self, materno):
        self.__apellm = materno
    
    def setapellp(self, paterno):
        self.__apellp = paterno
        
    def setcorreo(self, corre0):
        self.__correo = corre0
        
    def setcontraseña(self, passw):
        self.__contraseña = passw
    
    
#Creamos los metodos
def CrearUsuario(self,id,nombre,apellp,apellm,correo,contraseña):
    print("El personaje" + id, nombre,apellp,apellm,correo,contraseña)
    
    
    
#def eliminarusuario(self,id):
#   print("El usuario" + id + "a sido eliminado")
    
    
    
#def consultar(self,id,apellp,apellm,nombre):
#   print("El usuario" + id + "es" + apellp,apellm,nombre)


#def editar(self,nombre,apellp,apellm,correo,contraseña)
    #self.setnombre(nombre)
    #self.setapellp(apellp)
    #self.setapellm(apellm)
    #self.setcorreo(correo)
    #self.setcontraseña(contraseña)
    #print("La informacion del usuario" + id)

    
    
    
    
    